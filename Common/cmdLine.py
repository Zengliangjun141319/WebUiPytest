# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cmdLine.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/18/2022 9:04 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import os
import time
import sys


def restartService(node='192.168.25.210', servicename='FleetService_V2'):
    # 重启服务
    ex = 'Method execution successful.'
    err = 'No Instance(s) Available.'
    s = os.popen('wmic /node:%s /user:soft\demo /password:Soft.rz SERVICE where name="%s" call stopservice' % (node, servicename))
    sres = s.read()
    s.close()
    time.sleep(3)

    if ex in sres:
        # sys.stdout.write('Service Stop Successfully!')
        tsr = os.popen('wmic /node:%s /user:soft\demo /password:Soft.rz SERVICE where name="%s" call startservice' % (node, servicename))
        ts = tsr.read()
        tsr.close()
        if ex in ts:
            # sys.stdout.write('\nService start successfully!')
            return True
        elif err in ts:
            # sys.stdout.write('Service not exit')
            return False
    elif err in sres:
        # sys.stdout.write('Service not exit')
        return False


def ps(name='win2012devsrv', sname='FleetService_V2'):
    import subprocess
    try:
        res = subprocess.run(["powershell.exe", "Invoke-Command -ComputerName %s -ScriptBlock {Get-Service -Name %s | Restart-Service}" % (name, sname)], stdout=subprocess.PIPE)
    except:
        return False
    else:
        if res.returncode == 0:
            return True


if __name__ == "__main__":
    # restartService()
    # restartService('192.168.25.107', 'FISVCHOST_191126101201')
    ps(sname='foresightpublicservices')


