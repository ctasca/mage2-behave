import time
import operator
from selenium.common import (StaleElementReferenceException, JavascriptException, ElementClickInterceptedException,
                             ElementNotInteractableException)
from splinter.exceptions import ElementDoesNotExist

DEFAULT_SPINNER_WAIT_TIME = 60
DEFAULT_SLEEP_TIME = 1


class Spinner:
    def __init__(self, spin_function, activity_wait_time=DEFAULT_SPINNER_WAIT_TIME, sleep_time=DEFAULT_SLEEP_TIME):
        self.spin_function = spin_function
        self.activity_wait_time = activity_wait_time
        self.sleep_time = sleep_time

    def spin(self):
        for _ in range(self.activity_wait_time):
            try:
                self.spin_function()
                break
            except (StaleElementReferenceException, ElementDoesNotExist, JavascriptException,
                    ElementClickInterceptedException, ElementNotInteractableException, AttributeError, IndexError):
                time.sleep(self.sleep_time)


class ChainSpinner:
    def __init__(self, spin_functions: list, activity_wait_time=DEFAULT_SPINNER_WAIT_TIME,
                 sleep_time=DEFAULT_SLEEP_TIME):
        self.spin_functions = spin_functions
        self.activity_wait_time = activity_wait_time
        self.sleep_time = sleep_time

    def spin(self):
        for _ in range(self.activity_wait_time):
            try:
                for spin_function in self.spin_functions:
                    spin_function()
                break
            except (StaleElementReferenceException, ElementDoesNotExist, JavascriptException,
                    ElementClickInterceptedException, ElementNotInteractableException, AttributeError, IndexError):
                time.sleep(self.sleep_time)


class EvalSpinner:
    def __init__(self, spin_function, use_operator, eval_to, activity_wait_time=DEFAULT_SPINNER_WAIT_TIME,
                 sleep_time=DEFAULT_SLEEP_TIME):
        self.spin_function = spin_function
        self.activity_wait_time = activity_wait_time
        self.sleep_time = sleep_time
        self.use_operator = use_operator
        self.eval_to = eval_to
        self.operator_map = {
            "==": operator.eq,
            "!=": operator.ne
        }

    def spin(self):
        for _ in range(self.activity_wait_time):
            try:
                if self.operator_map[self.use_operator](self.spin_function(), self.eval_to):
                    break
                else:
                    raise IndexError
            except (StaleElementReferenceException, ElementDoesNotExist, JavascriptException,
                    ElementClickInterceptedException, ElementNotInteractableException, AttributeError, IndexError):
                time.sleep(self.sleep_time)
