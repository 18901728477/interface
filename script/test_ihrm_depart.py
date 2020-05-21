import logging
import time
import unittest

from api.depart_api import DepartApi
from api.login_api import TestLoginApi
import app
from utils import assesr_common


class TestDepart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = TestLoginApi()
        cls.depart_api = DepartApi()

    def test01_login(self):
        response = self.login.login({"mobile": "13800000002", "password": "123456"})
        token = "Bearer " + response.json().get('data')
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        assesr_common(200, True, 10000, "操作成功！", response, self)
        logging.info("登录成功的信息:", response.json())

    def test02_add(self):
        response1 = self.depart_api.add_depart(app.HEADERS)
        # 获取部门id
        depart_id = response1.json().get('data').get('id')
        app.DEPART_ID = depart_id
        assesr_common(200, True, 10000, "操作成功！", response1, self)
        logging.info("添加部门成功的信息:", response1.json())

    def test03_search(self):
        response2 = self.depart_api.search_depart(app.DEPART_ID, app.HEADERS)
        assesr_common(200, True, 10000, "操作成功！", response2, self)
        logging.info("查询部门的信息:", response2.json())

    def test04_change(self):
        response3 = self.depart_api.change_depart(app.DEPART_ID, app.HEADERS,
                                                  {"name": "狗狗部{}".format(time.strftime('%Y%M%d%H%m%S')),
                                                   "code": "002"})
        assesr_common(200, True, 10000, "操作成功！", response3, self)
        logging.info("修改部门的信息:", response3.json())

    def test05_delete(self):
        response4 = self.depart_api.delete_depart(app.DEPART_ID, app.HEADERS)
        assesr_common(200, True, 10000, "操作成功！", response4, self)
        logging.info("删除部门的信息:", response4.json())
