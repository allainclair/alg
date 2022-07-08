"""It contains some classes to scan the Upwork website."""
import json
import logging
import time

import selenium

import sync_browse as browse


logger = logging.getLogger(__name__)


class BaseProfile:
    def __init__(self, browse, driver, sleeptime, title, tries, url):
        self.browse = browse
        self.driver = driver
        self.profile = None
        self.sleeptime = sleeptime
        self.title = title
        self.tries = tries
        self.url = url

    def __call__(self):
        for i in range(self.tries):
            if self.driver.title == self.title:
                profile = self._getprofile()
                if profile is not None:
                    return profile
                else:
                    logger.warning('Profile is None.')
            else:
                logger.info(f'Trying to visit {self.url}')
                # Try to visit the URL for a basic profile again.
                self.driver.get(self.url)
                logger.info(f'Trying to auth')
                self.browse.try_auth(self.driver, self.sleeptime, self.tries)
            logger.info(f'Try {i + 1}/{self.tries} ...')
            time.sleep(self.sleeptime)
        else:
            logger.error(
                f'It is too many tries ({self.tries}) to scan the profile.')

    def _getprofile(self):
        pass

    def _scanelement(self, xpath):
        for i in range(self.tries):
            element = browse.try_element_by_xpath(self.driver, xpath)
            if element is not None:
                return element
            else:
                logging.warning(f'Scan element try: {i+1}/{self.tries}')

            time.sleep(self.sleeptime)


class MainProfile(BaseProfile):
    def __init__(self, browse, driver, sleeptime, title, tries, url):
        super().__init__(browse, driver, sleeptime, title, tries, url)

    def _handle_element(self, xpath):
        # TODO Refact this.
        element = self._scanelement(xpath)
        if element:
            # Need to open the menu.
            try:
                element.click()
                # We must try to find this class before creating the object.
                if browse.try_element_by_class_name(element, 'org-type') is not None:
                    # First 4 and last 3 fields are not relevant.
                    # It depends on the driver (Firefox or Safari)
                    splitted = element.text.split()[4:-3]

                    return {
                        'name': splitted[0],
                        'surname': ' '.join(splitted[1:-1]),
                        'plan': splitted[-1].lower(),
                    }

            # Sometimes, this exception happens
            # when trying to access element attributes.
            except selenium.common.exceptions.StaleElementReferenceException as e:
                logger.warning('Element action not performed.')

    def _getprofile(self):
        self.profile = self._handle_element(
            "//li[contains(@class, "
            "'nav-dropdown nav-dropdown-account nav-arrow-end')]")
        logging.info(f'Main profile: {self.profile}')
        return self.profile


class ExtraProfile(BaseProfile):
    def __init__(self, browse, driver, sleeptime, title, tries, url):
        super().__init__(browse, driver, sleeptime, title, tries, url)

    def _getprofile(self):
        try:
            self.profile = {}
            element = self._scanelement(
                "//small[contains(@class, 'ng-binding ng-scope')]")
            if element:
                self.profile['visibility'] = element.text.lower()

            element = self._scanelement(
                "//span[contains(@ng-if, 'vm.profile.availability.capacity')]")
            if element:
                self.profile['availability'] = element.text.lower()

            logging.info(f'Extra profile: {self.profile}')
            return self.profile
        except selenium.common.exceptions.StaleElementReferenceException as e:
            logger.warning('Element action not performed.')


class ContactInfo(BaseProfile):
    def __init__(self, browse, driver, sleeptime, title, tries, url):
        super().__init__(browse, driver, sleeptime, title, tries, url)

    def _getprofile(self):
        # TODO: Maybe break it in some methods.
        fields = {}

        xpath = "//div[contains(@data-test, 'userId')]"
        id_ = self._scandata(xpath, 'text')
        fields['id'] = id_
        fields |= {'employer': 'upwork'}
        fields['account'] = None

        xpath = "//div[contains(@data-test, 'userName')]"
        name = self._scandata(xpath, 'text')
        full_name_splitted = name.split()
        fields['full_name'] = ' '.join(full_name_splitted)
        fields['first_name'] = full_name_splitted[0]
        fields['last_name'] = ' '.join(full_name_splitted[1:])

        xpath = "//div[contains(@data-test, 'phone')]"
        phone = self._scandata(xpath, 'text')
        fields['phone_number'] = ''.join(phone.split())

        address = {}
        fields['address'] = address

        xpath = "//span[contains(@data-test, 'addressStreet')]"
        address_street = self._scandata(xpath, 'text')

        xpath = "//span[contains(@data-test, 'addressStreet2')]"
        address_street2 = self._scandata(xpath, 'text')

        address['line1'] = f"{address_street2} {address_street}"
        address['line2'] = None

        xpath = "//span[contains(@data-test, 'addressCity')]"
        address_city = self._scandata(xpath, 'text')
        address['city'] = address_city

        xpath = "//span[contains(@data-test, 'addressState')]"
        address_state = self._scandata(xpath, 'text')
        # Strip first comma and all other spaces if we have it.
        address['state'] = address_state.strip(',').strip()

        xpath = "//span[contains(@data-test, 'addressZip')]"
        address_postal = self._scandata(xpath, 'text')
        address['postal_code'] = address_postal

        xpath = "//span[contains(@data-test, 'addressCountry')]"
        address_country = self._scandata(xpath, 'text')
        # A simple map for ISO 3166-1 alpha-2.
        # Other countries than the US will be None.
        map_ = {'United States': 'US'}
        address['country'] = map_.get(address_country)

        xpath = "//img[contains(@class, 'nav-avatar nav-user-avatar')]"
        picture_url = self._scandata(xpath, 'src')
        fields['picture_url'] = picture_url

        fields['email'] = None
        fields['birth_date'] = None

        return fields

    def _scandata(self, xpath, fieldtype):
        """Scan data given xpath and fieldtype

            xpath: xpath pattern
            fieldtype:
                'text': return the text of the element
                other: return get attribute value of fieldtype
        """
        element = self._scanelement(xpath)
        if element is not None:
            try:
                if fieldtype == 'text':
                    return element.text.strip()
                else:
                    return element.get_attribute(fieldtype)
            except selenium.common.exceptions.StaleElementReferenceException as e:
                logger.warning('Element action not performed.')


def save(profile, filepath):
    if profile is not None:
        with open(filepath, 'w') as fp:
            json.dump(profile, fp, indent=2)
        logging.info(f'Profile saved in: "{filepath}"')
    else:
        logging.error(
            f'It could not save the profile in "{filepath}". '
            f'Please check the log errors.')
