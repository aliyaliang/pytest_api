import requests
from api.login import login
import pytest


@pytest.fixture(scope="session")
def login_setup():
    '''前置操作，先登录'''
    print("前置：调用登录")
    s = requests.session()
    login(s)
    return s
