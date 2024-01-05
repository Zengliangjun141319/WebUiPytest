# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CredentialsPage.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/25/2023 10:39 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'


from Common.Operator import Operator
from Page.comm import *
from selenium.webdriver.common.by import By


class CredentialsPage(Operator):
    # 左侧菜单
    exp_btn = (By.ID, 'nav_arrow')
    credentials_menu = (By.ID, 'nav_credential')
    johndeere_menu = (By.ID, 'nav_jdlink')
    apicred_menu = (By.ID, 'nav_apicredential')

    # Credentials页面
    right_iframe = (By.XPATH, '//*[@id="set_right"]/iframe')

    cred_add_btn = (By.XPATH, '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconadd"]')
    cred_refresh_btn = (By.XPATH, '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconrefresh"]')
    cred_list_edit_btn = (By.XPATH, '//*[@id="credentiallist"]/div/div/div/table/tbody/tr/td/a[@title="Edit"]')
    cred_list_del_btn = (By.XPATH, '//*[@id="credentiallist"]/div/div/div/table/tbody/tr/td/a[@title="Delete"]')
    lists = (By.XPATH, '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr')
    cred_del_yes_btn = (By.XPATH, yes_btn)  # '/html/body/div[19]/div[3]/input[2]'
    # 新建窗口
    cred_add_urlkey_inbox = (By.ID, 'dialog_urlkey')
    cred_add_username_inbox = (By.ID, 'dialog_username')
    cred_add_passwd_inbox = (By.ID, 'dialog_password')
    cred_add_enabled_chx = (By.ID, 'dialog_enabled')
    cred_add_notes_inbox = (By.ID, 'dialog_notes')
    cred_add_ok_btn = (By.XPATH, '//*[@id="dialog_credential"]/div[3]/input[@value="OK"]')

    # John Deere页面
    jdlink_add_btn = (By.XPATH, '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconadd"]')
    # 跳转新页面
    # jdlink_page_signin_lable = (By.XPATH, '//*[@id="form32"]/div[1]/h2')  # Sign In
    jdlink_page_signin_lable = (By.XPATH, '//*[@id="okta-sign-in"]/div[2]/div/div/form/div/h2')

    # API页面
    api_add_btn = (By.XPATH, '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconadd"]')
    api_refresh_btn = (By.XPATH, '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconrefresh"]')

    api_name_chelist = (By.ID, 'dialog_apiname')  # value=43  JCB
    api_username_inbox = (By.ID, 'dialog_username')
    api_pwd_inbox = (By.ID, 'dialog_password')
    api_key_inbox = (By.ID, 'dialog_apikey')
    api_secret_inbox = (By.ID, 'dialog_apisecret')
    api_ok_btn = (By.XPATH, '//*[@id="dialog_credential"]/div[3]/input[@value="OK"]')

    api_list_edit_btn = (By.XPATH, '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Edit"]')
    api_list_del_btn = (By.XPATH, '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Delete"]')

    api_del_yes_btn = (By.XPATH, yes_btn)  # /html/body/div[19]/div[3]/input[2]
