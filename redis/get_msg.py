# 订阅
from test_redis2 import RedisHelper
obj2 = RedisHelper()
redis_sub = obj2.subscribe()  # 调用订阅方法

while True:
    msg = redis_sub.parse_response()
    print(msg)