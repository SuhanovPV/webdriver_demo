from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_demo.commands import elements


def number_of_elements(selector, value: int):
    def condition(driver: WebDriver):
        webelements = elements(selector)
        actual_value = len(webelements)
        if actual_value != value:
            raise AssertionError(f'number of elements is not {value}\nactual value {actual_value}')
        return webelements

    return condition
