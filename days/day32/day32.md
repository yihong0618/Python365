## 第三十二天
### 索引
- Python标准库--csv
- Python好的文章[How To Use Linux epoll with Python](http://scotdoyle.com/python-epoll-howto.html)
- [Python代码片段](day32.py)
- Python读书--None
- Python框架相关--None
- Python项目相关--[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- Python之外--None
### python标准库 [csv](https://pymotw.com/3/csv/index.html)
1. read
```python
import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
2. write
```python
import csv
import sys

unicode_chars = 'å∫ç'

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '08/{:02d}/07'.format(i + 1),
            unicode_chars[i],
        )
        writer.writerow(row)

print(open(sys.argv[1], 'rt').read())
```