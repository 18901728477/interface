import unittest
import logging

import requests
from parameterized import parameterized

from utils import assesr_common, test_data

from api.login_api import TestLoginApi



class TestIhrmLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = TestLoginApi()

    def tearDown(self):
        pass

    @parameterized.expand(test_data('./data/test_login.json'))
    def test01_login_success(self, data, httpcode, success, code, message):
        jsonData = data
        response = self.login_api.login(jsonData)
        logging.info('登录的结果为:', response.json())
        assesr_common(httpcode, success, code, message, response, self)
    '''
    def test02_mobile_is_not_exists(self):
        jsonData = {"mobile": "13800000009", "password": '123456'}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test03_password_error(self):
        jsonData = {"mobile": "13800000002", "password": '135698'}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test04_mobile_is_empty(self):
        jsonData = {"mobile": "", "password": '123456'}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test05_password_is_empty(self):
        jsonData = {"mobile": "13800000002", "password": ''}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test06_mobile_has_special(self):
        jsonData = {"mobile": "138000000#2", "password": '123456'}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test07_more_parameter(self):
        jsonData = {"mobile": "13800000002", "password": '123456', "more": "123"}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test08_no_password(self):
        jsonData = {"mobile": "13800000002"}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test09_no_mobile(self):
        jsonData = {"password": '123456'}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test10_error_parameter(self):
        jsonData = {"mobileo": "13800000002", "password": '123456'}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test11_no_parameter(self):
        jsonData = {}
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 20001, '用户名或密码错误', response, self)

    def test12_None(self):
        jsonData = None
        response = self.login_api.login(jsonData)
        print(response.json())
        assesr_common(200, False, 99999, '抱歉，系统繁忙，请稍后重试！', response, self)
        '''





