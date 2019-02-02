# -*- coding: utf-8 -*-

import pymysql

from packing.db_properties import Properties


class Dao:
    """
    持久化层，提供连接数据库的接口
    """

    def __init__(self):
        # 读取配置文件，返回一个dict，
        # key包括'host', 'user', 'password', 'database', 'port'
        proper = Properties()
        self._db_config = proper.get_db_config()

        # 连接数据库，获得cursor，用于执行sql语句
        self._conn = self.get_connection(self._db_config)
        if self._conn:
            # 传入cursor参数使返回值为dict形式，默认为tuple
            self._cursor = self._conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.close_conn()

    # 连接数据库
    def get_connection(self, db_config):
        conn = False
        try:
            conn = pymysql.connect(host=db_config['host'],
                                      user=db_config['user'],
                                      password=db_config['password'],
                                      db=db_config['database'],
                                      port=db_config['port'])
        except pymysql.Error as e:
            raise e
        else:
            # 返回数据库连接
            return conn

    # 返回全部结果
    def select_all(self, sql):
        result = ""
        print(sql)
        try:
            # 要求传入tuple类型的value
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
        except Exception as e:
            # TODO: 添加异常处理，或log
            raise e
        else:
            return result

    # 返回1条结果
    def select_one(self, sql):
        result = ""
        print(sql)
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchone()
        except Exception as e:
            #
            raise e
        else:
            return result

    # 提交数据更新，包括update、insert、delete
    def exec_data(self, sql):
        flag = False
        print(sql)
        if not (self._conn):
            return flag

        try:
            self._cursor.execute(sql)
            self._conn.commit()
            flag = True
        except Exception as e:
            self._conn.rollback()
            # TODO: 添加异常处理，或log
            raise e
        return flag


    # 关闭连接
    def close_conn(self):
        if self._conn:
            try:
                self._cursor.close()
                self._conn.close()
                print("=========close_conn========")
            except Exception as e:
                # TODO: 添加异常处理，或log
                raise e


if __name__ == "__main__":
    dao = Dao()
    res = dao.select_all("select * from emp where id<20")
    print(res)
    print(type(res))

    # res = dao.exec_data("delete from emp where id=191")
    # print(res)

    # res = dao.exec_data("insert into emp(id, name, address) values(200, '文聘','漯河市')")
    # print(res)

