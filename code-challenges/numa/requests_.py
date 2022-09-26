import csv
import json

from collections import namedtuple
from pprint import pprint
from sys import argv

import requests

DB_JSON_FILEPATH = 'db.json'

KEYSTRING_BUSINESS_URL = '"businessUrl"'
KEYSTRING_ADDRESS = '"address"'
KEYSTRING_WIFI_FREE = 'free_wifi'
KEYSTRING_ALCOHOL = 'alcohol'

URL_BASE = 'https://www.yelp.com'
URL = URL_BASE + '/search?find_desc={}&find_loc={}'

# Basicaly None returns should have this information.
INFORMATION_NOT_FOUND = 'Information not found.'

Ask = namedtuple('Ask', ['business_terms', 'parameters', 'zipcode'])


def main():
    # TODO: Need refactor.
    ask_terms = argv[1:]
    ask = parse_ask_terms(ask_terms)
    print('Your ask structured is:', ask)
    db = load_db(path=DB_JSON_FILEPATH)

    if ask.zipcode:
        count = count_business_of_zipcode(db, str(ask.zipcode))
        print(
            f'There is(are) {count} business(es) '
            f'in the following zipcode: {ask.zipcode}')
        return

    business_name_terms, zipcode = ask.business_terms[:-1], ask.business_terms[-1]
    business_name = ' '.join(business_name_terms)
    print('business_name to check:', business_name)
    print('zipcode of the business:', zipcode)

    # TODO: We need to improve key fetching to not be linear.
    for id_, business in db.items():
        if business.get('name').lower() == business_name:
            if business_already_saved(business):
                print('Business info:')
                pprint(business)
                return
            break  # Let's use the "business" object.

    url = URL.format(business_name, zipcode)
    print('Find business url:', url)
    response = requests.get(url)
    if response.status_code >= 500:
        print(response)
        print('Server error')
        return

    str_content = str(response.content)
    business_url = get_business_url(str_content)
    print('Business_url', business_url)
    try:
        response = requests.get(business_url)
        str_content = str(response.content)
    except requests.exceptions.ConnectionError as e:
        print('GOT ERROR!')
        print(e)

    business |= get_business(str_content)
    db[id_] = business

    print('New business info will be saved:')
    pprint(business)

    with open(DB_JSON_FILEPATH, 'w') as f:
        json.dump(db, f, indent=2)


def business_already_saved(business):
    return len(business) > 3


def count_business_of_zipcode(db, zipcode):
    return sum(1 for id_, business in db.items() if business['zip_code'] == zipcode)


def parse_zipcode_count(ask_terms):
    # If there is only one arg, It must be an integer
    # to count businesses in this zipcode.
    if len(ask_terms) == 1:
        try:
            return Ask(business_terms=None, parameters=None, zipcode=int(ask_terms[0]))
        except ValueError:
            print(
                'If there is only one arg, It must be an integer '
                f'to count businesses in this zipcode. Arg: "{ask_terms[0]}"')
            return Ask(business_terms=None, parameters=None, zipcode=None)
    return None


def parse_ask_terms(ask_terms):
    ask = parse_zipcode_count(ask_terms)
    if ask is not None:
        return ask

    parameters = {
        'address': False,
        'alcohol': False,
        'phone': False,
        'wifi': False,
    }
    business_terms = []
    for ask_term in ask_terms:
        lower_term = ask_term.lower()
        if lower_term in parameters:
            parameters[lower_term] = True
        else:
            print(f'Ask parameter "{lower_term}" not found. '
                  'It will be a "business term".')
            business_terms.append(lower_term)

    return Ask(business_terms=business_terms, parameters=parameters, zipcode=None)


def load_db(path=DB_JSON_FILEPATH):
    try:
        with open(path) as file:
            db = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(
            "FileNotFoundError or json.decoder.JSONDecodeError. "
            "We are creating our new JSON database.")

        db = {}
        with open('business_list.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for id_, row in enumerate(reader):
                db[id_] = row

        with open(path, 'w') as f:
            json.dump(db, f, indent=2)
    return db


def get_business_url(content):
    business_url = get_string_value_by_keystring(content, KEYSTRING_BUSINESS_URL)
    return business_url and URL_BASE + business_url


def get_business(full_content, address=True, wifi=True, alcohol=True):
    handlers = {}
    if address:
        handlers[KEYSTRING_ADDRESS] = handle_address
    if wifi:
        handlers[KEYSTRING_WIFI_FREE] = handle_wifi
    if alcohol:
        handlers[KEYSTRING_ALCOHOL] = handle_alcohol

    business = {}
    for keystring, handler in handlers.items():
        value = handler(full_content, keystring)
        business[keystring.strip('"')] = value

    return business


def get_dict_by_keystring(line, keystring):
    """Try parsing line in the format: "keystring":["v1","v2",...]
    and return the list
    """
    found_string = ''
    start_position = line.find(keystring)
    start_position_to_return = -1
    if start_position > -1:
        start_string_to_end = line[start_position:]
        end_position = start_string_to_end.find('}') + 2  # Plus to get the '}' char.
        found_string = start_string_to_end[:end_position]
        start_position_to_return = len(keystring) + 1  # Plus to avoid colon
    return eval(found_string[start_position_to_return:-1]) if start_position_to_return > -1 else found_string


def get_string_value_by_keystring(string, keystring):
    """Try parsing line in the format: "keystring":"value" and return value"""
    found_string = ''
    start_position = string.find(keystring)
    start_position_to_return = -1
    if start_position > -1:
        start_string_to_end = string[start_position:]
        end_position = start_string_to_end.find(',')
        found_string = start_string_to_end[:end_position]
        start_position_to_return = len(keystring) + 2  # Plus to avoid colon and double quotes.
    return found_string[start_position_to_return:-1] if start_position_to_return > -1 else found_string


def handle_address(string, keystring):
    return get_dict_by_keystring(string, keystring) or None


def handle_wifi(string, keystring=None):
    if 'Free Wi-Fi' in string:
        return True
    if 'No Wi-Fi' in string:
        return False
    return None


def handle_alcohol(string, keystring=None):
    if 'Full Bar' in string:  # Need to add another term for alcohol=True.
        return True
    if 'No Alcohol' in string:
        return False
    if 'Alcohol' in string:
        print('ALCOHOL')
    return None


if __name__ == '__main__':
    main()
