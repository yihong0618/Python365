## 第三十四天
### 索引
- Python标准库--itertools day1
- Python好的文章[MENUEXPLORING UNITED STATES POLICING DATA USING PYTHON](https://blog.patricktriest.com/police-data-python/)
- [Python代码片段](day34.py)
- Python读书--None
- Python框架相关--None
- Python之外--[PayloadsAllTheThings][https://github.com/swisskyrepo/PayloadsAllTheThings]
### python标准库 [itertools](https://pymotw.com/3/itertools/index.html)
1. chain
2. zip
3. isslice
```python
from itertools import *

print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')
print('\n')
```
4. tee: 复制一些迭代器
```python
from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()

print('i1:', list(i1))
print('i2:', list(i2))
```