from pages.home.login_page import LoginPage
from utilities.teststatus import TStatus
from utilities.util import Util
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack #make sure to install this lib using pip3 install ddt
import unittest
import pytest
import time


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
    def test_login(self, email, password):
        self.lp.login_flow(email, password)
