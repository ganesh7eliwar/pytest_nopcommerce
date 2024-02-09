from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Search_customer:
    email_by_xpath = "//input[@id='SearchEmail']"
    first_name_by_xpath = "//input[@id='SearchFirstName']"
    last_name_by_xpath = "//input[@id='SearchLastName']"
    month_by_xpath = "//select[@id='SearchMonthOfBirth']"
    day_by_xpath = "//select[@id='SearchDayOfBirth']"
    registration_date_from_by_xpath = "//input[@id='SearchRegistrationDateFrom']"
    registration_date_to_by_xpath = "//input[@id='SearchRegistrationDateTo']"
    last_activity_from_by_xpath = "//input[@id='SearchLastActivityFrom']"
    last_activity_to_by_xpath = "//input[@id='SearchLastActivityTo']"
    company_by_xpath = "//input[@id='SearchCompany']"
    ip_address_by_xpath = "//input[@id='SearchIpAddress']"
    click_customer_roles_by_xpath = "//div[@role='listbox']"
    select_customer_roles_options_by_xpath = "//li[normalize-space()='Forum Moderators']"
    search_button_by_xpath = "//button[@id='search-customers']"
    edit_button_by_xpath = "//a[@class='btn btn-default']"
    edit_customer_by_xpath = "//h1[@class='float-left']"

    def __init__(self, driver):
        self.driver = driver

    def customer_email(self, email):
        self.driver.find_element(By.XPATH, self.email_by_xpath).send_keys(email)

    def customer_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.first_name_by_xpath).send_keys(first_name)

    def customer_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.last_name_by_xpath).send_keys(last_name)

    def month(self, month):
        Select(self.driver.find_element(By.XPATH, self.month_by_xpath)).select_by_visible_text(month)

    def day(self, day):
        Select(self.driver.find_element(By.XPATH, self.day_by_xpath)).select_by_visible_text(day)

    def click_registration_date_from(self, date_from):
        self.driver.find_element(By.XPATH, self.registration_date_from_by_xpath).send_keys(date_from)

    def click_registration_date_to(self, date_to):
        self.driver.find_element(By.XPATH, self.registration_date_to_by_xpath).send_keys(date_to)

    def click_last_activity_from(self, from_date):
        self.driver.find_element(By.XPATH, self.last_activity_from_by_xpath).send_keys(from_date)

    def click_last_activity_to(self, to_date):
        self.driver.find_element(By.XPATH, self.last_activity_to_by_xpath).send_keys(to_date)

    def company(self, company_name):
        self.driver.find_element(By.XPATH, self.company_by_xpath).send_keys(company_name)

    def ip_address(self, ip_address):
        self.driver.find_element(By.XPATH, self.ip_address_by_xpath).send_keys(ip_address)

    def customer_roles(self):
        self.driver.find_element(By.XPATH, self.click_customer_roles_by_xpath).click()

    def customer_roles_click(self):
        self.driver.find_element(By.XPATH, self.select_customer_roles_options_by_xpath).click()

    def search_btn(self):
        self.driver.find_element(By.XPATH, self.search_button_by_xpath).click()

    def edit_btn(self):
        self.driver.find_element(By.XPATH, self.edit_button_by_xpath).click()

    def search_customer_validation(self):
        try:
            self.driver.find_element(By.XPATH, self.edit_customer_by_xpath)
            return "You are on the Edit Customer Page"
        except NoSuchElementException:
            return "Operation Failed"

    def screenshot_pass_sc(self):
        self.driver.save_screenshot("..\\screenshots\\search_customer\\test_search_customer_004_pass.png")

    def screenshot_fail_sc(self):
        self.driver.save_screenshot("..\\screenshots\\search_customer\\test_search_customer_004_fail.png")

    def screenshot_fail_ac(self):
        self.driver.save_screenshot("..\\screenshots\\search_customer\\ac_test_search_customer_004_fail.png")

    def screenshot_fail_ac_(self):
        self.driver.save_screenshot("..\\screenshots\\search_customer\\_ac_test_search_customer_004_fail.png")

    def screenshot_fail_lp(self):
        self.driver.save_screenshot("..\\screenshots\\search_customer\\lp_test_search_customer_004_fail.png")
