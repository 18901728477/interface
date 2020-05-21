import requests
import time


class DepartApi():
    def __init__(self):
        self.ihrm_url = 'http://ihrm-test.itheima.net'
        self.add_url = self.ihrm_url + '/api/company/department'

    def add_depart(self, headers):
        response = requests.post(url=self.add_url, headers=headers,
                                 json={"name": "测试部{}".format(time.strftime('%Y%M%d%H%m%S')), "code": "003",
                                       "manager": "王昭君", "introduce": "貂蝉", "pid": ""})
        return response

    def search_depart(self, depart_id, headers):
        search_url = self.add_url + '/' + depart_id
        response = requests.get(url=search_url, headers=headers)
        return response

    def change_depart(self, depart_id, headers, jsondata):
        change_url = self.add_url + '/' + depart_id
        response = requests.put(url=change_url, headers=headers, json=jsondata)
        return response

    def delete_depart(self, depart_id, headers):
        delete_url = self.add_url + "/" + depart_id
        response = requests.delete(url=delete_url, headers=headers)
        return response
