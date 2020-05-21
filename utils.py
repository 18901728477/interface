def assesr_common(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertEqual(message, response.json().get('message'))

import json
#  登录模块
def test_data(test_path):
    data_list = []
    with open(test_path, encoding='utf-8') as f:
        data_json = json.load(f)
        for i in data_json.values():
            data_list.append(list(i.values()))
            print(data_list)
    return data_list

# 员工模块
def employee_data(employee_path, name):
    data_list = []
    with open(employee_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        emp_data = jsonData.get(name)
        data_list.append(list(emp_data.values()))
        print(emp_data)
    return data_list
        

