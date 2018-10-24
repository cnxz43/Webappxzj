# -*- coding: utf-8 -*-
import redis

def timed_task_get():
    conn = redis.StrictRedis()
    ps = conn.pubsub()
    ps.subscribe(["__keyevent@0__:expired"])  # 从foo，bar 订阅消息
    for item in ps.listen():  # 监听状态：有消息发布了就拿过来
        if item['type'] == 'message':
            #print(item['channel'])
            print(item['data'].decode('utf-8'))
            key_expire = item['data'].decode('utf-8')
            print(type(key_expire))
            key = key_expire[:-2]
            print(key)
            print(conn.get(key))
if __name__=="__main__":
    # conn = redis.StrictRedis()
    # massage = conn.get("test3")
    # while True :
    #     if massage != None:
    #         print("expired:", conn.get("__keyevent@0__:expired"))
    #         print("test3:", massage)
    #     massage = conn.get("test3")

    timed_task_get()

