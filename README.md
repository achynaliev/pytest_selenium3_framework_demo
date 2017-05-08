# pytest_selenium3_framework_demo
# To Be able to run this code you need to have pytest, Gecko driver for firefox, ddt.
# to install pytest(for python3), open terminal and enter:sudo pip install pytest
# to install ddt open terminal and enter:sudo pip3 install ddt
# for gecko driver download it from firefox website and put path to driver in your bash profile
# to run the code open terminal go the right derictory(or just put the right path to the file) and enter:pytest -v -s login_test.py --browser firefox
# to run test on chrome you need to have download chrome driver and put the path to the driver in webdriverfactory.py line 52
# run test on chrome :pytest -v -s login_test.py --browser chrome