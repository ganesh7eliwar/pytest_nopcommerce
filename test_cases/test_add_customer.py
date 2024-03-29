import random
import string
import allure
from allure_commons.types import AttachmentType

from page_objects.add_customer_page import Add_customer
from page_objects.login_page import Login_page
from utilities.logger import Log_generator
from utilities.readconfig import Readconfig


class Test_add_customer:
    email = Readconfig.get_email()
    password = Readconfig.get_password()
    password_1 = Readconfig.get_password_1()
    first_name = Readconfig.get_first_name()
    last_name = Readconfig.get_last_name()
    company = Readconfig.get_company()
    comment = Readconfig.get_comment()
    male = Readconfig.get_gender_male()
    female = Readconfig.get_gender_female()
    dob = Readconfig.get_date_of_birth()
    value = Readconfig.get_vendor_value()
    check = Readconfig.get_tax_box_check()
    uncheck = Readconfig.get_tax_box_uncheck()
    Check = Readconfig.get_active_box_check()
    Uncheck = Readconfig.get_active_box_uncheck()
    log = Log_generator.log_gen()

    @allure.feature('add customer')
    @allure.story('validating add customer page')
    @allure.issue('ABC-004')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('test_add_customer_004')
    @allure.description('testing_add_customer_page')
    def test_add_customer_003(self, setup):
        self.log.info("Testcase test_add_customer_003 Started")
        self.log.info("Opening the Browser")
        self.driver = setup
        self.log.info("Assigning Variable to Login_page")
        self.lp = Login_page(self.driver)
        self.log.info("Assigning Variable to Add_customer_page")
        self.ac = Add_customer(self.driver)
        self.log.info("Entering Email -->" + self.email)
        self.lp.email(self.email)
        self.log.info("Entering Password -->" + self.password)
        self.lp.password(self.password)
        self.log.info("Clicking Login Button")
        self.lp.login_btn()
        if self.lp.login_verification() == "Login Successful":
            self.log.info("Login Successful")
            self.log.info("Clicking 1st Customers Button")
            self.ac.customer_btn()
            self.log.info("Clicking 2nd Customers Button")
            self.ac.customer_btn_1()
            self.log.info("Clicking on Add Customer Button")
            self.ac.add_new_customer()
            if self.ac.add_customer_verification() == "You Are on Add New Customer Page":
                self.log.info("Landed on Add New Customer Page")
                email_1 = generate_email()
                self.log.info("Entering Customer Email -->" + email_1)
                self.ac.customer_email(email_1)
                self.log.info("Entering Password -->" + self.password_1)
                self.ac.customer_password(self.password_1)
                self.log.info("Entering First_name -->" + self.first_name)
                self.ac.first_name(self.first_name)
                self.log.info("Entering Last_name -->" + self.last_name)
                self.ac.last_name(self.last_name)
                self.log.info("Selecting Gender -->" + self.male)
                self.ac.gender(self.male)
                self.log.info("Entering Date of Birth -->" + self.dob)
                self.ac.date_of_birth(self.dob)
                self.log.info("Entering Company Name -->" + self.company)
                self.ac.company_name(self.company)
                self.log.info("Clicking on Tax Button -->" + self.uncheck)
                self.ac.tax_check_box(self.uncheck)
                self.log.info("Clicking on News Letter Button")
                self.ac.news_letter()
                self.log.info("Selecting option in News Letter")
                self.ac.click_news_letter()
                self.log.info("Clicking on Customer Roles")
                self.ac.customer_roles()
                self.log.info("Selecting Option in Customer Roles")
                self.ac.click_customer_roles()
                self.log.info("Selecting Manager of Vendor -->" + self.value)
                self.ac.dropdown_manager_of_vendor(self.value)
                self.log.info("Clicking on Active Button Check Box -->" + self.Uncheck)
                self.ac.active_button(self.Uncheck)
                self.log.info("Writing the Comment -->" + self.comment)
                self.ac.admin_comment(self.comment)
                self.log.info("Clicking on Save Button")
                self.ac.save_btn()
                if self.ac.add_customer_confirmation() == "Customer was Added Successfully":
                    self.log.info("Customer Added Successfully")
                    self.log.info("Screenshot Captured Testcase test_add_customer_003 Passed")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_add_customer_003_passed',
                                  attachment_type=AttachmentType.PNG)
                    self.ac.screenshot_pass_con()
                    self.log.info("Clicking on Logout Button")
                    self.lp.logout_btn()
                    self.log.info("Testcase test_add_customer_003 Completed")
                    assert True
                else:
                    self.log.info("Screenshot Captured Testcase test_add_customer_003 Failed")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_add_customer_003_failed',
                                  attachment_type=AttachmentType.PNG)
                    self.ac.screenshot_fail_con()
                    assert False
                assert True
            else:
                self.log.info("Screenshot Captured Testcase test_add_customer_003 Failed")
                allure.attach(self.driver.get_screenshot_as_png(),
                              name='test_add_customer_003_on_customer_verification_level',
                              attachment_type=AttachmentType.PNG)
                self.ac.screenshot_fail()
                assert False
            assert True
        else:
            self.log.info("Screenshot Captured login Testcase test_add_customer_003 Failed")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_add_customer_003_on_login_level',
                          attachment_type=AttachmentType.PNG)
            self.lp.screenshot_fail()
            assert False


def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=7))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"
