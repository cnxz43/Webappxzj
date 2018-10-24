#!/bin/python
import redis

def sent_massage(seq):
    conn = redis.Redis()
    # conn.hset('jack', 'sex', 'm')
    # conn.hset('jack', 'score', 90)
    # print (conn.hgetall('jack'))

    conn.set("test1","success!")
    conn.set("test2",seq)
    print("from sent massage",conn.get("test1"))

def get_massage():
    conn = redis.Redis()
    print("from get massage",conn.get("test3"),type(conn.get("test3")))

if __name__=="__main__":
    seq = input("输入消息：")
    sent_massage(seq)
    type(get_massage())
