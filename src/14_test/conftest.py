import os
import pytest

def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")

@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir,"test.csv"), "w+") as c:
        print("before test")
        yield c
        print("after test")