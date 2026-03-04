import os
from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Pytest fixture to handle browser lifecycle at the class level
@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    """Initializes WebDriver and injects it into the test class instance."""
    # Installs the matching ChromeDriver version and sets up the service
    service = Service(ChromeDriverManager().install())

    # Launches the Chrome browser instance
    driver = webdriver.Chrome(service=service)

    # Maximizes the browser window for consistent element visibility
    driver.maximize_window()

    # Attaches the driver instance to the test class so 'self.driver' can be used
    request.cls.driver = driver

    # Separates setup logic from teardown; execution pauses here for tests to run
    yield

    # Closes all browser windows and safely terminates the driver process
    driver.quit()


# Hook to configure pytest settings before the test session starts
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Dynamic configuration for timestamped HTML reporting."""
    # Captures current system date and time
    today = datetime.now()

    # Defines the report folder path using the current date (e.g., reports/20260304)
    report_dir = Path("reports") / today.strftime("%Y%m%d")

    # Creates the folder if it doesn't exist; 'parents=True' creates mid-level folders
    report_dir.mkdir(parents=True, exist_ok=True)

    # Generates a unique filename using a timestamp (e.g., Report_20260304_1430.html)
    report_path = report_dir / f"Report_{today.strftime('%Y%m%d_%H%M')}.html"

    # Assigns the generated path to the pytest-html configuration
    if not config.option.htmlpath:
        config.option.htmlpath = str(report_path)

    # Configures the report to be a standalone file with CSS/images embedded
    config.option.self_contained_html = True


# Hook to customize the internal metadata of the HTML report
def pytest_html_report_title(report):
    """Customizes the title of the generated HTML report."""
    # Sets the text that appears in the browser tab and report header
    report.title = "HRM Test Report"