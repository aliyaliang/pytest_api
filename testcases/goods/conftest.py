import pytest
from common.connect_mysql import DbConnet, dbinfo



@pytest.fixture(scope="function")
def delete_goods():
    '''前置操作：删除商品'''
    db = DbConnet(dbinfo)
    sql = "DELETE from apiapp_goods WHERE goodscode='sp_10086test'"
    db.execute(sql)
    db.close()