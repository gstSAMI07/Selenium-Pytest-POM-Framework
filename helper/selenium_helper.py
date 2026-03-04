from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class selenium_helper:
    """A wrapper class to simplify common Selenium interactions and explicit waits."""

    # Constructor method to initialize the helper with the WebDriver instance
    def __init__(self, driver):
        # Stores the driver instance to be used by methods within this class
        self.driver = driver

    # Method to wait for an input field and enter text
    def webelement_enter(self, locator, text):
        """Waits up to 10 seconds for an element to be visible, then enters text."""
        # WebDriverWait searches for the element; until() ensures it is visible before interacting
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Method to wait for a clickable element and perform a click
    def webelement_click(self, locator):
        """Waits up to 10 seconds for an element to be clickable, then performs a click."""
        # element_to_be_clickable ensures the element is visible AND enabled for interaction
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()