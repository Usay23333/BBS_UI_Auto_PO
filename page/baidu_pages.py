# coding=utf-8

from page.basepage import BasePage


class BaiduSearch(BasePage):
    ele_input_search = ('id', 'kw')
    ele_button_search = ('id', 'su')

    def input_value(self, text):
        self.sendKeys(self.ele_input_search, text)

    def click_search(self):
        self.click(self.ele_button_search)
