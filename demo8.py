#第三方模块安装与使用
'''win+R:cmd'''
'''pip install schedule'''
import time
import schedule
'''pip install schedule'''

def job():
    print('haha--------------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)