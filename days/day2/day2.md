## 第二天
### 索引
- Python标准库--datetime
- Python好的文章--[Python WSGI初探](http://liaoph.com/python-wsgi/)
- [Python代码片段--flask-socketio](day2.py)
- Python读书--[Django企业开发实战day2](http://product.dangdang.com/26509799.html)
- Python项目相关--[iredis](https://github.com/laixintao/iredis)
- Python之外--[web前端学习指南](https://github.com/qianguyihao/Web)
---
### python标准库 [datetime](https://pymotw.com/3/datetime/index.html)
1. datetime.time(1, 2, 3)
2. datetime.time.min, datetime.time.max, datetime.time.resolution
3. datetime.time.today()
```python
import datetime

today = datetime.date.today()
print(today)
print('ctime  :', today.ctime())
tt = today.timetuple()
print('tuple  : tm_year  =', tt.tm_year)
print('         tm_mon   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', today.toordinal())
print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)
```
4. datetime.date.fromordinal(), datetime.date.fromtimestamp()
5. datetime.date.min, datetime.date.max, datetime.date.resolution
6. replace
```python

import datetime

d1 = datetime.date(2008, 3, 29)
print('d1:', d1.ctime())

d2 = d1.replace(year=2009)
print('d2:', d2.ctime())
```
7. timedelta
```python
import datetime

print('microseconds:', datetime.timedelta(microseconds=1))
print('milliseconds:', datetime.timedelta(milliseconds=1))
print('seconds     :', datetime.timedelta(seconds=1))
print('minutes     :', datetime.timedelta(minutes=1))
print('hours       :', datetime.timedelta(hours=1))
print('days        :', datetime.timedelta(days=1))
print('weeks       :', datetime.timedelta(weeks=1))
```
8. datetime.date with math
```python
import datetime

one_day = datetime.timedelta(days=1)
print('1 day    :', one_day)test
print('5 days   :', one_day * 5)
print('1.5 days :', one_day * 1.5)
print('1/4 day  :', one_day / 4)

# assume an hour for lunch
work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print('meetings per day :', work_day / meeting_length)
```
9. Just as with date, datetime provides convenient class methods for creating new instances. It also includes fromordinal() and fromtimestamp().
```python
import datetime

t = datetime.time(1, 2, 3)
print('t :', t)

d = datetime.date.today()
print('d :', d)

dt = datetime.datetime.combine(d, t)
print('dt:', dt)
```
10. format date
```python
import datetime

today = datetime.datetime.today()
print('ISO     :', today)
print('format(): {:%a %b %d %H:%M:%S %Y}'.format(today))

```
11. time zone
```python

import datetime

min6 = datetime.timezone(datetime.timedelta(hours=-6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d = datetime.datetime.now(min6)

print(min6, ':', d)
print(datetime.timezone.utc, ':',
      d.astimezone(datetime.timezone.utc))
print(plus6, ':', d.astimezone(plus6))

# convert to the current system timezone
d_system = d.astimezone()
print(d_system.tzinfo, '      :', d_system)
```
### Python [代码片段](day2.py)
flask-socketio的用法