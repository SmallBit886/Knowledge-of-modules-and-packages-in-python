#python中常用的内置模块
import sys  #与python解释器及其环境草做相关的标准库
import time  #提供与时间相关的各种函数的标准库
import os   #提供了访问操作系统服务功能的标准库
import calendar #提供与日期相关的各种函数的标准库
import urllib.request   #用于读取来自网上（服务器）的数据标准库
import json #用于使用Json序列化和反序列化对象
import re   #用于在字符串中执行正则表达式匹配和替换
import math #提供了标准算术运算函数的库
import decimal  #用于进行精准控制运算精度，有小数位和四舍五入操作的十进制运算
import logging  #提供了灵活的记录事件、错误、警告、和调试信息等日志信息功能

print(sys.getsizeof(24))    #28
print(sys.getsizeof(55))    #28

print(sys.getsizeof(True))  #28
print(sys.getsizeof(False)) #24


print(time.time())  #1695988491.0591471
print(time.localtime()) #time.struct_time(tm_year=2023, tm_mon=9, tm_mday=29, tm_hour=19, tm_min=54, tm_sec=51, tm_wday=4, tm_yday=272, tm_isdst=0)


print(urllib.request.urlopen('http://www.baidu.com').read())    #百度返回的东西读取出来

print(math.pi)  #3.141592653589793
