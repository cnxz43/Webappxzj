#!/usr/bin/env python
#-*- coding:utf-8 -*-

#### redis 发布和订阅  #####
import redis

class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.StrictRedis(host='localhost',port=6379)#连接Redis
        self.channel = 'monitor' #定义名称

    def publish(self,msg):#定义发布方法
        self.__conn.publish(self.channel,msg)
        return True

    def subscribe(self):#定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub

def book_channel():
    # 订阅
    # from test_redis2 import RedisHelper
    obj2 = RedisHelper()
    redis_sub = obj2.subscribe()  # 调用订阅方法
    while True:
        msg = redis_sub.parse_response()
        print(msg)

def publish_channel(massage):
    # 发布
    obj1 = RedisHelper()
    obj1.publish(massage)


if __name__ == "__main__":
    # 发布
    obj1 = RedisHelper()
    str_ = input("input:")
    while str_ != 'quit!':
        obj1.publish(str_)
        str_ = input("input:")


