import datetime


def days_count(year, month, hour):
    point = datetime.datetime(year, month, hour, 0, 0, 0, 000000)
    now = datetime.datetime.now()
    interval_day = point - now
    return interval_day.days


messages = {
    '猫钰钰 五月有砖搬': '距离 猫钰钰 上岗还有 {} 天'.format(days_count(2019, 6, 1)),  # 6.1 上岗
    'AD Zh': '距离 AD Zh 换岗还有 {} 天'.format(days_count(2019, 6, 9)),  # 6.9
    'zzp': '距离 zzp 换岗还有 {} 天'.format(days_count(2019, 9, 1)),  # 9.1
    'cm': '距离 cm 换岗还有 {} 天'.format(days_count(2019, 7, 8)),  # 7.8
    '小皮': '距离 小皮 下岗还有 {} 天'.format(days_count(2019, 7, 15)),  # 7.15
}


group_threshold = 100

person_threshold_1 = 20

person_threshold_2 = 40

person_threshold_3 = 50

warning_1 = '@{}，你今天发言已经到达 {} 次，不好好干活，就知道吹逼！'

warning_2 = '@{}，你今天发言已经到达 {} 次，吹这么多逼，！'

warning_3 = '@{}，你今天发言已经到达 {} 次，你已经无敌了，我已经管不了你了！'


redis_config = {
    'host': '',
    'port': 6379,
    'decode_responses': True,
    'db': 2,
    'password': 1,
}
