## 第二十天
### 索引
- Python标准库--heapq
- Python好的文章[PyCon小节](https://laike9m.com/blog/wo-de-2019-pycon-china-xiao-jie-xia,127/)
- [Python代码片段](day20.py)
- Python读书--None
- Python框架相关--[django中自动重载机制探究](https://www.hongweipeng.com/index.php/archives/1365/)
- Python项目相关--[Cyberbrain](https://github.com/laike9m/Cyberbrain)
- Python之外--今天终于离职了，开心
### python标准库 [heapq](https://pymotw.com/3/heapq/index.html)
1. basic
```python
heapq_showtree.py
import math
from io import StringIO


def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
```
2. heapify
3. nlargest, nsmallest
4. heapq.merge(*data)