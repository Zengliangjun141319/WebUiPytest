# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_logins.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/1/2023 11:26 AM   
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
from selenium.webdriver.common.by import By
import allure

log = Log("test_logins")


@pytest.fixture(scope='class')
def starts():
    driver = browser("chrome")
    lg = Logins()
    lg.login(driver)
    driver.implicitly_wait(10)

    yield lg
    driver.quit()


@pytest.mark.usefixtures('starts')
class TestLogins(Operator):

    home_log = (By.ID, 'button_home')
    btnuser = (By.ID, 'btnuser')
    loc = (By.ID, 'spanusername')

    # 修改密码元素
    changePwBtn_loc = (By.XPATH, '//*[@id="usermenu_panel"]/ul/li[2]/table/tbody/tr/td[2]/span')
    oldpw_loc = (By.ID, 'txt_old_pass')
    newpw_loc = (By.ID, 'txt_new_pass')
    confirmpw_loc = (By.ID, 'txt_new_pass2')
    changeOk_loc = (By.ID, 'button_submit')

    # 退出登录相关元素
    logout_loc = (By.XPATH, '//*[@id="usermenu_panel"]/ul/li[3]/table/tbody/tr/td[2]/span')
    loginB_loc = (By.ID, 'btn_login')

    @allure.feature("用户登录相关测试")
    @allure.story("测试登录功能")
    def test_login(self, starts):
        starts.click(self.home_log)
        time.sleep(2)
        starts.click(self.btnuser)
        time.sleep(1)

        displayname = starts.find_element(self.loc).text
        starts.click(self.btnuser)
        assert displayname == 'Auto Test'

    def change_password(self, starts):
        starts.driver.refresh()
        time.sleep(2)

        starts.click(self.btnuser)
        try:
            starts.click(self.changePwBtn_loc)
            time.sleep(1)
        except Exception:
            log.info('open change password failed!')
            return False
        else:
            starts.send_keys(self.oldpw_loc, 'Win.12345')
            starts.send_keys(self.newpw_loc, 'Win.12345')
            starts.send_keys(self.confirmpw_loc, 'Win.12345')
            time.sleep(1)

            try:
                starts.click(self.changeOk_loc)
                time.sleep(2)
                starts.driver.switch_to.alert.accept()
                time.sleep(1)
            except Exception:
                return False
            else:
                return True

    @allure.feature("用户登录相关测试")
    @allure.story("测试修改密码")
    def test_change_password(self, starts):
        assert self.change_password(starts)

    @allure.feature("用户登录相关测试")
    @allure.story("测试退出功能")
    def test_logout(self, starts):
        starts.driver.refresh()
        time.sleep(3)

        starts.click(self.btnuser)
        time.sleep(1)
        starts.click(self.logout_loc)

        # 判断是否正确退出
        res = starts.is_text_in_value(self.loginB_loc, 'LOGIN')
        assert res


if __name__ == '__main__':
    # unittest.main()
    pytest.main(['-v', 'Testlogins.py'])  # 主函数模式  生成HTML测试报告 '--html=./report/report.html'
