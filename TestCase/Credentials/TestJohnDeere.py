# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     TestJohnDeere.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/1/2023 4:03 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import pytest
from Common.logger import Log
from Common.Operator import *
from Common.Logins import Logins
from Page.Credentials.CredentialsPage import CredentialsPage as cp
from selenium.webdriver.common.by import By
import allure

log = Log("TestJohnDeere")


class TestJohnDeere:
    driver = None
    lg = None
    page = None

    coll = (By.XPATH, '//*[@id="nav_arrow"]/div')

    @pytest.fixture()
    def begin(self):
        log.info('--------开始测试John Deere Credentials功能--------')
        self.driver = browser("chrome")
        self.lg = Logins()
        self.lg.login(self.driver, 'atcred@iicon004.com', 'Win.12345')
        self.driver.implicitly_wait(10)

        self.page = cp()
        ac = self.lg.get_attribute(self.coll, 'class')
        while True:
            if ac != 'icn collapse':
                ar = (By.ID, 'nav_arrow')
                self.page.click(ar)
                continue
            else:
                break
        self.lg.click(self.page.johndeere_menu)
        time.sleep(1)
        self.lg.switch_to_iframe(self.page.right_iframe)

        yield self.lg
        self.driver.quit()

    def add_jdlink(self, begin):
        log.info('点击 JD Link 的Add')
        if not begin.is_clickable(self.page.jdlink_add_btn):
            time.sleep(2)
        try:
            begin.click(self.page.jdlink_add_btn)
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            txt = begin.get_text(self.page.jdlink_page_signin_lable)
        except Exception:
            log.info('Add 跳转失败!')
            return False
        else:
            log.info('Add 跳转成功!')
            self.driver.switch_to.window(self.driver.window_handles[0])
            if txt == 'Sign In':
                return True
            else:
                return False

    @allure.feature("测试Credentials功能")
    @allure.story("测试JD Link Credentials设置功能")
    def test_addJDlink(self, begin):
        """测试Add JD Link功能"""
        res = self.add_jdlink(begin)
        if res:
            log.info('Add JD Link 测试成功！')
        else:
            log.info('Add JD Link 测试失败！')
        assert res


if __name__ == '__main__':
    pytest.main(['-vs', 'TestJohnDeere.py'])  # 主函数模式
