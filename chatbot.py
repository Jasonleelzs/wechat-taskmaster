import itchat
from apscheduler.schedulers.background import BackgroundScheduler
from configs import messages, person_threshold_1, person_threshold_2, person_threshold_3, warning_1, warning_2, warning_3
from redis_utils import MyRedis


sched = BackgroundScheduler()
redis_conn = MyRedis()


# 发送信息
def send_msg():
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name='AXE_分监')
    if len(chatrooms) > 0:
        chatroom = chatrooms[0]
        notice = ''
        for k, v in messages.items():
            notice = notice + v + '\n'
        notice = notice + '都给我抓紧点！'
        chatroom.send(notice)


# 吹水统计
def send_rank():
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name='AXE_分监')
    if len(chatrooms) > 0:
        chatroom = chatrooms[0]
        notice = ''
        for k, v in messages.items():
            notice = notice + v + '\n'
        notice = notice + '都给我抓紧点！'
        chatroom.send(notice)


def after_login():
    sched.add_job(send_msg, 'cron', hour='*/6')
    sched.add_job(send_rank, 'cron', hour=23)
    sched.start()


def after_logout():
    sched.shutdown()


# 处理群聊消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    chatroom_id = msg['FromUserName']
    # if chatroom_id == '@@82f7a5fc6c53673573f7737add842f5b3f7632f9f0e02bbcc118fda3d77a4300':
    nickname = msg['ActualNickName']
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name='AXE_分监')
    if len(chatrooms) > 0:
        chatroom = chatrooms[0]
        times = redis_conn.user_add(nickname)
        if times == person_threshold_1:
            chatroom.send(warning_1.format(nickname, times))
        elif times == person_threshold_2:
            chatroom.send(warning_2.format(nickname, times))
        elif times == person_threshold_3:
            chatroom.send(warning_3.format(nickname, times))

        if msg['isAt']:
            # itchat.send('@{}'.format(username), chatroom['UserName'])
            reply = messages.get(nickname, '没事 at 监工？皮痒吗？啪！(抽打)')
            chatroom.send('@{}，{}'.format(nickname, reply))


if __name__ == '__main__':
    itchat.auto_login(hotReload=True, loginCallback=after_login,
                      exitCallback=after_logout)
    itchat.run()
