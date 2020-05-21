import time
import unittest

import HTMLTestRunner_PY3

from script.test_ihrm_depart import TestDepart
from script.test_ihrm_employee import TestEmployee
from script.test_ihrm_login import TestIhrmLogin

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestIhrmLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
suite.addTest(unittest.makeSuite(TestDepart))

# 定义测试报告路径
resport_name = './report/ihrm.html'

with open(resport_name, 'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=2, title='IHRM接口测试报告', description='这是日历资源管理系统')
    runner.run(suite)