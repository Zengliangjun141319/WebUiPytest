# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Operator.py
   Author :        曾良均
   QQ:             277099728
   Date：          11/30/2023 9:12 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as fOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *   # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
from selenium import webdriver
from selenium.webdriver import Remote
import time


def browser(browser="chrome"):
    """
    打开浏览器函数:Firefox、chrome、ie、phantomjs
    """
    # 定义多终端浏览器
    nodes = [
        'http://192.168.25.107:5555/wd/hub',
        'http://192.168.25.49:5555/wd/hub',
        'http://192.168.25.107:5566/wd/hub'
    ]
    x = random.randint(0, 2)

    # 定义下载路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    downloads = os.path.abspath(os.path.join(base_dir, ".\\report"))

    try:
        if browser == "firefox":
            # profile_dir = r'C:\Users\zlj\AppData\Roaming\Mozilla\Firefox\Profiles\i40450n1.default-release'
            # profile = webdriver.FirefoxProfile(profile_dir)
            # driver = webdriver.Firefox(profile)
            sys.stderr.write("------ 这里是Firefox浏览器 ------\n")
            options = fOptions()
            # driver = webdriver.Firefox(firefox_options=options, firefox_binary=r"C:\Mozilla Firefox\firefox.exe")
            driver = webdriver.Firefox(options)
            return driver
        elif browser == "chromeH":
            # Chrome无界面模式
            sys.stderr.write("------ 这里是Chrome无界面模式 ------\n")
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--ignore-certificate-errors')  # 屏蔽HTTPS非信任站点
            # 设置浏览器默认下载路径
            prefs = {"download.default_directory": downloads}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=chrome_options)
            return driver
        elif browser == "chromeR":
            # 分布式
            sys.stderr.write(nodes[x])
            # 设置浏览器默认下载路径
            prefs = {"download.default_directory": downloads}
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')  # 屏蔽HTTPS非信任站点
            chrome_options.add_experimental_option("prefs", prefs)
            driver = Remote(nodes[x], chrome_options.to_capabilities())
            return driver
        elif browser == "chrome":
            # Chrome正常模式
            # 设置浏览器默认下载路径
            # sys.stderr.write("------ 这里是Chrome正常模式 ------\n")
            prefs = {"download.default_directory": downloads}
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')  # 屏蔽HTTPS非信任站点
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=chrome_options)
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "edge":
            driver = webdriver.Edge()
            return driver
        else:
            print("Not found this browser, You can enter 'firefox','chrome','ie' or 'edge'")
    except Exception as msg:
        print("%s" % msg)


def up_files(path):
    """通过自定义方法upfile上传文件
    path为相对路径
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.abspath(os.path.join(base_path, '..\\..'))
    time.sleep(3)
    exec_file = os.path.join(fpath, ".\\Common\\upfile.exe")
    os.system("%s %s" % (exec_file, path))
    time.sleep(2)


def waiting(sec=3):
    time.sleep(sec)


class Operator(object):
    """基于Selenium做二次封装"""

    def __int__(self, driver, *args):
        """
        启动浏览器
        """
        self.driver = driver

    def open(self, url, timeout=20):
        """
        使用get方法打开URL地址，最大化窗口
        """
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))  # 判断打开的URL是否与给出的一致
        except TimeoutException:
            sys.stderr.write("Open %s Fail" % url)
        except Exception as e:
            sys.stderr.write("Error: %s" % e)

    """
    封装点击、输入、上传、获取文字等操作
    """
    def click(self, location):
        """显示等待10秒直到指定对象可点击，重试3次
        location = ("BY.xx", "xxx")
        BY.ID, BY.NAME, BY.CLASS_NAME, BY.XPATH ...
        """
        t = 0
        while t < 3:
            try:
                ele = WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(location))
                ele.click()
            except TimeoutException:
                t += 1
                continue
            else:
                break

        if t == 3:
            sys.stderr.write("retry 3 times, click failed!")

    def send_keys(self, location, text):
        """显示等待10秒输入内容到指定对象，重试3次
        location = ("BY.xx", "xxx")
        BY.ID, BY.NAME, BY.CLASS_NAME, BY.XPATH ...
        """
        t = 0
        while t < 3:
            try:
                ele = WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(location))
                ele.clear()
                ele.send_keys(text)
            except TimeoutException:
                t += 1
                continue
            except Exception as e:
                sys.stderr.write("Error: %s" % e)
                t += 1
                continue
            else:
                break

        if t == 3:
            sys.stderr.write("Retry 3 times, send keys failed!")

    def is_clickable(self, location):
        """判断是否可以点击
        location = ("BY.xx", "xxx")
        BY.ID, BY.NAME, BY.CLASS_NAME, BY.XPATH ...
        """
        t = 0
        while t < 3:
            try:
                res = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(location))
            except Exception as e:
                sys.stderr.write("Error: %s" % e)
                t += 1
                continue
            else:
                return res
        if t == 3:
            sys.stderr.write("retry 3 times, operation failed!")
            return False

    def is_visibility(self, location):
        """判断元素是否存在
        location = ("BY.xx", "xxx")
        BY.ID, BY.NAME, BY.CLASS_NAME, BY.XPATH ...
        """
        t = 0
        while t < 3:
            try:
                res = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location))
            except Exception as e:
                sys.stderr.write("Error: %s" % e)
                t += 1
                continue
            else:
                return res
        if t == 3:
            sys.stderr.write("retry 3 times, find element failed!")
            return False

    def is_invisibility(self, location):
        """判断对象是否不存在"""
        try:
            res = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(location))
        except Exception as e:
            # sys.stderr.write("Find element!")
            return False
        else:
            return res

    def is_selected(self, location):
        """判断对象是否为已选择"""
        try:
            res = WebDriverWait(self.driver, 10).until(EC.element_located_to_be_selected(location))
        except Exception as e:
            # sys.stderr.write("Find element failed!")
            return False
        else:
            return res

    def is_text_in_element(self, location, text):
        """判断text内容是否在内容中"""
        try:
            res = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(location, text))
        except Exception as e:
            return False
        else:
            return res

    def is_text_in_value(self, location, value):
        """判断内容是否在value中"""
        try:
            res = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(location, value))
        except Exception as e:
            return False
        else:
            return res

    def find_element(self, location):
        """查找元素"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location))

    # 获取属性
    def get_text(self, location):
        ele = self.find_element(location)
        return ele.text

    def get_attribute(self, location, text):
        """获取对象指定属性"""
        ele = self.find_element(location)
        return ele.get_attribute(text)

    def js_execute(self, js):
        """执行JS脚本"""
        return self.driver.execute_script(js)

    def select_by_value(self, location, value):
        """下拉菜单选择指定值"""
        ele = self.find_element(location)
        Select(ele).select_by_value(value)

    def select_by_text(self, location, text):
        """下拉菜单选择文字内容"""
        ele = self.find_element(location)
        Select(ele).select_by_visible_text(text)

    def mouse_click(self, location):
        """鼠标点击操作"""
        ele = self.find_element(location)
        ActionChains(self.driver).click(ele).perform()

    def mouse_right_click(self, location):
        """鼠标右键点击"""
        ele = self.find_element(location)
        ActionChains(self.driver).context_click(ele).perform()

    def mouse_double_click(self, location):
        """鼠标双击操作"""
        ele = self.find_element(location)
        ActionChains(self.driver).double_click(ele).perform()

    def switch_to_iframe(self, location):
        """跳转到 iframe"""
        iframe = self.find_element(location)
        self.driver.switch_to.frame(iframe)
