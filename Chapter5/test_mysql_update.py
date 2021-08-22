# -*- coding:utf-8 -*-
# @Time: 2021/8/22 下午3:48
# @Author: Elvin
import pymysql

def update_table():
    #打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3307,user='root',passwd='111111',db='test_db',charset='utf8')


    #获取游标
    cursor = db.cursor()

    #sql语句
    sql ='xxxx'

    try:
        #执行sql
        cursor.execute(sql)
        #提交到数据库执行
        db.commit()
        print('执行成功')
    except Exception as e:
        print('执行失败：', e)
        #回滚数据
        db.rollback()
    finally:
        #关闭数据库
        db.close()

def main():
    update_table()

if __name__ == '__main__':
    main()
