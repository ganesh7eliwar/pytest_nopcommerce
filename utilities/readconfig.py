import configparser

config = configparser.RawConfigParser()
config.read("D:\\ct_17_batch_revision\\Pytest_Framework_By_Tushar_Sir\\Pytest_nopcommerce\\configuration\\config.ini")


class Readconfig:
    @staticmethod
    def get_email():
        email = config.get('static data', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('static data', 'password')
        return password

    @staticmethod
    def get_email_1():
        email_1 = config.get('add_customer data', 'email')
        return email_1

    @staticmethod
    def get_password_1():
        password_1 = config.get('add_customer data', 'password')
        return password_1

    @staticmethod
    def get_first_name():
        first_name = config.get('add_customer data', 'first_name')
        return first_name

    @staticmethod
    def get_last_name():
        last_name = config.get('add_customer data', 'last_name')
        return last_name

    @staticmethod
    def get_company():
        company = config.get('add_customer data', 'company')
        return company

    @staticmethod
    def get_comment():
        comment = config.get('add_customer data', 'comment')
        return comment

    @staticmethod
    def get_date_of_birth():
        date_of_birth = config.get('add_customer data', 'date_of_birth')
        return date_of_birth

    @staticmethod
    def get_month():
        month = config.get('search_customer data', 'month')
        return month

    @staticmethod
    def get_day():
        day = config.get('search_customer data', 'day')
        return day

    @staticmethod
    def get_date_from():
        date_from = config.get('search_customer data', 'date_from')
        return date_from

    @staticmethod
    def get_date_to():
        date_to = config.get('search_customer data', 'date_to')
        return date_to

    @staticmethod
    def get_from_date():
        from_date = config.get('search_customer data', 'from_date')
        return from_date

    @staticmethod
    def get_to_date():
        to_date = config.get('search_customer data', 'to_date')
        return to_date

    @staticmethod
    def get_ip_address():
        ip_address = config.get('search_customer data', 'ip_address')
        return ip_address

    @staticmethod
    def get_gender_male():
        gender = config.get('add_customer data', 'gender_male')
        return gender

    @staticmethod
    def get_gender_female():
        gender = config.get('add_customer data', 'gender_female')
        return gender

    @staticmethod
    def get_vendor_value():
        value = config.get('add_customer data', 'vendor_value')
        return value

    @staticmethod
    def get_tax_box_check():
        check = config.get('add_customer data', 'tax_box_check')
        return check

    @staticmethod
    def get_tax_box_uncheck():
        uncheck = config.get('add_customer data', 'tax_box_uncheck')
        return uncheck

    @staticmethod
    def get_active_box_check():
        check = config.get('add_customer data', 'active_btn_check')
        return check

    @staticmethod
    def get_active_box_uncheck():
        uncheck = config.get('add_customer data', 'active_btn_uncheck')
        return uncheck
