"""Constants for the application"""
import logging

JSON_BASIC_PROFILE_FILE_PATH = 'profile_basic.json'
JSON_FULL_PROFILE_FILE_PATH = 'profile_full.json'

LOGGING_FORMAT = '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(message)s'
LOGGING_LEVEL = logging.INFO

SLEEP_TIME = 1

TRIES = 10  # Number of tries to get data from the pages.

URL_CONTACT_INFO = 'https://www.upwork.com/freelancers/settings/contactInfo'
# Starting page to log in and to scan data.
URL_LOG_IN = 'https://www.upwork.com/ab/account-security/login'
URL_FIND_WORK = 'https://www.upwork.com/ab/find-work/domestic'

# Size of the window to get more data from the pages.
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 900

TITLE_CAPTCHA = 'Access to this page has been denied.'
TITLE_CONTACT_INFO = 'Contact info'
TITLE_DEVICE_AUTHORIZATION = 'Device authorization'
TITLE_MY_JOB_FEED = 'My Job Feed'
TITLE_RE_ENTER_PASSWORD = 'Re-enter password'
TITLE_HOME = 'In-demand talent on demand'
