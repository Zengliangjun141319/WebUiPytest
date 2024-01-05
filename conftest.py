# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     conftest.py
   Author :        曾良均
   QQ:             277099728
   Date：          12/5/2023 11:08 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'
import pytest
import allure

driver = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if hasattr(driver, "get_screenshot_as_png"):
            allure.attach(driver.get_screenshot_as_png(), "异常截图", allure.attachment_type.PNG)
