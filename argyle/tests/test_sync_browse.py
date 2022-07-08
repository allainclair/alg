import selenium

import selenium

import sync_browse

NAME_TO_FIND = 'name_to_find'
NAME_TO_NOT_FIND = 'name_to_not_find'


class MockDriver():
    def find_element_by_name(self, name):
        if name == NAME_TO_FIND:
            return 'Any element'
        else:
            raise selenium.common.exceptions.NoSuchElementException('Any message.')

    def find_element_by_xpath(self, xpath):
        if xpath == NAME_TO_FIND:
            return 'Any element'
        else:
            raise selenium.common.exceptions.NoSuchElementException('Any message.')


def test__try_element():
    driver = MockDriver()
    assert sync_browse._try_element_by_name(driver, NAME_TO_FIND)
    # When NoSuchElementException happens, it returns None.
    assert sync_browse._try_element_by_name(driver, NAME_TO_NOT_FIND) is None

    assert sync_browse._try_element_by_xpath(driver, NAME_TO_FIND)
    # When NoSuchElementException happens, it returns None.
    assert sync_browse._try_element_by_xpath(driver, NAME_TO_NOT_FIND) is None
