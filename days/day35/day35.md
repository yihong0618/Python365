## 第三十五天
### 索引
- Python标准库--itertools day2
- Python好的文章[[python]记录关于websocket的原理和使用](https://vimiix.com/post/2018/04/02/python-websocket/)
- [Python代码片段](day35.py)
- Python读书--None
- Python框架相关--[Django Channels2.0 websocket最佳实践](https://vimiix.com/post/2018/07/26/channels2-tutorial/)
- Python项目相关--[examiner](https://github.com/howie6879/examiner)
- Python之外--[原生JS灵魂之问, 请问你能接得住几个？(上)](https://juejin.im/post/5dac5d82e51d45249850cd20)
### python标准库 [itertools](https://pymotw.com/3/itertools/index.html)
1. cycle
2. repeat
```python
from itertools import *

for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))
```
3. dropwhile
4. filter & filterfalse
5. compress: compress() offers another way to filter the contents of an iterable. Instead of calling a function, it uses the values in another iterable to indicate when to accept a value and when to ignore it.
```python
from itertools import *

every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()

```
6. groupby
```python
import functools
from itertools import *
import operator
import pprint


@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


# Create a dataset of Point instances
data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))
print('Data:')
pprint.pprint(data, width=35)
print()

# Try to group the unsorted data based on X values
print('Grouped, unsorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Sort the data
data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Group the sorted data based on X values
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()
```
