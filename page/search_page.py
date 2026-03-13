from base.base_page import BasePage
from selenium.webdriver.common.by import By
from utils import DriverUtils
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
        self.iframe = (By.ID,"layui-layer-iframe1")
        self.span = (By.XPATH,"//*[@class='conect-title']/span")

    def tp_search_to_add(self,search_text):
        """输入内容并搜索"""
        # 返回首页
        self.find_el(self.index).click()
        self.input_text(self.find_el(self.search_input),search_text)
        self.find_el(self.search_btn).click()
        # 点击加入购物车按钮
        self.driver.find_elements(*self.add_cat_btn)[0].click()
        self.find_el(self.add_btn).click()
        time.sleep(1)
        # 子窗口
        try:
            self.switch_frame(self.find_el(self.iframe))
            msg = self.find_el(self.span).text
            # 可以点击 要回退父页面
            self.driver.switch_to.default_content()
            self.find_el(self.cancel).click()
        except Exception as e:
            msg = ""
            print(e)
        return msg