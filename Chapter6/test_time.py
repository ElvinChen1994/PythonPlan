# -*- coding:utf-8 -*-
# @Time: 2021/8/24 下午11:31
# @Author: Elvin

import time

time_expamle = time.time()
print("当前时间戳：",time_expamle)

lcoaltime = time.localtime(time.time())
print("本地时间：",lcoaltime)

#可读时间
localtime = time.asctime(time.localtime(time.time()))
print("本地时间：",localtime)

#格式化时间:2021-08-24 23:47:25
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#Tue Aug 24 23:48:57 2021
print(time.strftime("%a %b %d %H:%M:%S %Y"),time.localtime())

#字符串转换成时间戳
a = 'Tue Aug 24 23:50:28 2021'
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


from datetime import datetime

#获取当前时间2021-08-24 23:59:46.351950
now_time = datetime.now()
print(now_time)

#设置指定的时间
set_time = datetime(2021,5,19,13,22)
print(set_time)

#转换时间戳
ts = datetime(2021,5,19,13,22)
ts_time = ts.timestamp()
print(ts_time)

#时间戳转换成具体时间
t = 1621401720.0
print(datetime.fromtimestamp(t))

#字符串转datetime
one = datetime.strptime('2021-6-12 20:20:20', '%Y-%m-%d %H:%M:%S')
print(one)

#datetime转str
now_time = datetime.now()
print(now_time.strftime('%a, %b %d %H:%M'))

#时间加减，主要是把当前时间前后计算
from datetime import datetime, timedelta, timezone

now_time = datetime.now()
print(now_time)
print(now_time+timedelta(hours=2))
print(now_time-timedelta(hours=1))

#创建时区
time_utc_8 = timezone(timedelta(hours=8))
print(time_utc_8)
now = datetime.now()
print(now)

#强制设置utc+8
rt = now.replace(tzinfo=time_utc_8)
print(rt)

#强制设置时区+utc0:00
utc_rt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_rt)

#将其转换成北京时间
bei_time = utc_rt.astimezone(timezone(timedelta(hours=8)))
print(bei_time)

