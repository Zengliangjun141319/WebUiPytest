# -*- coding:utf-8 -*-
"""
@author: 曾良均
@file: excel.py
@time: 2017/12/19 13:12
"""

import xlrd
import os
"""
最新版的xlrd不支持读取xlsx，需安装旧版本
#卸载已安装的
pip uninstall xlrd 

#下载对应的版本
pip install xlrd==1.2.0
"""


def open_excel(excelfile):
    u'''读取Excel文件'''
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # print(BASE_DIR)
    BASE_DIR = os.path.join(base_dir, '..\\')
    excelfile = os.path.join(BASE_DIR, excelfile)
    try:
        data = xlrd.open_workbook(excelfile)
        return data
    except Exception as e:
        raise e


def excel_table(excelfile):
    u'''加载数据到List'''
    data = open_excel(excelfile)
    # data = xlrd.open_workbook(excelfile)
    # 通过工作表名称，获取到一个工作表
    table = data.sheet_by_name('Sheet1')
    # table = data.sheet_by_index(0)
    # 获取行数
    Trows = table.nrows
    # 获取第一行数据
    Tcolnames = table.row_values(0)
    # print('第一行数据为： %s ' % Tcolnames)
    lister = []
    for rownumber in range(1, Trows):
        row = table.row_values(rownumber)
        if row:
            app = {}
            for i in range(len(Tcolnames)):
                app[Tcolnames[i]] = row[i]
            lister.append(app)
    return lister


def get_list(excelfile):
    try:
        data_list = excel_table(excelfile)
        assert len(data_list) > 0, u'Excel标签页：' + 'Sheet1' + u'为空'
        return data_list
    except Exception as e:
        raise e


def get_rows(filename):
    xlsdata = xlrd.open_workbook(filename)
    table = xlsdata.sheet_by_name('Sheet1')
    rows = table.nrows
    return rows


def reaExcel(files):
    # 定义一个列表，目的是为了使excel文件中的内容（字符串格式）转为列表数据类型
    data = list()
    # 读取excel文件中的内容
    book = open_excel(files)
    # 由于excel的特性，数据在第一个sheet页里面，这时我们需要去通过读取excel里面的索引来获取数据（如果后续有多个sheet，只需要读取对应sheet下标索引即可）
    sheet = book.sheet_by_index(0)
    # 循环遍历打印出所有数据，这里的“1”表示的是跳过excel文件里面的第一行，有点类似csv文件里面的next(csv.reader(f))
    for item in range(1, sheet.nrows):
        # 将循环打印出的字符串内容追加到列表里面，使其变为列表数据
        data.append(sheet.row_values(item))
    # 最后返回列表数据
    return data


if __name__ == '__main__':
    root = None
    files = r'D:\SVN\IronIntel\Doc\AutoTest\report\Time+Line.xlsx'
    # datas = excel.get_list(files, 'Sheet1')
    # for line in datas:
    #     print(line)
    r = Excels()
    r.get_rows(filename=files)
    print('Rows is : %s ' % r)
