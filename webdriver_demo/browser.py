from typing import List

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from webdriver_demo.custom_wait import Wait
from selenium.webdriver.remote.webdriver import WebDriver

from webdriver_demo.selector import to_locator

driver: WebDriver = ...
wait: Wait = ...


def assert_(condition):
    return wait.until(condition)


def open(url):
    driver.get(url)

def back():
    driver.back()

def quit():
    driver.quit()


def element(selector) -> WebElement:
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        if not webelement.is_displayed():
            raise AssertionError(f'element is not displayed: {webelement.get_attribute("outerHTML")}')
        return webelement

    return wait.until(command, message=f'failed to find element by {selector}')


def elements(selector) -> List[WebElement]:
    def command(driver: WebDriver):
        webelements = driver.find_elements(*to_locator(selector))
        return webelements

    return wait.until(command, message=f'failed to find elements by {selector}')


def click_on(selector):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    wait.until(command, message=f'failed to click on element by {selector}')


def type_to(selector, value):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        is_element_covered = driver.execute_script(
            '''
                    element=arguments[0];
                    rectangle = element.getBoundingClientRect();
                    let x = rectangle.x + Math.floor(rectangle.width/2);
                    let y = rectangle.y + Math.floor(rectangle.height/2);
                    return !element.isSameNode(document.elementFromPoint(x,y));
                    ''',
            webelement)

        if is_element_covered:
            raise TimeoutException

        webelement.send_keys(value)
        return webelement

    wait.until(command, message=f'failed to type {value} in to element by {selector}')
