#!/usr/bin/env python3
"""The main module to run the application. Run it using: python main.py

Python version required: 3.9
We use Selenium to open and log in to Upwork, scan the profile data,
and save it in two files:
"JSON_BASIC_PROFILE_FILE_PATH" and "JSON_FULL_PROFILE_FILE_PATH".
"""
import logging

import pydantic

from const import (
    LOGGING_FORMAT,
    LOGGING_LEVEL,
    JSON_BASIC_PROFILE_FILE_PATH,
    JSON_FULL_PROFILE_FILE_PATH,
    SLEEP_TIME,
    TITLE_CONTACT_INFO,
    TITLE_MY_JOB_FEED,
    TRIES,
    URL_CONTACT_INFO,
    URL_FIND_WORK,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
import profilemodel
import sync_browse as browse
import sync_scan as scan

logging.basicConfig(format=LOGGING_FORMAT, level=LOGGING_LEVEL)


def main():
    logging.info('Starting to scan...')
    for i in range(TRIES):
        if run():
            break
        else:
            logging.warning(f'Try {i+1}/{TRIES} to save profiles failed.')
    else:
        logging.error(
            f'It could not save profiles. Check the logs for possible errors.')


def run():
    basicprofile_scan_classes = [scan.MainProfile, scan.ExtraProfile]
    fullprofile_scan_classes = [scan.ContactInfo]

    # Browser driver to scan data.
    driver = browse.login()
    if driver is not None:
        browse.try_auth(driver, SLEEP_TIME, TRIES)
        # Increase window size to get more data from the page.
        driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Run two different sets of scanners to save two different profiles.
        execution1 = run_scanners(
            driver, basicprofile_scan_classes, profilemodel.BasicProfile,
            JSON_BASIC_PROFILE_FILE_PATH, TITLE_MY_JOB_FEED, URL_FIND_WORK)
        execution2 = run_scanners(
            driver, fullprofile_scan_classes, profilemodel.Profile,
            JSON_FULL_PROFILE_FILE_PATH, TITLE_CONTACT_INFO, URL_CONTACT_INFO)

        driver.close()
        # Both executions need to perform well.
        return execution1 and execution2


def run_scanners(driver, classes, profile_model, filepath, title, url):
    profiledata = {}
    for ScannerClass in classes:
        scanner = ScannerClass(browse, driver, SLEEP_TIME, title, TRIES, url)
        profiledata |= scanner() or {}  # Empty dict to not throw an exception.

    try:
        logging.info(f'Profile: {profiledata}')
        logging.info(f'Profile serialized to object: {profile_model(**profiledata)}')
        scan.save(profiledata, filepath)
        return True
    except pydantic.error_wrappers.ValidationError as e:
        logging.error('No profile data saved.')
        logging.error(e)
        return False


if __name__ == '__main__':
    main()
