import time
import allure
from allure_commons.types import AttachmentType

from page_objects.login_page import Login_page
from utilities.logger import Log_generator
from utilities.readconfig import Readconfig


class Test_user_login:
    email = Readconfig.get_email()
    password = Readconfig.get_password()
    log = Log_generator.log_gen()

    @allure.feature('url')
    @allure.story('Verifying the URL')
    @allure.issue('ABC-001')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('test_url_001')
    @allure.description('url testing')
    def test_url_001(self, setup):
        self.log.info("test_url_001 has started")
        self.log.info("Opening Browser and Navigating to nopcommerce")
        self.driver = setup
        self.log.info("Page Title is --> " + self.driver.title)
        page_title = self.driver.title
        time.sleep(5)
        if page_title == "Your store. Login":
            self.driver.save_screenshot("..\\screenshots\\url_testing\\test_url_001_passed.png")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_url_001_passed',
                          attachment_type=AttachmentType.PNG)
            self.log.info("Screenshot Captured Testcase test_url_001 Passed")
            assert True
        else:
            self.driver.save_screenshot("..\\screenshots\\url_testing\\test_url_001_failed.png")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_url_001_failed',
                          attachment_type=AttachmentType.PNG)
            self.log.info("Screenshot Captured Testcase test_url_001 Failed")
            assert False
        self.log.info("Testcase test_url_001 Completed")
        self.driver.quit()

    @allure.feature('login')
    @allure.story('validating the login page')
    @allure.issue('ABC-002')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('test_login_page_002')
    @allure.description('login testing')
    def test_login_page_002(self, setup):
        self.log.info("test_login_page_002 has started")
        self.log.info("Opening the Browser")
        self.driver = setup
        self.lp = Login_page(self.driver)
        self.log.info("Entering Email -->" + self.email)
        self.lp.email(self.email)
        self.log.info("Entering Password -->" + self.password)
        self.lp.password(self.password)
        self.log.info("Clicking Login Button")
        self.lp.login_btn()
        time.sleep(5)
        if self.lp.login_verification() == "Login Successful":
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_login_page_002_pass',
                          attachment_type=AttachmentType.PNG)
            self.log.info("Verification Completed Testcase test_login_page_002 Passed")
            self.log.info("Clicking Logout Button")
            self.lp.logout_btn()
            assert True
        else:
            self.lp.screenshot_fail()
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_login_page_002_failed',
                          attachment_type=AttachmentType.PNG)
            self.log.info("Screenshot Captured Testcase test_login_page_002 Failed")
            assert False
        self.log.info("Testcase test_login_page_002 Completed")
        self.driver.quit()
