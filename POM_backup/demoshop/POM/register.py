from demoshop.Library.library import Base


class HomePage(Base):
    register_locator = ("xpath","//a[.='Register']")

    def click_on_register(self):
        self.click_on_an_element(self.register_locator)
