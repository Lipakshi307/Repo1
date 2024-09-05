import pytest
import openpyxl
from demoshop.POM.homepage import HomePage
from demoshop.POM.loginpage import LogIn

# usernames = [("reddyvinuth27@gmail.com", "selenium"), ("abc@gmail.com", "1234"), ("xyaz@yahoo.com", "5235"),
#              ("mno@hotmail.com", "5251")]

creds = openpyxl.load_workbook("creds.xlsx")
login_creds = creds["login_creds"]

credentials = []
for row in range(1, 6):
    nested_creds = []
    for column in range(1, 3):
        data = login_creds.cell(row,column)
        nested_creds.append(data.value)

    credentials.append(nested_creds)


@pytest.mark.parametrize("username,password", credentials)
def test_login_with_proper_credentials(driver, username, password):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username, password)
    assert driver.find_element("xpath", f"//a[.='{username}']").is_displayed()


@pytest.mark.skip
def test_login_with_no_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("reddyvinuth27@gmail.com", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


@pytest.mark.skip
def test_login_with_no_username(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "selenium")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


@pytest.mark.skip
def test_login_with_no_credntials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


@pytest.mark.skip
def test_login_with_invalid_credntials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("abc@gmail.com", "wastejava")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
