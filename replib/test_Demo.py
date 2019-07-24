import pytest
from replib.status import Status
from replib.config import Config

class TestSuit:

    Config.Script_version = "AppTest_11.45.9"
    Config.org_name = "MakTag"
    Config.Project_name = "AppTest"
    Config.User_name = "U@testapp"
    Config.Scripting_team = "QA_team_1"
    Config.Testing_env = "UAT_2"
    Config.Operating_system = "macOS 10.14.3"
    Config.Python_version = "Python3"
    Config.Org_logo_url = "../../maktag_1024.png"

    st = Status(Config.Script_version)


    # @pytest.mark.order1
    # def test_1(self):
    #     self.st.start_module('Login With Facebook')
    #     self.st.pass_test('001', 'Login is working fine with the FB.', 'T')
    #     self.st.fail_test('002', 'Loging with fb is not working fine.', 'T')
    #     self.st.skip_test('004', 'Loging with fb is not working fine.', 'T')
    #     self.st.error_test('005', 'Loging with fb is not working fine.', 'T')
    #     self.st.info_test('006', 'Loging with fb is not working fine.', 'T')
    #     self.st.pass_test('007', 'Login is working fine with the FB.', 'T')
    #     self.st.fail_test('008', 'Loging with fb is not working fine.', 'T')
    #     self.st.skip_test('009', 'Loging with fb is not working fine.', 'T')
    #     self.st.error_test('010', 'Loging with fb is not working fine.', 'T')

    # @pytest.mark.order2
    # def test_2(self):
    #     time.sleep(2)
    #     self.st.end_module()

    # @pytest.mark.order3
    # def test_3(self):
    #     time.sleep(2)
    #     self.st.start_module('Login With Twitter')
    #     self.st.pass_test('001', 'Loging with tw is working fine.')
    #     self.st.pass_test('002', 'Loging with tw is working fine.')
    #     self.st.pass_test('003', 'Loging with tw is working fine.')
    #     self.st.pass_test('004', 'Loging with tw is working fine.')
    #     self.st.pass_test('005', 'Loging with tw is working fine.')
    #     time.sleep(2)

    @pytest.mark.order2
    def test_4(self):
        self.st.end_module()
        self.st.report_end()
