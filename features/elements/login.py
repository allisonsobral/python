from selenium.webdriver.common.by import By
from features.core.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.emailField = (By.XPATH, '//*[@id="email"]')
        self.passwordField = (By.XPATH, '//*[@id="pass"]')
        self.loginButton = (By.CSS_SELECTOR, '[data-testid="royal_login_button"]')

    def insertEmail(self, email):
        self.sendKeysToElement(self.emailField, email)

    def insertPassword(self, password):
        self.sendKeysToElement(self.passwordField, password)

    def clickLogin(self):
        self.driver.find_element(*self.loginButton).click()

    def getLoginButtonText(self):
        return self.get_text_from_element(self.driver.find_element(*self.loginButton))

    def waitLoginButtonToBeDisplayed(self):
        self.waitElementToBeDisplayed(self.loginButton)


