import allure
import pytest
from allure_common.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from demoshop.POM.register import HomePage


# def attach_screenshot():
#     allure_attach(driver.get_screenshot_as_png(), name="test_check_for_login", attachment_type=AttachmentType.PNG)

@pytest.fixture()
def driver():
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()


# def test_clicking_on_login_button(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     assert driver.find_element("id", "register-button").is_displayed()




def test_check_for_login(driver):
    home_page_obj = HomePage(driver)
    home_page_obj.click_on_login()
    condition = False:
    if condition == False:
        attach_screenshot(driver.get_screenshot_as_png(), name="test_check_for_login.png", attachment_type=AttachmentType.PNG)
    assert condition

def test_check_for_register(driver):
    home_page_obj = HomePage(driver)
    home_page_obj.click_on_register()
    condition = True
    if condition == False:
        allure.attach(driver.get_screenshot_as_png(), name="test_check_for_login.png", attachment_type=AttachmentType.PNG)
    assert condition