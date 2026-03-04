import pytest
from pages.Loginpage import Loginpage


# Use the browser_setup fixture defined in conftest.py for this class
@pytest.mark.usefixtures("browser_setup")
class TestLogin:
    """Test suite for OrangeHRM Login functionality."""

    # Static test data for environment URL and user credentials
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_valid_login(self):
        """Verifies that a user can log in with valid credentials."""

        # Navigates the browser to the application login page
        self.driver.get(self.url)

        # Creates an instance of the Loginpage Object and passes the driver
        lp = Loginpage(self.driver)

        # Executes the login action using credentials defined above
        lp.login(self.username, self.password)

    # Note: No manual tear_down is needed here as 'driver.quit()'
    # is automatically handled by the 'browser_setup' fixture.