'''工作流的测试用例
登录-添加商品（返回商品id) - 修改商品(id)- 查询商品（id)
'''
from api.goods import add_goods, update_goods, get_goods_id
import pytest


@pytest.mark.smoke
def test_goods_flow(login_setup, delete_goods):
    "测试工作流"
    print("step1-添加商品code: sp_10086test")
    r1 = add_goods(session=login_setup, goodscode="sp_10086test", goodsname="悠悠111")
    print("添加商品返回：", r1.text)
    assert r1.json()["code"] == 0

    # 获取商品id
    spid = r1.json()["data"]["id"]
    print("获取商品id:", spid)
    print("step2-更新商品code: sp_10086test goodsname=悠悠111")
    r2 = update_goods(session=login_setup, goodsid=spid, goodscode="sp_10086test", goodsname="悠悠111")
    print("更新商品返回", r2.text)
    assert r2.json()["code"] == 0

    print("step3-查询商品")
    r3 = get_goods_id(session=login_setup, goodsid=spid)
    print(r3.text)
    assert r3.json()["code"] == 0
    assert r3.json()["data"]["goodsname"] == "悠悠111"


