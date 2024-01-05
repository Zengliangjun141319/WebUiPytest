# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     updateResultToDB.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          3/3/2022 9:35 AM
-------------------------------------------------
   Change Activity:
                   3/3/2022:
-------------------------------------------------
"""
__author__ = 'ljzeng'

from bs4 import BeautifulSoup
import pymssql


def getresult(url, version):
    # 解析html报告文件
    sou = BeautifulSoup(open(url, encoding='utf-8'), features='html.parser')
    starttime = (sou.find('p', class_='attribute').get_text()).split(' ')[1]
    ver = version

    summary = float(sou.find(class_="abstract detail_button").string.split('[')[1][:-1][:-1]) / 100
    passed = int(sou.find(class_="passed detail_button").string.split('[')[1][:-1])
    failed = int(sou.find(class_="failed detail_button").string.split('[')[1][:-1])
    err = int(sou.find(class_="errored detail_button").string.split('[')[1][:-1])
    skiped = int(sou.find(class_="skiped detail_button").string.split('[')[1][:-1])
    all = int(sou.find(class_="all detail_button").string.split('[')[1][:-1])

    sqls = ("insert into Autotestresult(version,runDate,summary,pass,fail,error,skip,total) "
            "values('%s','%s',%f,%d,%d,%d,%d,%d)") % (ver, starttime, summary, passed, failed, err, skiped, all)
    updateSQL('Test', sqls)


def updateSQL(dt, sqlstr, server='192.168.25.214\\fi', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()
    if not cur:
        raise (NameError, "数据库连接失败")

    # if 'delete' or 'update' in sqlstr:
    sqlstr += ";commit"

    try:
        cur.execute(sqlstr)
    except Exception as e:
        print(e.args)
        conn.rollback()

    cur.close()
    conn.close()


if __name__ == "__main__":
    reportfile = r''
    getresult(reportfile, '2.22.302')