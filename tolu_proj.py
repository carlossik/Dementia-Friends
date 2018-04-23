from selenium import webdriver
import pytest
import splinter
from splinter import Browser
from selenium.webdriver.common.by import By

class Login_tests():

    driver = webdriver.Chrome()
    baseURL = "https://uat-alzheimerscommunities.cs81.force.com/"






    def test_valid_users(self):
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
            self.driver.get(self.baseURL)
            self.driver.find_element_by_xpath('/html/body/div/span[1]/div[1]/div[3]/a[1]').click()
            self.driver.find_element_by_id('j_id0:j_id69:email').send_keys("tolu1@mailinator.com")
            self.driver.find_element_by_id('j_id0:j_id69:password').send_keys("Hulster2017")
            self.driver.find_element_by_id('j_id0:j_id69:Submit').click()
            self.driver.implicitly_wait(30)
            if self.driver.find_elements_by_css_selector('a.btn:nth-child(2)'):
                print("login_tets passed")
            else:
                print("login_test failed")
    def test_tabs(self):
        click_home_tab = self.driver.find_element(By.LINK_TEXT, "Home").click()
        click_get_involved = self.driver.find_element(By.LINK_TEXT, "Get involved").click()
        click_faqs = self.driver.find_element(By.LINK_TEXT, "FAQs").click()
        click_what_is_dementia = self.driver.find_element(By.LINK_TEXT, "What is dementia?").click()
        click_news = self.driver.find_element(By.LINK_TEXT, "News & press").click()
        click_contact_us = self.driver.find_element(By.LINK_TEXT, "Contact us").click
        if self.driver.find_elements_by_css_selector('#page_content > h1:nth-child(1) > abbr:nth-child(1)'):
            print("FAQ tab is working as expected")
        else:
            print("FAQ not working")
        if self.driver.find_element_by_css_selector(".col-md-8 > h1:nth-child(1)"):
            print("what is dementia tab works as expected")
        else:
            print("what is dementia is not working")
        if self.driver.find_element_by_css_selector(".col-md-8 > h1:nth-child(1)"):
            print("News tab works")
        else:
            print("New tab is caput")
        if self.driver.find_element_by_css_selector("ul.nav:nth-child(1) > li:nth-child(6) > a:nth-child(1)"):
            print("contact us works")
            self.driver.close()
        else:
            print("contactus not working")


    def cross_browser(self):
        driverstack = webdriver.Chrome
        driverstack2 = webdriver.Firefox
        driverstack3 = webdriver.Ie
        browsers = [driverstack,driverstack2,driverstack3]
        for browser in browsers:

            browser.get(self.baseURL)
            print("testing for" + browser)























ff = Login_tests()
ff.test_valid_users()
ff.test_tabs()
ff.cross_browser()



