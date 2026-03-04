import pytest
from pages.Loginpage import Loginpage


# Apply the 'browser_setup' fixture to manage the browser lifecycle for this class
@pytest.mark.usefixtures("browser_setup")
class TestLogin:
    """Test suite for OrangeHRM Login functionality."""

    # Define test environment URL and login credentials
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_valid_login(self):
        """Test case to verify successful login with valid credentials."""

        # Navigate to the target application URL
        self.driver.get(self.url)

        # Initialize the Login Page Object with the current driver instance
        lp = Loginpage(self.driver)

        # Perform the login action using the provided username and password
        lp.login(self.username, self.password)

    # Manual teardown is disabled; 'driver.quit()' is managed by the conftest fixture
    # def tear_down(self):
    #     self.driver.quit()