from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By
import time
class SearchPage(BasePage):
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        # 输入框
        self.search_input = (By.XPATH,"//input[@class='ecsc-search-input']")
        # 搜索按钮
        self.search_btn = (By.XPATH,"//button[@class='ecsc-search-button']")
        self.index = (By.XPATH,"//a[text()='首页']")
        self.add_cat_btn = (By.XPATH,"//a[text()='加入购物车']")
        self.add_btn = (By.XPATH,"//*[@id='join_cart']")
        self.cancel = (By.XPATH,"//*[@class='layui-layer-setwin']/a")

    def tp_search_to_add(self,search_text):
        """输入内容并搜索"""
        # 返回首页
        self.find_el(self.index).click()
        self.input_text(self.find_el(self.search_input),search_text)
        self.find_el(self.search_btn).click()
        # 点击加入购物车按钮
        self.driver.find_elements(*self.add_cat_btn)[0].click()
        self.find_el(self.add_btn).click()
        # 取消
        time.sleep(1)
        self.find_el(self.cancel).click()
