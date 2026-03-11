from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By
import time
class AdminUpdateGoodFilePage(BasePage):
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        # 获取iframe
        self.iframe = (By.ID,"layui-layer-iframe1")
        # 上传文件按钮
        self.update_btn = (By.XPATH,"//*[@name='file[]']")
        self.img = (By.XPATH,"//*[@class='icon']")
        self.comfirm_btn = (By.ID,"confirm")

    def tp_update_file(self,file_name):
        print("is coming!!!!!!!!!")
        self.switch_frame(self.find_el(self.iframe))
        # # update点击
        # if self.find_el(self.update_btn) is None:
        #     print("is none")
        # else:
        #     print("is have") 找到update按钮了
        # print(f"路径：{file_name}")
        """TUDO:上文文件按钮"""
        # self.find_el(self.update_btn).send_keys(file_name)
        """选择已经存在的文件"""
        self.find_el(self.img).click()
        self.find_el(self.comfirm_btn).click()
        time.sleep(2)

        
        