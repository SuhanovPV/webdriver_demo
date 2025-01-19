from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible


def to_locator(selector: str) -> Tuple[str, str]:
    return (By.XPATH, selector) if (
            selector.startswith('/') or
            selector.startswith('//') or
            selector.startswith('./') or
            selector.startswith('..') or
            selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)


def element(selector):
    def command(driver):
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    return command


def click_on_element(selector):
    selector_type = By.XPATH if (
            selector.startswith('/') or
            selector.startswith('//') or
            selector.startswith('./') or
            selector.startswith('..') or
            selector.startswith('(')
    ) else By.CSS_SELECTOR

    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    return command


def type_to_element(selector, value):
    selector_type = By.XPATH if (
            selector.startswith('/') or
            selector.startswith('//') or
            selector.startswith('./') or
            selector.startswith('..') or
            selector.startswith('(')
    ) else By.CSS_SELECTOR

    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        is_element_covered = driver.execute_script('element=arguments[1]; return element;', webelement, 2)
        webelement.send_keys(value)
        return webelement

    return command


def number_of_elements(selector, value: int):
    selector_type = By.XPATH if (
            selector.startswith('/') or
            selector.startswith('//') or
            selector.startswith('./') or
            selector.startswith('..') or
            selector.startswith('(')
    ) else By.CSS_SELECTOR

    def predicate(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return len(webelements) == value

    return predicate
