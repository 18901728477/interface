'''
import requests
import unittest
import time

class TestEmployee():
    def __init__(self):
        self.emp_url = 'http://ihrm-test.itheima.net/api/sys/user'

    # 添加员工接口
    def test_employee(self, headers):
        response_manage = requests.post(url=self.emp_url, json={
            "username": "狗子{}".format(time.strftime('%Y%M%d%H%m%S')),
            "mobile": "18588889959{}".format(time.strftime('%Y%M%d%H%m%S')),
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "workNumber": "123488",
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-17T16:00:00.000Z"}, headers=headers)
        return response_manage

    # 查询员工接口
    def employee_check(self, emp_id, headers):
        query_url = self.emp_url + '/' + emp_id
        # 查询员工
        response_check = requests.get(url=query_url, headers=headers)
        return response_check

    # 修改员工接口
    def employee_change(self, emp_id, headers, json):
        # 修改员工
        modify_url = self.emp_url + '/' + emp_id
        response_change = requests.put(url=modify_url, headers=headers,
                                       json=json)
        return response_change

    # 删除员工接口
    def employee_delete(self, emp_id, headers):
        # 删除员工
        delete_url = self.emp_url + '/' + emp_id
        response_delete = requests.delete(url=delete_url, headers=headers)
        return response_delete
        '''
import time

import requests

class EmployeeIhrm():
    def __init__(self):
        self.add_url = 'http://ihrm-test.itheima.net/api/sys/user'

    # 添加员工
    def ihrm_add(self, HEADERS):
        response = requests.post(self.add_url, json={
            "username": "狗子{}".format(time.strftime('%Y%M%d%H%m%S')),
            "mobile": "18588889959{}".format(time.strftime('%Y%M%d%H%m%S')),
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "workNumber": "123488",
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-17T16:00:00.000Z"}, headers=HEADERS)
        return response

    # 查询员工
    def ihrm_search(self, EMP_ID, HEADERS):
        search_url = self.add_url + '/' + EMP_ID
        response = requests.get(url=search_url, headers=HEADERS)
        return response

    # 修改员工
    def ihrm_put(self, EMP_ID, HEADERS, json):
        put_url = self.add_url + '/' + EMP_ID
        response = requests.put(url=put_url, headers=HEADERS, json=json)
        return response

    # 删除员工
    def ihrm_delete(self, EMP_ID, HEADERS):
        delete_url = self.add_url + '/' + EMP_ID
        response = requests.delete(url=delete_url, headers=HEADERS)
        return response
