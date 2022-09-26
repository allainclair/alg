import logging
import os
import time

import dotenv
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from const import (
    SLEEP_TIME,
    TITLE_DEVICE_AUTHORIZATION,
    TITLE_RE_ENTER_PASSWORD,
    TRIES,
    URL_LOG_IN,
)

dotenv.load_dotenv()  # Default path to get env variables: '.env'
logger = logging.getLogger(__name__)

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SECRET_ANSWER = os.getenv('SECRET_ANSWER')


def login(
        loginurl=URL_LOG_IN, username=USERNAME, password=PASSWORD,
        webdriver_=webdriver.Safari):
    driver = webdriver_()
    logger.info(f'Log in: {loginurl}')
    driver.get(loginurl)

    username_field = try_element_by_name(driver, 'login[username]')
    if username_field:
        username_field.clear()
        username_field.send_keys(username)
        username_field.send_keys(Keys.RETURN)
        logger.info('Username sent.')

        time.sleep(3)  # Wait for the password field to appear.

        password_field = driver.find_element_by_id('login_password')
        password_field.clear()
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        logger.info('Log in submitted.')

        title_change(driver)

        return driver
    else:
        driver.close()
        return None


def title_change(driver, sleep_time=SLEEP_TIME, tries=TRIES):
    start_title = driver.title
    for i in range(tries):
        if start_title != driver.title:
            logging.info(f'Page title changed: "{start_title}" -> "{driver.title}".')
            return driver.title
        logging.info(
            f'Waiting page title "{driver.title}" to change. Try: {i + 1}/{tries}')
        time.sleep(sleep_time)


def try_auth(driver, sleep_time, tries):
    title = _try_device_auth(driver, sleep_time, tries)
    if title:
        return title
    elif driver.title == TITLE_RE_ENTER_PASSWORD:
        # TODO: Sometimes we need to add the password again.
        pass


def _get_secretkey_field(driver):
    field = try_element_by_name(driver, 'deviceAuth[answer]')
    if not field:
        field = try_element_by_name(
            driver, 'login[deviceAuthorization][answer]')
    return field


def try_element_by_class_name(driver, name):
    return _try_element(driver, 'find_element_by_class_name', name)


def try_element_by_name(driver, name):
    return _try_element(driver, 'find_element_by_name', name)


def try_element_by_xpath(driver, xpath):
    return _try_element(driver, 'find_element_by_xpath', xpath)


def _try_element(driver, method_name, arg):
    try:
        return getattr(driver, method_name)(arg)
    except selenium.common.exceptions.NoSuchElementException:
        logger.info(f'Argument "{arg}" for the method "{method_name}" not found.')


def _try_device_auth(driver, sleep_time, tries):
    element = try_element_by_xpath(
        driver, "//label[contains(@for, 'login_deviceAuthorization_answer')]")

    if driver.title == TITLE_DEVICE_AUTHORIZATION or element:
        logger.info('Device authorization issue.')

        field = _get_secretkey_field(driver)

        field.clear()
        field.send_keys(SECRET_ANSWER)
        field.send_keys(Keys.RETURN)
        logger.info('Secret answer sent.')
        return title_change(driver, sleep_time, tries)
    elif driver.title == TITLE_RE_ENTER_PASSWORD:
        # TODO we need to input password again sometimes.
        pass
