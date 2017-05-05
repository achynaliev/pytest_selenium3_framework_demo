from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from utilities.util import Util
import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _sign_in_button_home = ".gmail-nav__nav-link.gmail-nav__nav-link__sign-in" #CSS
    _email_input_sign_in = "Email" #ID
    _email_input_sign_in_1 = "identifierId" # ID
    _next_after_email_input = "next" # ID
    _next_after_email_input_1 = "identifierNext" # ID
    _password_input_sign_in = "Passwd" #ID
    _password_input_sign_in_1 = "//div[@id='password']//div/input" # Xpath
    _final_sing_in = "signIn" #ID
    _next_after_password_input = "passwordNext"
    _compose_main = "COMPOSE" #LinkText
    _send_to = ":84" #ID

    def ClickSignInHome(self):
        self.elementClick(self._sign_in_button_home, locatorType="css")

    def isEmailElementIsPresent(self):
        result = self.isElementPresent(self._email_input_sign_in)
        return result

    def InputEmailSignIn(self, Email):
        self.sendKeys(Email, self._email_input_sign_in) #do not have to specify locatorType since ID is default

    def InputEmailSignIn1(self, Email):
        self.sendKeys(Email, self._email_input_sign_in_1)

    def clickNextAfterEmail(self):
        self.elementClick(self._next_after_email_input)

    def clickNextAfterEmail1(self):
        self.elementClick(self._next_after_email_input_1)

    def InputPasswordSignIn(self, password):
        self.sendKeys(password, self._password_input_sign_in)

    def SelectElementPasswordInput(self):
        self.elementClick(self._password_input_sign_in_1, locatorType="xpath")

    def InputPasswordSignIn1(self, password):
        self.sendKeys(password, self._password_input_sign_in_1, locatorType="xpath")

    def clickFinalSignIn(self):
        self.elementClick(self._final_sing_in)

    def clickNextAfterPassword(self):
        self.elementClick(self._next_after_password_input)

    def clickComposeMainButton(self):
        self.elementClick(self._compose_main, locatorType="link") #Link text

    def enterSendToEmail(self, sendtoemail):
        self.sendKeys(sendtoemail, self._send_to)

    def login_flow(self, email, password):
        self.ClickSignInHome()
        time.sleep(1)
        result1 = self.isEmailElementIsPresent()
        if result1 == True:
            self.InputEmailSignIn(email)
            self.clickNextAfterEmail()
            time.sleep(1)
            self.InputPasswordSignIn(password)
            time.sleep(1)
            self.clickFinalSignIn()
            self.util.sleep(2, "wait before TearDown")
        else:
            self.InputEmailSignIn1(email)
            self.clickNextAfterEmail1()
            time.sleep(1)
            self.SelectElementPasswordInput()
            time.sleep(1)
            self.InputPasswordSignIn1(password)
            self.clickNextAfterPassword()
            self.util.sleep(2, "wait before TearDown")
