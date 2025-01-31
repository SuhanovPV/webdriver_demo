import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import TypeVar
from typing import Union
from typing import Callable
from typing import Literal
from selenium.common.exceptions import TimeoutException

D = TypeVar("D", bound=Union[WebDriver, WebElement])
T = TypeVar("T")


class Wait(WebDriverWait):
    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        screen = None
        stacktrace = None
        reason = None

        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
                reason = getattr(exc, "msg", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
        raise TimeoutException(message + f'\n\nReason:\n\t{reason}\n', screen, stacktrace)
