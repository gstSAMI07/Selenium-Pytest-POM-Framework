from helper.selenium_helper import selenium_helper
from selenium.webdriver.common.by import By


class Loginpage(selenium_helper):
    """Page Object Class for the OrangeHRM Login page, inheriting from selenium_helper."""

    # Locator for the Username input field using XPATH
    email_Webelement = (By.XPATH, "//input[@placeholder='Username']")

    # Locator for the Password input field using XPATH
    password_Webelement = (By.XPATH, "//input[@placeholder='Password']")

    # Locator for the Login button using XPATH and text normalization
    login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        """Initializes the login page and passes the driver to the parent helper class."""
        # super() ensures the driver instance is available to the selenium_helper methods
        super().__init__(driver)

    def login(self, username, password):
        """Performs the complete login flow by entering credentials and clicking login."""

        # Enters the provided username into the email/username field
        self.webelement_enter(self.email_Webelement, username)

        # Enters the provided password into the password field
        self.webelement_enter(self.password_Webelement, password)

        # Clicks the login button to submit the credentials
        self.webelement_click(self.login_button)