from pages.home.login_page import LoginPage
from utilities.teststatus import TStatus
from utilities.util import Util
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack #make sure to install this lib using pip3 install ddt
import unittest
import pytest
import time  #slow wi-fi at my grandma's place where I was writing this script


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TStatus(self.driver)
        self.util = Util()

    @pytest.mark.run(order=1)
    @data(*getCSVData("../framework_demo_pytest_selenium3/testdata.csv")) #uses input data from csv file
    @unpack
    def test_valid_cred(self, email, password):
        self.lp.ClickSignInHome()
        time.sleep(1)
        result1 = self.lp.isEmailElementIsPresent()
        if result1 == True:
            self.lp.InputEmailSignIn(email)
            self.lp.clickNextAfterEmail()
            time.sleep(1)
            self.lp.InputPasswordSignIn(password)
            time.sleep(1)
            self.lp.clickFinalSignIn()
            self.util.sleep(5, "wait before TearDown")
        else:
            self.lp.InputEmailSignIn1(email)
            self.lp.clickNextAfterEmail1()
            time.sleep(2)
            self.lp.SelectElementPasswordInput()
            time.sleep(1)
            self.lp.InputPasswordSignIn1(password)
            self.lp.clickNextAfterPassword()
            self.util.sleep(5, "wait before TearDown")


        # self.lp.clickComposeMainButton()
        # time.sleep(2)
        # self.lp.enterSendToEmail("tendima1199@gmail.com")
        # time.sleep(5)