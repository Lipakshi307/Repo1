from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

class Base:
    def __init__(self,driver):
        self.driver = driver
        self. actions = ActionChains(self.driver)

    def find_an_element(self,locator):
        element = self.driver.find_element(*locator)
        return element

    def click_on_an_element(self,locator):
        element = self.find_an_element(locator)
        element.click()

    def double_click_on_an_element(self,locator,value):
        element = self.find_an_element(locator,value)
        self.actions.double_click(element).perform()

    def right_click_on_an_element(self,locator):
        element = self.search_for_an_element(locator)
        self.actions.context_click(element).perform()

    def send_text_to_an_element(self,locator,value,text):
        element = self.find_an_element(locator,value)
        element.send_keys(text)

    def switch_to_another_frame(self,locator):
        element = self.search_for_an_element(locator)
        self.driver.switch_to.frame(element)







