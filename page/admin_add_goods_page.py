from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from page.admin_update_good_file_page import AdminUpdateGoodFilePage
import os
class AdminAddGoodsPage(BasePage):
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        # iframe元素
        self.iframe = (By.ID,"workspace")
        self.add_good_btn = (By.XPATH,"//*[@class='add']/..")
        # 商品名称
        self.good_name = (By.XPATH,"//*[@class='input-txt']")
        # 一级分类
        self.caregory_one = (By.ID,"cat_id")
        self.caregory_two = (By.ID,"cat_id_2")
        self.caregory_three = (By.ID,"cat_id_3")
        # 商品简介
        self.desc = (By.XPATH,"//*[@name='goods_remark']")
        # 商品品牌
        self.band = (By.ID,"brand_id")
        self.supplier = (By.ID,"suppliers_id")
        self.sell = (By.XPATH,"//*[@name='shop_price']")
        self.market_price = (By.XPATH,"//*[@name='market_price']")
        """TUDO:文件上传"""
        # 文件上传按钮
        self.update_file_btn = (By.XPATH,"//input[@class='type-file-file']")
        # 是否包邮：是
        self.is_free_shipping = (By.ID,"is_free_shipping_label_1")
        self.submit = (By.ID,"submit")



    def tp_add_good(self,g_name,caregory_one,caregory_two,caregory_three,desc,band,supplier,sell,market_price,file_name):
        # 切换iframe
        self.switch_frame(self.find_el(self.iframe))
        self.find_el(self.add_good_btn).click()
        self.input_text(self.find_el(self.good_name),g_name)
        Select(self.find_el(self.caregory_one)).select_by_value(caregory_one)
        Select(self.find_el(self.caregory_two)).select_by_value(caregory_two)
        Select(self.find_el(self.caregory_three)).select_by_value(caregory_three)
        self.input_text(self.find_el(self.desc),desc)
        Select(self.find_el(self.band)).select_by_value(band)
        Select(self.find_el(self.supplier)).select_by_value(supplier)
        self.input_text(self.find_el(self.sell),sell)
        self.input_text(self.find_el(self.market_price),market_price)
        # 文件上传部分
        # 点击按钮
        self.find_el(self.update_file_btn).click()
        # update's iframe
        update = AdminUpdateGoodFilePage()
        current_path = os.path.dirname(os.path.abspath(__file__))
        # 使用 os.path.join 会自动根据操作系统处理斜杠问题
        file_path = os.path.join(current_path, "data", file_name)
        print(f"--- 尝试上传文件前，完整路径为: {file_path} ---")
        file_path = file_path.replace("\\", "/")
        print(f"--- 尝试上传文件后，完整路径为: {file_path} ---")
        update.tp_update_file(file_path)
        time.sleep(0.5)
        # self.find_el(self.is_free_shipping).click()
        # self.find_el(self.submit).click()



