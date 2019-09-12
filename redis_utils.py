import redis
from configs import redis_config, person_threshold


class MyRedis:
    def __init__(self):
        pool = redis.ConnectionPool(**redis_config)
        self.r = redis.StrictRedis(connection_pool=pool)

    def user_add(self, nickname):
        # 时间, face_id
        user_prefix = 'user_{}'
        key = user_prefix.format(nickname)
        times = self.r.hincrby(key, 'times', amount=1)
        if times == 1:
            self.r.expire(key, time=86400)
        return times

    def hash_get(self, face_id):
        user_prefix = 'user_{}'
        key = user_prefix.format(face_id)
        times = self.r.hget(key, 'frequency')
        return times

    def judge_expire(self, nickname, timestamp, expired):
        expire_prefix = 'today_voice_{}'
        key = expire_prefix.format(nickname)
        result = self.r.set(key, timestamp, ex=expired, nx=True)
        # 如果是 None，就是没过期，不推送，返回 false
        return result


if __name__ == '__main__':
    conn = MyRedis()
    conn.user_add('adsads')
