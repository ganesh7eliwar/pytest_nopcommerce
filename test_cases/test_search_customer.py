import string
import random

import allure
from allure_commons.types import AttachmentType

from page_objects.add_customer_page import Add_customer
from page_objects.login_page import Login_page
from page_objects.search_customer_page import Search_customer
from utilities.logger import Log_generator
from utilities.readconfig import Readconfig


class Test_search_customer:
    month = Readconfig.get_month()
    day = Readconfig.get_day()
    date_from = Readconfig.get_date_from()
    date_to = Readconfig.get_date_to()
    from_date = Readconfig.get_from_date()
    to_date = Readconfig.get_to_date()
    company_name = Readconfig.get_company()
    ip_address = Readconfig.get_ip_address()
    first_name = Readconfig.get_first_name()
    last_name = Readconfig.get_last_name()
    email = Readconfig.get_email()
    password = Readconfig.get_password()
    password_1 = Readconfig.get_password_1()
    male = Readconfig.get_gender_male()
    female = Readconfig.get_gender_female()
    dob = Readconfig.get_date_of_birth()
    value = Readconfig.get_vendor_value()
    check = Readconfig.get_tax_box_check()
    uncheck = Readconfig.get_tax_box_uncheck()
    Check = Readconfig.get_active_box_check()
    Uncheck = Readconfig.get_active_box_uncheck()
    company = Readconfig.get_company()
    comment = Readconfig.get_comment()
    log = Log_generator.log_gen()

    @allure.feature('search customer')
    @allure.story('validating search customer page')
    @allure.issue('ABC-003')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('test_search_customer_004')
    @allure.description('testing_search_customer_page')
    def test_search_customer_004(self, setup):
        self.log.info("Testcase test_search_customer_004 Started")
        self.log.info("Opening the Browser")
        self.driver = setup
        self.log.info("Assigning Variable to Login Page")
        self.lp = Login_page(self.driver)
        self.log.info("Assigning Variable to Search Customer")
        self.sc = Search_customer(self.driver)
        self.log.info("Assigning Variable to Add Customer")
        self.ac = Add_customer(self.driver)
        self.log.info("Entering Email -->" + self.email)
        self.lp.email(self.email)
        self.log.info("Entering Password -->" + self.password)
        self.lp.password(self.password)
        self.log.info("Clicking on Login Button")
        self.lp.login_btn()
        if self.lp.login_verification() == "Login Successful":
            self.log.info("Login Successful")
            self.log.info("Clicking 1st Customer Button")
            self.ac.customer_btn()
            self.log.info("Clicking 2st Customer Button")
            self.ac.customer_btn_1()
            self.log.info("Clicking on Add New Customer Button")
            self.ac.add_new_customer()
            if self.ac.add_customer_verification() == "You Are on Add New Customer Page":
                self.log.info("Landed on Add New Customer Page")
                self.log.info("Creating Variable for generate_email()")
                email_1 = generate_email()
                self.log.info("Entering Customer Email -->" + email_1)
                self.ac.customer_email(email_1)
                self.log.info("Entering Customer Password -->" + self.password_1)
                self.ac.customer_password(self.password_1)
                self.log.info("Entering Customer First Name -->" + self.first_name)
                self.ac.first_name(self.first_name)
                self.log.info("Entering Customer Last Name -->" + self.last_name)
                self.ac.last_name(self.last_name)
                self.log.info("Selecting Gender -->" + self.male)
                self.ac.gender(self.male)
                self.log.info("Entering Customer DOB -->" + self.dob)
                self.ac.date_of_birth(self.dob)
                self.log.info("Entering Company Name -->" + self.company)
                self.ac.company_name(self.company)
                self.log.info("Clicking on Tax Check Box -->" + self.uncheck)
                self.ac.tax_check_box(self.uncheck)
                self.log.info("Clicking on New Letter")
                self.ac.news_letter()
                self.log.info("Selecting News Letter")
                self.ac.click_news_letter()
                self.log.info("Clicking on Customer Roles")
                self.ac.customer_roles()
                self.log.info("Selecting Customer Roles")
                self.ac.click_customer_roles()
                self.log.info("Clicking on Manager of Vendor Dropdown Button and Selecting Value -->" + self.value)
                self.ac.dropdown_manager_of_vendor(self.value)
                self.log.info("Clicking on Active Button Check Box -->" + self.Uncheck)
                self.ac.active_button(self.Uncheck)
                self.log.info("Clicking on Comment Box -->" + self.comment)
                self.ac.admin_comment(self.comment)
                self.log.info("Clicking on Save Button")
                self.ac.save_btn()
                if self.ac.add_customer_confirmation() == "Customer was Added Successfully":
                    self.log.info("Customer Added Successfully")
                    self.log.info("Entering Customer Email -->" + email_1)
                    self.sc.customer_email(email_1)
                    self.log.info("Clicking on Search Button")
                    self.sc.search_btn()
                    self.log.info("Clicking on Edit Button")
                    self.sc.edit_btn()
                    if self.sc.search_customer_validation() == "You are on the Edit Customer Page":
                        self.log.info("Landed on Edit Customer Page")
                        self.log.info("Capturing Screenshot Testcase 'test_search_customer_004_passed'")
                        allure.attach(self.driver.get_screenshot_as_png(),
                                      name='test_search_customer_004_passed',
                                      attachment_type=AttachmentType.PNG)
                        self.sc.screenshot_pass_sc()
                        self.log.info("Clicking on Logout Button")
                        self.lp.logout_btn()
                        self.log.info("Testcase 'test_search_customer_004' Completed")
                        assert True
                    else:
                        self.log.info("Capturing Screenshot Testcase 'test_search_customer_004_failed' on Search "
                                      "Customer stage")
                        allure.attach(self.driver.get_screenshot_as_png(),
                                      name='test_search_customer_004_failed',
                                      attachment_type=AttachmentType.PNG)
                        self.sc.screenshot_fail_sc()
                        assert False
                    assert True
                else:
                    self.log.info("Capturing Screenshot Testcase 'test_search_customer_004_failed' on Add "
                                  "Customer stage_2")
                    allure.attach(self.driver.get_screenshot_as_png(),
                                  name='test_search_customer_004_on_customer_validation_level_2',
                                  attachment_type=AttachmentType.PNG)
                    self.sc.screenshot_fail_ac()
                    assert False
                assert True
            else:
                self.log.info("Capturing Screenshot Testcase 'test_search_customer_004_failed' "
                              "on Add Customer stage_1")
                allure.attach(self.driver.get_screenshot_as_png(),
                              name='test_search_customer_004_on_customer_verification_level_1',
                              attachment_type=AttachmentType.PNG)
                self.sc.screenshot_fail_ac_()
                assert False
            assert True
        else:
            self.log.info("Capturing Screenshot Testcase 'test_search_customer_004_failed' on Login Stage")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_search_customer_004_on_login_level',
                          attachment_type=AttachmentType.PNG)
            self.sc.screenshot_fail_lp()
            assert False


def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=7))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"
