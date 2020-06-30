# coding=utf-8

from selenium import webdriver
from utils.LoggingUtil import Logger

log = Logger().instance()

class BasePage():

    def __init__(self, driver, url):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.driver.get(url)

    def find_element(self, t_selector):
        selector = t_selector[0]
        value = t_selector[1]
        if selector.upper() == 'ID':
            ele = self.driver.find_element_by_id(value)
        elif selector.upper() == 'NAME':
            ele = self.driver.find_element_by_name(value)
        elif selector.upper() == 'CLASS':
            ele = self.driver.find_element_by_class_name(value)
        elif selector.upper() == 'TAG':
            ele = self.driver.find_element_by_tag_name(value)
        elif selector.upper() == 'CSS':
            ele = self.driver.find_element_by_css_selector(value)
        elif selector.upper() == 'XPATH':
            ele = self.driver.find_elements_by_xpath(value)
        elif selector.upper() == 'LINK_TEXT':
            ele = self.driver.find_element_by_link_text(value)
        elif selector.upper() == 'PARTIAL_LINK_TEXT':
            ele = self.driver.find_element_by_partial_link_text(value)
        else:
            raise NameError('Illegal Selector Type')

        return ele

    def sendKeys(self, selector, text):
        ele = None
        try:
            ele = self.find_element(selector)
        except Exception:
            log.error(f"Element Not Found [{selector[0], selector[1]}]")
        try:
            ele.send_keys(text)
            log.info(f"Input <{text}> Into [{selector[0], selector[1]}]")
        except NameError as e:
            log.error(e)

    def clear(self, selector):
        ele = self.find_element(selector)
        try:
            ele.clear()
        except NameError as e:
            log.error(e)

    def click(self, selector):
        ele = self.find_element(selector)
        try:
            ele.click()
            log.info(f"Click Element [{selector[0], selector[1]}]")
        except NameError as e:
            log.error(e)
