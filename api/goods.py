
import requests


def get_goods_id(session, goodsid):
    """查询商品"""
    url = "http://49.235.92.12:7005/api/v2/goods/%s"%goodsid
    r = session.get(url)
    print("查询结果：%s" % r.text)
    return r


def add_goods(session,
              goodscode="sp_111",
              goodsname="商品_test",
              **kwargs):
    """添加商品"""
    # 添加商品 goodscode
    url = "http://49.235.92.12:7005/api/v2/goods"
    body = {
        "goodsname": goodsname,
        "goodscode": goodscode
    }
    body.update(kwargs)  # 更新关键字参数
    r = session.post(url, json=body)
    print("添加商品返回:%s" % r.text)
    return r

def update_goods(session, goodsid, goodscode="sp_100861112", **kwargs):
    """修改商品"""
    url = "http://49.235.92.12:7005/api/v2/goods/{}".format(goodsid)
    body = {"goodscode": goodscode}
    body.update(kwargs)
    r = session.put(url, json=body)
    print("修改商品返回:", r.text)
    return r


def delete_goods(session, goodsid):
    """删除商品"""
    url = "http://49.235.92.12:7005/api/v2/goods/{}".format(goodsid)



def get_all_goods(session, goodsid):
    """全部商品"""
    pass

if __name__ == '__main__':
    s = requests.session()
    from api.login import login
    login(s)

    # 查询商品
    r = get_goods_id(s, goodsid=12)
    print(r.text)

    add_goods(s,
              goodsname="悠悠测试123",
              goodscode="sp_100861112")
    update_goods(s, goodsid=12, goodscode="sp_1235444444", stock=10)