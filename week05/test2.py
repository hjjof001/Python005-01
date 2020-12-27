import string
from functools import wraps
import time

import redis

r = redis.Redis(host='***.***.***.***', port=6379, password='***')


def send_times(times):
    def decorate(func):
        @wraps(func)
        def wrapper(telephone_number: int, content: string, **kwargs):
            con_len = len(content)
            if con_len < 70:
                if r.llen(telephone_number) < times:
                    func(telephone_number, content, **kwargs)
                elif check(telephone_number, False):
                    func(telephone_number, content, **kwargs)
                else:
                    print(f'失败{telephone_number},操作频繁，1 分钟后重试')
            else:
                if r.llen(telephone_number) < times - 1:
                    func(telephone_number, content[:con_len >> 2])
                    func(telephone_number, content[con_len >> 2:])
                elif check(telephone_number, True):
                    func(telephone_number, content[:con_len >> 2])
                    func(telephone_number, content[con_len >> 2:])
                else:
                    print(f'失败{telephone_number},超过70字符，剩余次数不足，稍后再试！')
        return wrapper
    return decorate


@send_times(times=5)
def send_sms(telephone_number: int, content: string, key=None):
    r.rpush(telephone_number, int(time.time()))
    print(f'发送{telephone_number}: {content}')


def check(telephone_number, double):
    result = 0
    while result < 5:
        last = int(r.lpop(telephone_number))
        now = int(time.time())
        if now - last > 60:
            result += 1
            continue
        else:
            r.lpush(telephone_number, last)
            break
    return result > 0 if not double else result > 1


if __name__ == '__main__':
    for i in range(6):
        send_sms(12345654321, 'hello')
    time.sleep(2)
    send_sms(88887777666, 'hello')
    send_sms(12345654321, 'hello')
    send_sms(88887777666, 'hello')
