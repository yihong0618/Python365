## 第一天
### 索引
- Python标准库--time
- Python好的文章--[Python之路](https://blog.laisky.com/p/python-road/)
- [Python代码片段--asyncio](day1.py)
- Python读书--[Django企业开发实战day1](http://product.dangdang.com/26509799.html)
- Python项目相关--[funNLP](https://github.com/fighting41love/funNLP)
- Python之外--[大型互联网公司分布式ID方案总结](https://juejin.im/post/5d6fc8eff265da03ef7a324b?utm_source=gold_browser_extension)
---
### 标准库 [time](https://pymotw.com/3/time/index.html)
1. time.get_clock_info(name)
2. time.time()
3. time.monotime() # 系统时间外更精确的时间
4. time.process_time()
5. time.perf_counter() && time.ctime()
```python
import hashlib
import time

# Data to use to calculate md5 checksums
data = open(__file__, 'rb').read()

loop_start = time.perf_counter()

for i in range(5):
    iter_start = time.perf_counter()
    h = hashlib.sha1()
    for i in range(300000):
        h.update(data)
    cksum = h.digest()
    now = time.perf_counter()
    loop_elapsed = now - loop_start
    iter_elapsed = now - iter_start
    print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
        iter_elapsed, loop_elapsed))
```
6.time.gmtime() && time.localtime()
```python
import time
# gmttime <-- UTC time

def show_struct(s):
    print('  tm_year :', s.tm_year)
    print('  tm_mon  :', s.tm_mon)
    print('  tm_mday :', s.tm_mday)
    print('  tm_hour :', s.tm_hour)
    print('  tm_min  :', s.tm_min)
    print('  tm_sec  :', s.tm_sec)
    print('  tm_wday :', s.tm_wday)
    print('  tm_yday :', s.tm_yday)
    print('  tm_isdst:', s.tm_isdst)


print('gmtime:')
show_struct(time.gmtime())
print('\nlocaltime:')
show_struct(time.localtime())
print('\nmktime:', time.mktime(time.localtime()))
```
7. time.tzset()
```python
# To change the time zone, set the environment variable TZ, then call tzset().
import time
import os


def show_zone_info():
    print('  TZ    :', os.environ.get('TZ', '(not set)'))
    print('  tzname:', time.tzname)
    print('  Zone  : {} ({})'.format(
        time.timezone, (time.timezone / 3600)))
    print('  DST   :', time.daylight)
    print('  Time  :', time.ctime())
    print()


print('Default :')
show_zone_info()

ZONES = [
    'GMT',
    'Europe/Amsterdam',
]

for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ':')
    show_zone_info()
```
8. Parsing and Formatting Times
```python
import time


def show_struct(s):
    print('  tm_year :', s.tm_year)
    print('  tm_mon  :', s.tm_mon)
    print('  tm_mday :', s.tm_mday)
    print('  tm_hour :', s.tm_hour)
    print('  tm_min  :', s.tm_min)
    print('  tm_sec  :', s.tm_sec)
    print('  tm_wday :', s.tm_wday)
    print('  tm_yday :', s.tm_yday)
    print('  tm_isdst:', s.tm_isdst)


now = time.ctime(1483391847.433716)
print('Now:', now)

parsed = time.strptime(now)
print('\nParsed:')
show_struct(parsed)

print('\nFormatted:',
      time.strftime("%a %b %d %H:%M:%S %Y", parsed))
```
### [Python代码片段](day1.py)
注： 代码来自[深入理解asyncio(一)](https://www.dongwm.com/post/understand-asyncio-1/)
- 协程要用 async def 声明，Python 3.5 时的装饰器写法已经过时，我就不列出来了。
- asyncio.gather 用来并发运行任务，在这里表示协同的执行 a 和 b2 个协程
- asyncio.run 是 Python 3.7 新加的接口，要不然你得这么写:
```python
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```
### 错误的并发用法
```python

async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')


async def s1():
    await a()
    await b()

## 正确的用法 1.
## async def c1():
##     await asyncio.gather(a(), b())

## 正确的用法 2.
## async def c2():
##    await asyncio.wait([a(), b()])
```
