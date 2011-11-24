
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


BROWSER_CAPABILITIES = {
    'version' : '5',
    'platform' : 'XP',
    'name' : 'Testing Selenium 2'
}

SAUCELABS_EXECUTOR = "http://rotoudjimaye:02cefab9-c500-4f05-a761-00fc441f3187@ondemand.saucelabs.com:80/wd/hub"
BASE_URL = "https://csr-theo.rhcloud.com"

class TestSeleniumWebDriver(unittest.TestCase):
    def setUp(self):
        capabilities = webdriver.DesiredCapabilities.FIREFOX
        capabilities['version'] = '6'
        capabilities['platform'] = 'XP'
        capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'
        # capabilities.update(BROWSER_CAPABILITIES)
        self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=SAUCELABS_EXECUTOR)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
    
    def getUrl(self, url):
        return "".join([BASE_URL, str(url)])

    def testLogin(self):
        driver = self.driver
        driver.get(self.getUrl("/accounts/login/"))
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("abc")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("ysvf")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class TestRemote(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_remote(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=secure page")
        sel.wait_for_page_to_load("30000")
        sel.type("name=username", "abc")
        sel.type("name=password", "ysvf")
        sel.click("css=input[type=\"submit\"]")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSeleniumWebDriver)

if __name__ == "__main__":
    unittest.main()

