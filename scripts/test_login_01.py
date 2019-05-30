import os, sys

from page.elements_Login_Part import ElementsLoginPart

sys.path.append(os.getcwd())

import time

import allure
import pytest
from selenium.webdriver.common.by import By

from base.get_Driver import get_phone_driver
from base.page import Page
from base.getfiledata import GetFileData
from selenium.common.exceptions import TimeoutException


def get_login():
    suc_list = []
    fail_list = []
    login_data = GetFileData().get_yaml_data("logindata.yaml")
    for i in login_data:
        if (login_data.get(i)).get("toast"):
            fail_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd"),
                              login_data.get(i).get("toast"), login_data.get(i).get("expect_data")))
        else:
            suc_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("expect_data")))
    return {"suc": suc_list, "fail": fail_list}


class TestLoginTes:

    def setup_class(self):
        self.driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_in_login(self):
        self.page.get_main_page().mp_click_mine_btn()
        self.page.get_login_page().lp_click_go_login()

    # @pytest.mark.parametrize("case_num, account, passwd, expect_data", get_login().get("suc"))
    # def test_login_test_01(self, case_num, account, passwd, expect_data):
    #     # self.page.get_main_page().mp_click_mine_btn()
    #     # self.page.get_login_page().lp_click_go_login()
    #     self.page.get_login_page().lp_input_username(account)
    #     self.page.get_login_page().lp_input_password(passwd)
    #     self.page.get_login_page().lp_click_login_btn()
    #     try:
    #         shop_cart = self.page.get_mine_page().minep_get_result()
    #         try:
    #             assert expect_data in shop_cart
    #         except AssertionError:
    #             self.page.get_mine_page().screen_page()
    #             assert False
    #         finally:
    #             self.page.get_mine_page().minep_click_settings_btn()
    #             self.page.get_settings_page().sp_click_logout_btn()
    #
    #     # except TimeoutException:
    #     #     self.page.get_mine_page().screen_page()
    #     #     self.page.get_login_page().lp_click_close_login_page_btn()
    #     #     assert False
    #
    #     except TimeoutException:
    #         self.page.get_settings_page().screen_page()
    #         try:
    #             self.page.get_login_page().lp_if_login_btn()
    #             self.page.get_login_page().lp_click_close_login_page_btn()
    #
    #
    #         except TimeoutException:
    #             self.page.get_mine_page().minep_click_settings_btn()
    #             self.page.get_settings_page().sp_click_logout_btn()
    #         assert False

    @pytest.mark.parametrize("case_num, account, passwd, toast, expect_data", get_login().get("fail"))
    def test_login_fail(self, case_num, account, passwd, toast, expect_data):
        # self.page.get_main_page().mp_click_mine_btn()
        # self.page.get_login_page().lp_click_go_login()
        self.page.get_login_page().lp_input_username(account)
        self.page.get_login_page().lp_input_password(passwd)
        self.page.get_login_page().lp_click_login_btn()

        try:
            # toast_data = "此用户不存在"
            toast_data = self.page.get_settings_page().get_toast(toast)
            print(toast_data)
            try:
                self.page.get_login_page().lp_if_login_btn()
                assert toast_data == expect_data
                self.page.get_login_page().lp_click_close_login_page_btn()
            except TimeoutException:
                self.page.get_settings_page().screen_page()
                self.page.get_mine_page().minep_click_settings_btn()
                self.page.get_settings_page().sp_click_logout_btn()
                assert False
            except AssertionError:
                self.page.get_settings_page().screen_page()
                self.page.get_login_page().lp_click_close_login_page_btn()
                assert False
        except TimeoutException:
            self.page.get_settings_page().screen_page()
            try:
                self.page.get_login_page().lp_if_login_btn()
                self.page.get_login_page().lp_click_close_login_page_btn()

            except TimeoutException:
                self.page.get_mine_page().minep_click_settings_btn()
                self.page.get_settings_page().sp_click_logout_btn()
            assert False
