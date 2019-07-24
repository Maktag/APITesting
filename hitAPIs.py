import requests
import json


class APIs:

    def __init__(self, base_url, req_route, req_m, req_payload, req_header):
        self.base_url = base_url
        self.req_route = req_route
        self.req_m = req_m
        self.req_payload = req_payload
        self.req_header = req_header

    def hit_api(self):
        request_method = self.req_m.upper()
        request_url = self.base_url+self.req_route
        request_data = self.req_payload
        request_header = self.req_header

        if request_method == 'GET':
            req = requests.get(request_url, params=request_data, headers=request_header)
        elif request_method == 'POST':
            req = requests.post(request_url, data=request_data, headers=request_header)
        elif request_method == 'PUT':
            req = requests.put(request_url, data=request_data, headers=request_header)
        elif request_method == 'DELETE':
            req = requests.delete(request_url+'/'+request_data, headers=request_header)
        elif request_method == 'PATCH':
            req = requests.patch(request_url, data=json.dumps(request_data), headers=request_header)
        return req

    def req_status_code(self):
        try:
            return self.hit_api().status_code
        except Exception as exp:
            print(exp)

    def req_session(self):
        try:
            return self.hit_api().json()['session']
        except Exception:
            return False

    def req_json(self):
        return self.hit_api().json()
