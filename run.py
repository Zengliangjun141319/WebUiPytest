# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     run.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/4/2023 9:27 AM   
   Description :    这是所有测试用例运行的主函数
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
__author__ = 'ljzeng'
import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"copy environment.properties allure-results\\")
    os.system(r"allure generate -c -o Report\allure-report")
    # os.system(r"allure open Report\allure-report")  # 此命令会打开报告
