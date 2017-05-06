from pages.home.login_page import LoginPage
from pages.home.main_page import MainPage
from utilities.teststatus import TStatus
from utilities.util import Util
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack #make sure to install this lib using pip3 install ddt
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class MainTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.mainp = MainPage(self.driver)
        self.ts = TStatus(self.driver)
        self.util = Util()

    @pytest.mark.run(order=1)
#    @data(*getCSVData("../framework_demo_pytest_selenium3/testdata.csv")) #uses input data from csv file
#    @unpack
    def test_sending_email(self):
        self.mainp.SendAnEmail("ataitesting1@gmail.com", "This is test email", "this is an testing email")