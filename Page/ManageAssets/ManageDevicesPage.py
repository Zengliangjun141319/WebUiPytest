# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageDevicesPage.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/4/2023 2:19 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

from Common.Operator import Operator
from Page.comm import *
from selenium.webdriver.common.by import By


class ManageDevicesPage(Operator):
    # 左侧滑块大图标
    manageAssetLink_loc = (By.XPATH, '//div[@title="Manage Assets"]')

    # 机器管理菜单元素
    exButton_loc = (By.XPATH, '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    manageDevices_loc = (By.ID, 'nav_managegpsdevices')  # 设备管理

    # 设备管理列表元素
    iframe_loc = (By.XPATH, '//iframe[@class="set_iframe"]')  # 机器组主体页面内嵌的iframe
    searchInbox_loc = (By.ID, 'searchinputtxt')  # 搜索框
    searchBtn_loc = (By.XPATH, '//*[@id="recordcontent"]/div[2]/input[@value="Search"]')  # 搜索按钮
    addBtn_loc = (By.XPATH, '//*[@id="recordcontent"]/div[3]/span[@class="sbutton iconadd"]')  # 添加设备按钮
    refreshBtn_loc = (
    By.XPATH, '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')
    exExcelBtn_loc = (
    By.XPATH, '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconexport"]')
    importBtn_loc = (By.XPATH, '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconimport"]')

    searchSN_loc = (By.XPATH, '//*[@id="devicelist"]/div/div/div/table/tbody/tr/td[1]')  # 搜索出的设备的SN
    searchNotes_loc = (By.XPATH, '//*[@id="devicelist"]/div/div/div/table/tbody/tr/td[7]')  # 搜索出的设备的Notes

    # 添加设备页面元素
    addDeviceIframe_loc = (By.ID, 'iframe_gpsdevice')  # 添加设备页面iframe
    saveBtn_loc = (By.XPATH, '//*[@id="content1"]/div[1]/span[@class="sbutton iconsave"]')  # save按钮
    saveAndExitBtn_loc = (By.XPATH, '//*[@id="content1"]/div[1]/span[@onclick="OnSave(1);"]')  # save and exit按钮
    exitWithoutSavingBtn_loc = (
    By.XPATH, '//*[@id="content1"]/div[1]/span[@class="sbutton iconexit"]')  # exit without saving按钮

    selectSource_loc = (By.ID, 'dialog_source')  # Source下拉列表框
    deviceId_loc = (By.ID, 'dialog_sn')  # Device Air Id
    deviceEsn_loc = (By.ID, 'dialog_asn')  # Device ESN
    deviceType_loc = (By.ID, 'dialog_devicetype')  # Device Type
    seldeviceType_loc = (By.ID, 'dialog_seldevicetype')  # ATU类型下拉的Type
    deviceStatus_loc = (By.ID, 'dialog_status')  # Status
    invoiceDate_loc = (By.ID, 'dialog_invoicedate')  # Invoice Date
    invoiceNo_loc = (By.ID, 'dialog_invoiceno')  # Invoice
    startDate_loc = (By.ID, 'dialog_servicestartdate')  # Service Start Date
    notes_loc = (By.ID, 'dialog_notes')  # Notes

    saveDialog_loc = (By.XPATH, '/html/body/div[6]/div[2]/div')  # save后的对话框
    savemessage_loc = (By.XPATH, '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')
    saveDialogOkBtn_loc = (By.XPATH, ok_btn)  # 对话框上的OK按钮

    # 编辑设备相关元素
    editDeviceBtn_loc = (By.XPATH, '//*[@id="devicelist"]/div/div/div/table/tbody/tr[1]/td[19]')  # 编辑设备按钮

    # Notes相关元素
    notesBtn_loc = (By.XPATH, '//*[@id="devicelist"]/div/div/div/table/tbody/tr[1]/td[20]/a')  # Notes按钮
    notesText_loc = (By.ID, 'dialog_comments')  # Notes文本框
    sendNotesBtn_loc = (By.XPATH, '//*[@id="tab_comments"]/div/div[1]/table/tbody/tr/td/div/div/span')  # 发送Notes按钮
    sendedNotes_loc = (By.XPATH, '//*[@id="divcomments"]/div[1]/div[2]')  # 发送后的Notes内容

    # 配对相关元素
    selectAssetBtn_loc = (By.ID, 'btnSelectAsset')
    unpairBtn_loc = (By.ID, 'btnUnpair')

    firstAsset_loc = (
    By.XPATH, '//*[@id="dialog_machines"]/div[@class="dialog-content"]/div[5]/div/div[1]/div/table/tbody/tr[1]/td[1]')
    selectAssetOK_loc = (By.XPATH, '//*[@id="dialog_machines"]/div[@class="dialog-func"]/input[@value="OK"]')

    selVin_loc = (By.ID, 'dialog_vin')  # 设备编辑页面配对的机器VIN
    listsVin_loc = (By.XPATH, '//*[@id="devicelist"]/div/div[1]/div/table/tbody/tr/td[9]/span')