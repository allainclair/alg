#!/usr/bin/env python
import random
import sys
from collections import namedtuple
from pprint import pprint

import yagmail

Contact = namedtuple('Contact', ['name', 'email'])

GMAIL = 'allainclair@gmail.com'
PASSWD = 'hpsxaezctlakdccy'
yag = yagmail.SMTP(GMAIL, PASSWD)


def secretfriend(friends):
    if len(friends) < 2:
        return None

    shuffled = random.sample(list(friends), k=len(friends))
    result = {
        (friend1, friend2)
        for friend1, friend2 in zip(shuffled[:-1], shuffled[1:])}
    return result | {(shuffled[-1], shuffled[0])}


def build_contacts():
    allain = Contact(
        'Allain',
        'allainclair@gmail.com',)
    amanda = Contact(
        'Amanda',
        'invalid_amanda@gmail.com', )
    ana = Contact(
        'Ana',
        'invalid_ana@gmail.com',)
    clara = Contact(
        'Clara',
        'invalid_clara@gmail.com',)
    hugo = Contact(
        'Hugo',
        'invalid_hugo@gmail.com',)
    janderson = Contact(
        'Janderson',
        'invalidjands@gmail.com',)
    luciano = Contact(
        'Luciano',
        'invalid_luciano@gmail.com',)
    marcel = Contact(
        'Marcel',
        'invalidmarcel@gmail.com',)
    nagela = Contact(
        'Nagela',
        'invalid_nagela@gmail.com',)
    rafaela = Contact(
        'Rafaela',
        'invalid_rafaela@gmail.com',)
    raiza = Contact(
        'Raiza',
        'invalid_raiza@gmail.com',)
    thaty = Contact(
        'Thaty',
        'invalid_thaty@gmail.com',)
    # return {allain, amanda, ana}
    return {allain, amanda, ana, clara, hugo, janderson, luciano, marcel, nagela, rafaela, raiza, thaty}


def build_definite_message(friend_from, friend_to):
    bgcolor = '#FFD8D8'
    padding = '5px'
    return f'<b>{friend_from}</b>, seu(ua) amigo(a) secreto(a) é:\n<h2 style="background-color:{bgcolor};display:inline-flex;padding:{padding};">{friend_to}<h2>'


def build_test_message(friend_from, friend_to):
    header = '<b>## Mensagem de TESTE para amigo secreto ##</b>\n'
    message = build_definite_message(friend_from, friend_to)
    return header + message


def send_definitive_message(to_email, message):
    print(f'Sending email to {to_email}...')
    subject = 'Amigo Secreto do dia 11/12/2021'
    yag.send(
        to=to_email,
        subject=subject,
        contents=message,
    )


def send_test_message(to_email, message):
    print(f'Sending TESTING email to {to_email}...')
    subject = 'MENSAGEM DE TESTE - Amigo Secreto do dia 11/12/2021'
    yag.send(
        to=to_email,
        subject=subject,
        contents=message,
    )


def main():
    test_mode = False
    if len(sys.argv) > 1:
        print('TEST MODE\n')
        test_mode = True

    contacts = build_contacts()
    secrets = secretfriend(contacts)
    print('Tuplas dos amigos secretos')
    pprint(secrets)
    print()
    for friend1, friend2 in secrets:
        print(f'{friend1.name} -> {friend2.name}')
        if test_mode:
            message = build_test_message(friend1.name, friend2.name)
            send_test_message(friend1.email, message)
        else:
            message = build_definite_message(friend1.name, friend2.name)
            send_definitive_message(friend1.email, message)
        print(message)
        print()


if __name__ == '__main__':
    main()
