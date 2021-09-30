import os

import allure
import pytest
from pages.log_in_page import LogInPage
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    global driver
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(15)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def log_in_admin(setup):
    driver.get("https://agrii-tms.x-one.dev/login")
    log_in_page = LogInPage(driver)
    log_in_page.set_login("skowalska@x-one.com.pl")
    log_in_page.set_password("123456789")
    log_in_page.perform_log_in()


def pytest_deselected(items):
    if not items:
        return
    config = items[0].session.config
    reporter = config.pluginmanager.getplugin("terminalreporter")
    reporter.ensure_newline()
    for item in items:
        reporter.line(f"deselected: {item.nodeid}", yellow=True, bold=True)
