import requests
from common.connect_mysql import DbConnet, dbinfo
import pytest


@pytest.fixture(scope="function")
def delete_register():
    '''前置操作：删除注册的账号'''
    db = DbConnet(dbinfo)
    sql = "DELETE from auth_user WHERE username='test_yoyox';"
    db.execute(sql)
    db.close()



def test_register(delete_register):
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
        "username": "test_yoyox",
        "password": "123456"
    }
    r = requests.post(url, json=body)
    print(r.text)
    assert r.json()["code"] == 0

def test_register_2(delete_register):
    '''重复注册。提示已注册'''
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
        "username": "test_yoyox",
        "password": "123456"
    }
    r1 = requests.post(url, json=body)
    print(r1.text)
    assert r1.json()["code"] == 0  # 第1次注册成功

    # 第二次注册
    r2 = requests.post(url, json=body)
    print(r2.json())
    assert r2.json()["code"] == 2000  # 第2次注册成功
    assert "用户已被注册" in r2.json()["msg"]