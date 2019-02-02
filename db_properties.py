# -*- coding: utf-8 -*-

class Properties:
    """
    数据库配置文件，保存数据库连接信息等，可以方便修改配置
    """

    # 当前要连接的数据库
    db = 'testdb'   # test

    # 接口返回数据库连接信息
    def get_db_config(self):
        databases = {
            'testdb': {
                'host': 'localhost',
                'user': '****',
                'password': '****',
                'database': '****',
                'port': 3306,
            },
        }
        return databases[self.db]
