import os
import shutil
from shutil import copyfile
from replib.config import Config as r_info
import time

from replib.createHtml import Prepare_report
from replib.module_page_creation import module_page_create


class Status:

    version = None
    module_name = None
    and_driver = None

    def __init__(self, test_script_version):
        self.version = test_script_version
        if not os.path.exists('../test_report'):
            os.makedirs('../test_report')
        if not os.path.exists('../test_report/'+self.version):
            os.makedirs('../test_report/'+self.version)
        if not os.path.exists('../test_report/'+self.version+'/index.html'):
            html_file = open('../test_report/'+self.version+'/index.html', 'w')
            html_file.close()
        try:
            copyfile(os.path.abspath("replib/mt.css"), '../test_report/mt.css')
        except Exception as exp:
            print(exp)

    test_unit = {}
    time_stamp = []
    list_of_test_unit = {}
    test_case_with_result = {}
    status_percentage = {}
    passCases = []
    failCases = []
    errorCases = []
    skipCases = []
    infoCases = []
    final_elements = []
    all_pages = []

    def start_module(self, module_name):
        self.module_name = module_name

        if os.path.exists('../test_report/'+self.version+'/' + module_name.replace(' ', '')):
            try:
                shutil.rmtree('../test_report/'+self.version+'/' + module_name.replace(' ', ''))
            except Exception as Exc:
                print(Exc)
            os.makedirs('../test_report/' + self.version+'/' + module_name.replace(' ', ''))
        elif not os.path.exists('../test_report/'+self.version+'/' + module_name.replace(' ', '')):
            os.makedirs('../test_report/' + self.version+'/' + module_name.replace(' ', ''))
        if not os.path.exists('../test_report/'+self.version+'/' + module_name.replace(' ', '') + '.html'):
            html_file = open('../test_report/'+self.version+'/' + module_name.replace(' ', '') + '.html', 'w')
            html_file.close()
        self.time_stamp.append(time.strftime('%a %Y-%m-%d %H:%M:%S'))

    def pass_test(self, tc_id, tc_Message, *save_screenshot):
        self.passCases.append(tc_id)
        if tc_id not in self.test_case_with_result.keys():
            self.test_case_with_result[tc_id] = tc_Message+'_P'
            for ar in save_screenshot:
                if ar == 'T':
                    try:
                        self.save_screenshot(tc_id)
                    except Exception as exp:
                        print(exp)
        # print('Message after adding status', self.test_case_with_result[tc_id])

    def fail_test(self, tc_id, tc_Message, *save_screenshot):
        self.failCases.append(tc_id)
        self.test_case_with_result[tc_id] = tc_Message+'_F'
        for ar in save_screenshot:
            if ar == 'T':
                self.save_screenshot(tc_id)

    def error_test(self, tc_id, tc_Message, *save_screenshot):
        self.errorCases.append(tc_id)
        if tc_id not in self.test_case_with_result.keys():
            self.test_case_with_result[tc_id] = tc_Message+'_E'
            for ar in save_screenshot:
                if ar == 'T':
                    self.save_screenshot(tc_id)

    def skip_test(self, tc_id, tc_Message, *save_screenshot):
        self.skipCases.append(tc_id)
        if tc_id not in self.test_case_with_result.keys():
            self.test_case_with_result[tc_id] = tc_Message+'_S'
            for ar in save_screenshot:
                if ar == 'T':
                    self.save_screenshot(tc_id)

    def info_test(self, tc_id, tc_Message, *save_screenshot):
        self.infoCases.append(tc_id)
        if tc_id not in self.test_case_with_result.keys():
            self.test_case_with_result[tc_id] = tc_Message+'_I'
            for ar in save_screenshot:
                if ar == 'T':
                    self.save_screenshot(tc_id)

    def end_module(self):
        try:
            self.time_stamp.append(time.strftime('%a %Y-%m-%d %H:%M:%S'))
            self.test_unit['Module_Name'] = self.module_name
            self.test_unit['Test_cases'] = self.test_case_with_result
            self.test_unit['TimeStamp'] = self.time_stamp
            self.create_report(self.test_unit, self.module_name)
            self.test_case_with_result.clear()
        except Exception as ex:
            print(ex)

    def create_report(self, data_of_report, pageName):
        self.all_pages.append(pageName)
        # print(self.all_pages)
        # print(data_of_report)
        module_page_create(data_of_report,pageName,self.version, self.time_stamp)
        # print(self.time_stamp)
        self.time_stamp.clear()

    def report_end(self):
        self.passCases = [x for x in self.passCases if x not in self.failCases]
        totalTc = len(self.passCases)+len(self.failCases)+len(self.errorCases)+len(self.skipCases)+len(self.infoCases)
        passPer = (len(self.passCases) * 100) / totalTc
        failPer = (len(self.failCases) * 100) / totalTc
        errorPer = (len(self.errorCases) * 100) / totalTc
        skipPer = (len(self.skipCases) * 100) / totalTc
        infoPer = (len(self.infoCases) * 100) / totalTc
        self.final_elements.append(str(round(passPer,2)))
        self.final_elements.append(str(round(failPer, 2)))
        self.final_elements.append(str(round(errorPer, 2)))
        self.final_elements.append(str(round(skipPer, 2)))
        self.final_elements.append(str(round(infoPer, 2)))
        self.final_elements.append(self.version)
        self.final_elements.append(r_info.org_name)
        self.final_elements.append(r_info.Project_name)
        self.final_elements.append(r_info.User_name)
        self.final_elements.append(r_info.Scripting_team)
        self.final_elements.append(r_info.DateOfExe_name)
        self.final_elements.append(r_info.Testing_env)
        self.final_elements.append(r_info.Operating_system)
        self.final_elements.append(r_info.Python_version)
        self.final_elements.append(r_info.Org_logo_url)
        Prepare_report(self.final_elements, self.time_stamp, self.all_pages)

    def save_screenshot(self, tc_id):
        try:
            self.and_driver.get_screenshot_as_file('../test_report/' + self.version + '/' + self.module_name.replace(' ', '')
                                               + '/' + tc_id + '.png')
        except Exception as exp:
            print(exp)
        # ImageGrab.grab_to_file('../test_report/'+self.version+'/' + self.module_name.replace(' ', '')+'/'+tc_id+'.png')
