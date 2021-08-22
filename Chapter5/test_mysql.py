# -*- coding:utf-8 -*-
# @Time: 2021/8/21 下午3:37
# @Author: Elvin
import pymysql
con = pymysql.connect(host='127.0.0.1', port=3307,user='root',passwd='11111',db='test_db',charset='utf8')
#创建游标
cursor = con.cursor()
#执行语句
cursor.execute('insert into Persons(PersonID,LastName,FirstName,Address,City) values("101","YANG","ming","shanghai","putdong")')

r=cursor.execute('insert into Persons(PersonID,LastName,FirstName,Address,City) values("101","YANG","ming","shanghai","putdong")')
print(r) #r表示受影响的行数

input_data = input('添加的数据是：')
rc = cursor.execute('insert into School(id) values (%s)', input_data) #参数传递 单条数据

#多条数据使用元组、列表传数据
rc = cursor.execute('insert into School(id,age,leve) values (%s,%s,%s)', (1,20,'高中'))

#插入多条数据
list_data = [(2,18,'初中'),
             (3,30,'大学'),
             (4,8,'小学')]
rc = cursor.executemany('insert into School(id,age,leve) values (%s,%s,%s)', list_data)

#更新
rc = cursor.execute('update School set age = %s where id = %s',('100',4))

#删除
rc = cursor.execute('delete from School where id = %s',('100',))

#查询 不需要commit()
rc = cursor.execute('select * from School')
res = cursor.fetchall() #全部数据
res = cursor.fetchone()#取第一条数据，执行多次按指针顺序从内存中取
res = cursor.fetchmany(2)#取第几条数据
res = cursor.scroll(1,'relative')#相对当前位置移动
res = cursor.scroll(2,'absolute')#相对绝对位置移动
print(res)

#sql 注入
sql = 'select username, password from user where username="%s" and password="%s"'
sql = sql % ('WANG or 1=1 -- ', 123) #由于--是sql的注释，不管输入任何数据都可以直接登录，注释内容后加空格

#获取最新的自增id
user_id=cursor.lastrowid

#设置游标的数据类型
con.cursor(cursor=pymysql.cursors.DictCursor)#设置成为字典类型

#提交
con.commit()

#关闭游标
cursor.close()

#关闭连接
con.close()

#回滚
con.rollback()
#rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

#使用给定的名称和参数调用已命名的数据库程序
cursor.callproc()

#调至下一个可用的结果集
cursor.nextset()

#未参数预先定义内存区域
cursor.setinputsizes()

#为获取大数据值设定缓冲区尺寸
cursor.setoutputsizes()

'''
Warning:当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
Error:警告以外所有其他错误类。必须是 StandardError 的子类。
InterfaceError:当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
DatabaseError:和数据库有关的错误发生时触发。 必须是Error的子类。
DataError:当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
OperationalError:指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
IntegrityError:完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
InternalError:数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
ProgrammingError:程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
NotSupportedError:不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
'''