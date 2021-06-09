from Car import Car
import pytest
# Import the 'modules' that are required for execution for Selenium test automation
import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys

# from seleniumbase import BaseCase


@pytest.fixture(scope='class')
def init_car(request):
    car_obj = Car(100)
    request.cls.obj = car_obj
    yield
    del car_obj


@pytest.mark.usefixtures("init_car")
class Cars:
    pass


class Test_Benz(Cars):
    def test_car(self):
        car = self.obj
        car.accelerate()
        assert car.speed == 105

class Test_Ford(Cars):
    def test_car(self):
        car = self.obj
        car.accelerate()
        car.accelerate()

        assert car.speed == 110


@pytest.mark.usefixtures("init_car")
class Test_Tesla():
    def test_car(self):
        car = self.obj
        car.accelerate()
        car.accelerate()

        assert car.speed == 110



#@pytest.fixture(scope="module")


# @pytest.fixture(scope="module",  params=[100,  200, 300])
# @pytest.fixture(scope="session",  params=[100,  200, 300])
# def car(request):
#     print(f'\ncalling setup fixture')
#     print(f'{request.param}')
#     car = Car(request.param)
#     yield car
#     car = None
#     print(f'\ncalling terminate fixture')
#
#
#
# @pytest.mark.feature
# @pytest.mark.parametrize("speed", [100,  200, 300])
# def test_car_brake(car, speed):
#     # car = Car(50)
#     car.speed = speed
#     car.brake()
#     assert car.speed == speed-5
#
#
# @pytest.mark.regression
# @pytest.mark.feature
# @pytest.mark.parametrize("speed",[100,  200, 300])
# def test_car_acc(car, speed):
#     # car = Car(50)
#     car.speed = speed
#     car.accelerate()
#     print(":executing test_car_acc")
#     assert car.speed == speed+5



# class MyTestClass(BaseCase):
#
#     def test_basics(self):
#         url = "https://store.xkcd.com/collections/posters"
#         self.open(url)
#         self.type('input[name="q"]', "xkcd book")
#         self.click('input[value="Search"]')
#         self.assert_text("xkcd: volume 0", "h3")
#         self.open("https://xkcd.com/353/")
#         self.assert_title("xkcd: Python")
#         self.assert_element('img[alt="Python"]')
#         self.click('a[rel="license"]')
#         self.assert_text("free to copy and reuse")
#         self.go_back()
#         self.click_link("About")
#         self.assert_exact_text("xkcd.com", "h2")
#
# # Fixture for Firefox
# @pytest.fixture(scope="class")
# def driver_init(request):
#     ff_driver = webdriver.Firefox()
#     request.cls.driver = ff_driver
#     yield
#     ff_driver.close()
#
#
# # Fixture for Chrome
# @pytest.fixture(scope="class")
# def chrome_driver_init(request):
#     chrome_driver = webdriver.Chrome()
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()
#
#
# @pytest.mark.usefixtures("driver_init")
# class BasicTest:
#     pass
#
#
# class Test_URL(BasicTest):
#     def test_open_url(self):
#         self.driver.get('https://www.google.com/')
#         self.driver.maximize_window()
#         title = "Google"
#         assert title == self.driver.title
#
#         search_text = "LambdaTest"
#         search_box = self.driver.find_element_by_xpath("//input[@name='q']")
#         search_box.send_keys(search_text)
#
#         time.sleep(5)
#
#         # Option 1 - To Submit the search
#         # search_box.submit()
#
#         # Option 2 - To Submit the search
#         search_box.send_keys(Keys.ARROW_DOWN)
#         search_box.send_keys(Keys.ARROW_UP)
#         time.sleep(2)
#         search_box.send_keys(Keys.RETURN)
#
#         time.sleep(5)
#
#         # Click on the LambdaTest HomePage Link
#         title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
#         lt_link = self.driver.find_element_by_xpath(
#             "//h3[.='LambdaTest: Cross Browser Testing Tools | Free Automated ...']")
#         lt_link.click()
#
#         time.sleep(10)
#         assert title == self.driver.title
#         time.sleep(2)
#
#
# @pytest.mark.usefixtures("chrome_driver_init")
# class Basic_Chrome_Test:
#     pass
#
#
# class Test_URL_Chrome(Basic_Chrome_Test):
#     def test_open_url(self):
#         self.driver.get('https://lambdatest.github.io/sample-todo-app/')
#         self.driver.maximize_window()
#
#         self.driver.find_element_by_name("li1").click()
#         self.driver.find_element_by_name("li2").click()
#
#         title = "Sample page - lambdatest.com"
#         assert title == self.driver.title
#
#         sample_text = "Happy Testing at LambdaTest"
#         email_text_field = self.driver.find_element_by_id("sampletodotext")
#         email_text_field.send_keys(sample_text)
#         time.sleep(5)
#
#         self.driver.find_element_by_id("addbutton").click()
#         time.sleep(5)
#
#         output_str = self.driver.find_element_by_name("li6").text
#         sys.stderr.write(output_str)
#
#         time.sleep(2)
#
#
#
#
#
#
#
#
#
