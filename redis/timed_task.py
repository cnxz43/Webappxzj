# -*- coding: utf-8 -*-
import redis
import time
def sent_massage(channel, seq):
    conn = redis.StrictRedis()
    conn.set(channel, seq)


def expire_massage(channel, time):
    conn = redis.StrictRedis()
    conn.expire(channel, time)
    #conn.expireat()

def get_massage(channel):
    conn = redis.StrictRedis()
    print("from {channel} get massage:{massage}"
          .format(channel= channel, massage=conn.get(channel).decode('utf-8')))

def timed_task_set(value, publish_localtime):
    # 利用任务到达time生成一个key
    now = time.time()
    now_local = time.localtime()
    print(now,"|",publish_localtime)

    #publish_localtime = "2018-10-24 18:00:00"
    # 转换成时间数组
    timeArray = time.strptime(publish_localtime, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)

    time_span = timestamp-now
    time_span = int(time_span)

    if time_span >= 0:
        conn = redis.StrictRedis()
        key = str(now)
        key_expire = str(now) + '_e'
        conn.set(key, value)
        conn.set(key_expire, 'expire')
        conn.expire(key_expire,time_span)
        # conn.get(key)
        return True
    else:
        return False

def timed_task_listen():
    conn = redis.StrictRedis()
    ps = conn.pubsub()
    ps.subscribe(["__keyevent@0__:expired"])  # 从foo，bar 订阅消息
    for item in ps.listen():  # 监听状态：有消息发布了就拿过来
        if item['type'] == 'message':
            #print(item['channel'])
            # print(item['data'].decode('utf-8'))
            key_expire = item['data'].decode('utf-8')
            # print(type(key_expire))
            key = key_expire[:-2]
            # print(key)
            print(conn.get(key))


if __name__=="__main__":


    print(timed_task_set("123","2018-10-24 17:49:50"))

    # operation = input("operation:")
    # while operation != ":q":
    #     key = input("key:")
    #     value = input("value:")
    #     if operation == "set":
    #         sent_massage(key,value)
    #     elif operation == "get":
    #         get_massage(key)
    #     elif operation == "expire":
    #         expire_massage(key, value)
    #     operation = input("operation:")


