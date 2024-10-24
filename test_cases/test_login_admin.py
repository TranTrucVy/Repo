import pytest
from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from test_cases.conftest import setup
from utilities.read_properties import Read_Config
import logging
from utilities.custom_logger import Log_Maker

import logging

class Test_Login_Admin:
    admin_url_page = Read_Config.get_admin_page_url()
    username = Read_Config.username()
    password = Read_Config.password()
    invalid_username = Read_Config.invalid_username()

    # Static method to configure logger


    # Initialize the logger
    logger = Log_Maker.log_gen()

    def test_verification_title(self, setup):
        self.driver = setup
        self.driver.get(self.admin_url_page)
        act_title = self.driver.title
        exp_title = "Your store. Login"
        self.logger.info("Starting test_verification_title")

        if act_title == exp_title:
            self.logger.info("Title matches expected value")
            assert True
            self.driver.close()
        else:
            self.logger.info("Title does not match expected value")
            self.driver.close()
            assert False

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_url_page)
        self.adminlp = Login_Admin_Page(self.driver)
        self.adminlp.enter_username(self.invalid_username)
        self.adminlp.enter_password(self.password)
        self.adminlp.click_btnlogin()
        self.logger.info("Running test_invalid_login")
        
        err_mess = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li").text
        if err_mess == "No customer account found":
            self.logger.info("Error message found: No customer account found")
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_invalid.png")
            self.driver.close()
        else:
            self.logger.info("Test failed: Error message not found")
            self.driver.close()
