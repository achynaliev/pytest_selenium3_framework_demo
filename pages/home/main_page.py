from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from utilities.util import Util
import time

class MainPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _compose_main = "//div[@class='aic']/div/div" #xpath
    _send_to = ":89" #ID
    _subject_email = "subjectbox" #name
    _body_email = ':8w'
    _send_email_button = ":7j"

    def clickComposeMainButton(self):
        self.elementClick(self._compose_main, locatorType="xpath") #Link text

    def clickSendToEmail(self):
        self.elementClick(self._send_to)

    def enterSendToEmail(self, sendtoemail):
        self.sendKeys(sendtoemail, self._send_to)

    def enterSubjectToEmail(self, subject):
        self.sendKeys(subject, self._subject_email, locatorType="name")

    def enterEmailBody(self, emaildata):
        self.sendKeys(emaildata, self._body_email)

    def clickSendEmailButton(self):
        self.elementClick(self._send_email_button)

    def SendAnEmail(self,sendtoemail, subject,emaildata, ):
        self.clickComposeMainButton()
        time.sleep(2)
        self.clickSendToEmail()
        time.sleep(1)
        self.enterSendToEmail(sendtoemail)
        time.sleep(1)
        self.enterSubjectToEmail(subject)
        time.sleep(1)
        self.enterEmailBody(emaildata)
        time.sleep(1)
        self.clickSendEmailButton()
        self.util.sleep(2,"wait")