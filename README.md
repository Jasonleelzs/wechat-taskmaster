### 微信机器人如何一直在线
1. 机器人账号要保持在线
2. 机器人微信号不能在手机上登出
3. 机器人微信号也不能登录 PC/网页版微信


### 我的需求
1. 每天定时推送消息
2. 每次来了一条信息就统计一下, 信息数目达到了 100 条，就发一张图，信息太多了
3. 统计每人每天的发言量，到达一定数量就 @他，20 次提醒？100 次？每日水量统计
4. 群里的人 at 机器人，机器人会发出他的相关信息，如果有任务的，就发任务 @他，没任务，看你太闲了
5. 根据 @ 剩余字段来 判断回复信息


1，每天早上提醒换岗倒计时
2，关键字查询换岗信息（at 监工，发关键字，有很大发挥空间啊）
3，2整点？


### 案例：
itchat 官方文档 https://itchat.readthedocs.io/zh/latest/
https://www.jianshu.com/p/5d4de51f5375
https://zhuanlan.zhihu.com/p/25445025

https://juejin.im/post/5b61b01f6fb9a04fba6e97ba

https://www.jianshu.com/p/4f5305e220f0

```bash
{
    'MsgId':'3007981554245134657',
    'FromUserName':'@1ee0f8d88e4b33e11907478b46c5d083e9e34ba01829247656ddb180f12659a2',
    'ToUserName':'filehelper',
    'MsgType':1,
    'Content':'ss',
    'Status':3,
    'ImgStatus':1,
    'CreateTime':1559055112,
    'VoiceLength':0,
    'PlayLength':0,
    'FileName':'',
    'FileSize':'',
    'MediaId':'',
    'Url':'',
    'AppMsgType':0,
    'StatusNotifyCode':0,
    'StatusNotifyUserName':'',
    'RecommendInfo':{
        'UserName':'',
        'NickName':'',
        'QQNum':0,
        'Province':'',
        'City':'',
        'Content':'',
        'Signature':'',
        'Alias':'',
        'Scene':0,
        'VerifyFlag':0,
        'AttrStatus':0,
        'Sex':0,
        'Ticket':'',
        'OpCode':0
    },
    'ForwardFlag':0,
    'AppInfo':{
        'AppID':'',
        'Type':0
    },
    'HasProductId':0,
    'Ticket':'',
    'ImgHeight':0,
    'ImgWidth':0,
    'SubMsgType':0,
    'NewMsgId':3007981554245134657,
    'OriContent':'',
    'EncryFileName':'',
    'User':    <User:{
        'UserName':'filehelper',
        'MemberList':        <ContactList:[

        ]        >
    }    >,
    'Type':'Text',
    'Text':'ss'
}

```