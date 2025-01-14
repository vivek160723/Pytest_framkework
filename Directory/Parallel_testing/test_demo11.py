import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemo:
    def  test_login(self,setupp):
        self.driver=setupp
        self.driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("abc123@gmail.com")
        self.driver.find_element(By.XPATH,'//*[@id="passwd"]').send_keys("abc123")
        self.driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span').click()