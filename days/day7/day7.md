## 第七天
### 索引
- Python标准库--pprint
- Python好的文章[Python中的坑](https://www.v2ai.cn/python/2019/01/01/PY-6.html)
- [Python代码片段](day7.py)
- Python读书--[Django企业开发实战day7](http://product.dangdang.com/26509799.html)
- Python框架相关--[Django中间件](http://www.ziawang.com/article/322/)
- Python项目相关--[快速转化「中文数字」和「阿拉伯数字」](https://www.dovolopor.com/cn2an)
- Python之外--[一份详细HTTP学习指南](https://juejin.im/post/5b95bf226fb9a05d16586851)
### python标准库 [pprint](https://pymotw.com/3/pprint/index.html
1. pprint
```python
data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]
from pprint import pprint

print('PRINT:')
print(data)
print()
print('PPRINT:')
pprint(data)
```
2. class with __repr__
```python
from pprint import pprint


class node:

    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return (
            'node(' + repr(self.name) + ', ' +
            repr(self.contents) + ')'
        )


trees = [
    node('node-1'),
    node('node-2', [node('node-2-1')]),
    node('node-3', [node('node-3-1')]),
]
pprint(trees)

```
3. pprint(data, depth=1), pprint(data, depth=2) 可以定义深度
4. pprint(data, width=width) 可以定义宽度
