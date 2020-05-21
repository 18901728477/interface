'''
# 导包
import unittest
import logging

import requests
# 创建测试类 ,集成
import time

from api.employee_api import TestEmployee
from api.login_api import TestLoginApi
from utils import assesr_common


class TestIhrmEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_api = TestEmployee()
        self.login = TestLoginApi()

    def tearDown(self):
        pass

    # 实现增加员工函数
    def test01_employee_manage(self):
        # 先登录
        response = self.login.login({"mobile": "13800000002", "password": '123456'})
        print("登录结果为:", logging.info(response.json()))
        assesr_common(200, True, 10000, '操作成功！', response, self)
        # 获取令牌
        lp = 'Bearer ' + response.json().get('data')
        headers = {"Content-Type": "application/json", "Authorization": lp}
        # 添加员工
        response_manage = self.emp_api.test_employee(headers)
        print("添加员工的结果为:", logging.info(response_manage.json()))
        self.assertEqual('操作成功！', response_manage.json().get('message'))

        # 提取员工id
        emp_id = response_manage.json().get('data').get('id')
        # 查询员工
        response_check = self.emp_api.employee_check(emp_id, headers)
        print("查询员工的结果为:", logging.info(response_check.json()))
        self.assertEqual('操作成功！', response_check.json().get('message'))
        # 修改员工
        response_change = self.emp_api.employee_change(emp_id, headers, {"username": "仙女{}".format(time.strftime('%Y%M%d%H%m%S'))})
        print("修改员工的结果为:", logging.info(response_change.json()))
        # 删除员工
        response_delete = self.emp_api.employee_delete(emp_id, headers)
        print("删除员工的结果为:", logging.info(response_delete.json()))
'''
import logging
import time
import unittest

from parameterized import parameterized

import app
from api.employee_api import EmployeeIhrm
from api.login_api import TestLoginApi
from utils import employee_data


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = TestLoginApi()
        cls.ihrm_employee = EmployeeIhrm()

    def tearDown(self):
        pass

    def test01_employee_login(self):
        # 实现登录
        response = self.login.login({"mobile": "13800000002", "password": "123456"})
        # 提取登录的令牌, 并保存到请求头
        token = "Bearer " + response.json().get('data')
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        print(app.HEADERS)
        logging.info('登录后的信息为:', response.json())
        # 添加员工

    def test02_employee_add(self):
        response2 = self.ihrm_employee.ihrm_add(app.HEADERS)
        print("添加员工的响应数据:", response2.json())
        # 提取员工id
        emp_id = response2.json().get('data').get('id')
        app.EMP_ID = emp_id
        logging.info('添加员工的信息为:', response2.json())

        # 查询员工

    def test03_employee_search(self):
        response3 = self.ihrm_employee.ihrm_search(app.EMP_ID, app.HEADERS)
        logging.info('查询员工后的信息为:', response3.json())
        # 修改员工

    def test04_employee_change(self):
        response4 = self.ihrm_employee.ihrm_put(app.EMP_ID, app.HEADERS, {"username": "小仙女{}".format(time.strftime('%Y%M%d%H%m%S'))})
        logging.info("修改员工的响应数据:", response4.json())
        # 删除员工

    def test05_employee_delete(self):
        response5 = self.ihrm_employee.ihrm_delete(app.EMP_ID, app.HEADERS)
        logging.info("删除员工的响应数据:", response5.json())
