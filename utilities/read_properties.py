import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', "admin_url_page")
        return url

    @staticmethod
    def username():
        username = config.get('admin login info', "username")
        return username

    @staticmethod
    def password():
        password = config.get('admin login info', "password")
        return password

    @staticmethod
    def invalid_username():
        invalid_username = config.get('admin login info', "invalid_username")
        return invalid_username