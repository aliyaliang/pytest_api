import pymysql

# 配置信息
dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309,
    "database": "apps"}


class DbConnet():

    def __init__(self, dbinfo):
        self.db = pymysql.connect(
                        cursorclass=pymysql.cursors.DictCursor,
                        **dbinfo,
                             )

        self.cursor = self.db.cursor()

    def select(self, sql):
        '''查询'''
        # 写SQL
        # sql = "SELECT * from apiapp_goods"
        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        # print(result)
        return result

    def execute(self, sql2):
        '''执行删除，修改，新增'''
        # 修改数据
        # sql2 = 'UPDATE apiapp_goods set goodsname="《selenium 入门到精通234》" WHERE id=12;'
        try:
            self.cursor.execute(sql2)
            self.db.commit()
        except:
            # 捕获异常 回滚
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    db = DbConnet(dbinfo)
    sql1 = "SELECT * from apiapp_goods"
    result = db.select(sql1)
    print(result)
    sql2 = 'UPDATE apiapp_goods set goodsname="《selenium 入门到精通》" WHERE id=12;'
    db.execute(sql2)
    db.close()  # 关闭连接