from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_homepageTitle(self, setup):
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Swag Labs123":
            assert True, f"{actual_title} is correct"
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False, f"{actual_title} is incorrect"

    def test_login(self, setup):
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login_button()
        actual_title = self.driver.title
        if actual_title == "Swag Labs123":
            assert True, f"{actual_title} is correct"
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False, f"{actual_title} is incorrect"
