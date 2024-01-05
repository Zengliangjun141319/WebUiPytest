# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     TestManageDevices.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/4/2023 2:06 PM   
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
import allure
from Common.excel import *
from Common.queryMSSQL import updateSQL
from Page.ManageAssets.ManageDevicesPage import ManageDevicesPage

log = Log("TestManageDevices")
file_path = "TestData\\managedevice.xlsx"
testData = get_list(file_path)


# 初始化数据库数据
def clearTestData():
    log.info('从数据库删除测试数据')
    dta = 'ironintel_admin'
    dtm = 'IICON_001_FLVMST'
    sqlstr = "delete from GPSDEVICES where CONTRACTORID='IICON_001' and Notes like '%AutoTest%'"
    sqls = "delete from COMMENTS where COMMENTS like '%AutoTest%'"
    updateSQL(dta, sqlstr)
    updateSQL(dtm, sqls)


@pytest.fixture(scope='class')
def begin():
    driver = browser("chrome")
    lg = Logins()
    lg.login(driver, 'atdevice@iicon001.com', 'Win.12345')
    driver.implicitly_wait(10)
    clearTestData()

    lg.device = ManageDevicesPage()
    try:
        lg.switch_to_iframe(lg.device.iframe_loc)
        time.sleep(1)
    except Exception:
        log.info('------Open Manage Devices failed!')
    else:
        log.info('------Open Manage Devices completed!')

    yield lg
    clearTestData()
    driver.quit()


@pytest.mark.usefixtures("begin")
class TestManageDevices:
    def saveDevices(self, begin, data):
        current_time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        current_date1 = time.strftime('%m/%d/%Y')
        time.sleep(1)
        try:
            while not begin.is_clickable(begin.device.addBtn_loc):
                log.info('添加按钮不可点击，等待3秒再看')
                time.sleep(3)
            begin.click(begin.device.addBtn_loc)
            time.sleep(1)
            begin.switch_to_iframe(begin.device.addDeviceIframe_loc)
            time.sleep(1)
        except Exception:
            log.info('--------打开添加设备页面失败！--------')
        else:
            log.info('----测试：  %s' % data['casename'])
            time.sleep(3)
            begin.select_by_text(begin.device.selectSource_loc, data['source'])
            time.sleep(2)
            if data['source'] == 'Foresight ATU':
                begin.select_by_text(begin.device.seldeviceType_loc, data['type'])
            else:
                begin.send_keys(begin.device.deviceType_loc, data['type'])

            begin.send_keys(begin.device.deviceId_loc, data['sn'])
            time.sleep(2)

            begin.send_keys(begin.device.invoiceDate_loc, current_date1)
            begin.send_keys(begin.device.invoiceNo_loc, current_time1)
            begin.send_keys(begin.device.startDate_loc, current_date1)
            begin.send_keys(begin.device.notes_loc, 'AutoTestNotes' + current_time1)
            try:
                begin.click(begin.device.saveBtn_loc)
                time.sleep(1)
                mess = begin.get_text(begin.device.savemessage_loc)
                time.sleep(1)
                begin.click(begin.device.saveDialogOkBtn_loc)
                time.sleep(1)
                res = (mess == data['mess'])
            except Exception:
                log.info('-----保存设备添加失败！-----')
                res = False
            else:
                begin.click(begin.device.exitWithoutSavingBtn_loc)
                time.sleep(3)
                begin.driver.switch_to.default_content()
                begin.switch_to_iframe(begin.device.iframe_loc)
                time.sleep(3)
            return res

    @allure.feature('测试设备管理相关功能')
    @allure.story('测试新建设备')
    @pytest.mark.parametrize('data', testData)
    def test_add_devices(self, begin, data):
        """测试添加设备"""
        res = self.saveDevices(begin, data)
        assert res


if __name__ == '__main__':
    pytest.main(['-vs', 'TestManageDevices.py'])  # 主函数模式
