import requests
import unittest
class TestLoginApi():
    def __init__(self):
        self.login_url = 'http://ihrm-test.itheima.net' + '/api/sys/login'
        self.headers = {"Content-Type": "application/json"}

    def login(self, jsonData):

        response = requests.post(url=self.login_url, headers=self.headers, json=jsonData)
        return response
