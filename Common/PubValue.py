# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PubValue.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/19/2023 9:13 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   用于存储变量，并支持取出变量值
-------------------------------------------------
"""
__author__ = 'ljzeng'
import sys


class PubValue(object):
    def __init__(self, values):
        #  以 __开头的属性为私有属性，不允许外部访问
        self.__value = values

    def getvalue(self):
        return self.__value

    def setvalue(self, value):
        if value:
            self.__value = value
            # sys.stderr.write('value: %s set completed\n' % value)
        else:
            sys.stderr.write('Error: Value can not null')


if __name__ == '__main__':
    var = PubValue(None)
    var.setvalue('AAC')
    print(var.getvalue())
