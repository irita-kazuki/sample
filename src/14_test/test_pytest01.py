import pytest

import test_01

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal = test_01.Cal()

    @classmethod
    def teardown_class(cls):
        print("end")
        del cls.cal

    def setup_method(self, method):
        print("method = {}".format(method.__name__))

    def teardown_method(self, method):
        print("method = {}".format(method.__name__))

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4
    
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1", 1)

    @pytest.mark.skipif(True, reason="skip!")        
    def test_add_num_and_double_raise2(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1", "1")

    def test_conftest(self, request):
        os_name = request.config.getoption("--os-name")
        if os_name == "mac":
            print("ls")
        elif os_name == "windows":
            print("dir")

    def test_csv_file(self, csv_file):
        print(csv_file)