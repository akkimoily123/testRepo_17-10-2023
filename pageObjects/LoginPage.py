from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox = "//input[@id='user-name']"
    password_textbox = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    logout_link = "//a[@id='logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_burger_menu(self):
        self.driver.find_element(By.XPATH, self.burger_menu).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link).click()
