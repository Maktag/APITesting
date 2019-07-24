from replib.status import Status
from replib.config import Config
from readCSV import ReadCSV
from hitAPIs import APIs
import jsbeautifier
import json


class ApiTesting:

    session = ''

    st = Status(Config.Script_version)

    def test_1(self):
        print('Testing is starting.')
        self.st.start_module('HH')

    def test_2(self):
        readcsv_obj = ReadCSV(Config.APIListFile, Config.BaseUrl)
        obj = readcsv_obj.file_obj()
        for rows in range(readcsv_obj.get_rows_len()):
            api_id = obj.values[rows][0]
            api_method = obj.values[rows][1]
            api_route = obj.values[rows][2]
            try:
                api_payload = json.loads(obj.values[rows][3])
            except:
                api_payload = str(obj.values[rows][3])
            api_header = json.loads(obj.values[rows][4])
            api_expected_status_code = obj.values[rows][5]
            api_session = obj.values[rows][6]
            about_api = obj.values[rows][7]
            print('-----------*-----------*-----------*-----------*-----------*-----------*-----------*-----------')
            try:
                api_header["session"] = self.session
            except:
                pass
            service_call = APIs(readcsv_obj.baseURL, api_route, api_method, api_payload, api_header)
            api_actual_status_code = service_call.req_status_code()
            if api_actual_status_code is api_expected_status_code:
                res = jsbeautifier.beautify(json.dumps(service_call.req_json()))
                self.st.pass_test(api_id, about_api+"<div style=' color: #c2fe59;  border-left: 6px solid #c2fe59;"
                                                    "background-color: black;'><h5>Response:"
                                                    "</h5><xmp>"+res+"</xmp></div>", False)
                if api_session == 'Yes':
                    self.session = service_call.req_session()
            else:
                self.st.fail_test(api_id, about_api+"<h5>Response:</h5><xmp>"+res+"</xmp>", False)

    def test_3(self):
        self.st.end_module()
        self.st.report_end()


if __name__ == '__main__':
    ApiTesting().test_1()
    ApiTesting().test_2()
    ApiTesting().test_3()