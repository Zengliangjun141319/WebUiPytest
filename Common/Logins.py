# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Logins.py
   Author :        曾良均
   QQ:             277099728
   Date：          11/30/2023 3:34 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

from .Operator import *
from .queryMSSQL import *
from selenium.webdriver.common.by import By

url = "https://iron.soft.rz/login/"


class Logins(Operator):
    # locations
    username = (By.ID, "txt_uid")
    pwd = (By.ID, "txt_pwd")
    loginBtn = (By.ID, "btn_login")
    forget = (By.XPATH, '/html/body/form/div[4]/div/div[2]/div/div[8]/a/span')
    term_acc = (By.XPATH, '//*[@id="panel_bottom"]/input[@value="Accept and continue"]')

    # def __init__(self, driver, url=url):
    #     self.driver = driver
    #     self.open(url)
    #     sys.stderr.write('Test Site is: %s \n' % url)

    def login(self, driver, accont='auto@iicon004.com', pwd='Win.12345'):
        """Login mothed"""
        self.driver = driver
        self.open(url)

        self.send_keys(self.username, accont)
        self.send_keys(self.pwd, pwd)
        self.click(self.loginBtn)

        time.sleep(1)
        time0 = time.time()
        # verify code
        try:
            vc = (self.driver.find_element(By.XPATH, '//*[@id="panel_verifycode"]/div/div/div[2]/input[1]'))
            vc.click()
        except Exception as e:
            sys.stderr.write('------Don\'t neet verify code! ------\n')
        else:
            sys.stderr.write('Time used: %s \n' % (time.time() - time0))
            try:
                codes = getVerifyCode(loginuser=accont)
                vc.send_keys(codes)
                time.sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="panel_verifycode"]/div/div/div[2]/input[2]').click()
            except Exception as e:
                sys.stderr.write('------Input verify code failed! \n')
            else:
                sys.stderr.write('------Input verify code completed! \n ')

        # Terms
        try:
            time.sleep(2)
            ter = self.driver.find_element(By.XPATH, '//*[@id="panel_bottom"]/input[@value="Accept and continue"]')
            ter.click()
        except Exception as e:
            sys.stderr.write('------Don\'t need terms! \n')
        else:
            sys.stderr.write('------User Access terms! \n')
