import itchat
from apscheduler.schedulers.blocking import BlockingScheduler
import time


# 发送信息
def send_msg():
    # user_info = itchat.search_friends(name='故园无此声')
    # if len(user_info) > 0:
    #     user_name = user_info[0]['UserName']
    #     itchat.send_msg('生日快乐哦！', toUserName=user_name)
    print('asasd')


def after_login():
    sched.add_job(send_msg, 'cron', second='*/5')
    sched.start()


def after_logout():
    sched.shutdown()


if __name__ == '__main__':
    sched = BlockingScheduler()
    itchat.auto_login(loginCallback=after_login)
    # itchat.run()
    # after_login()

