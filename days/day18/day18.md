## 第十八天
### 索引
- Python标准库--weakref
- Python好的文章[Python项目容器化实践(一) - Docker Compose](https://www.dongwm.com/post/use-dcker-compose/)
- [Python代码片段](day18.py)
- Python读书--Django设计模式与最佳实践 day4
- Python框架相关--[Django restfulframework 权限](http://www.ziawang.com/article/304/)
- Python项目相关--[lyanna](https://github.com/dongweiming/lyanna)
- Python之外--[学完这篇你就会写正则](https://juejin.im/post/5d89edb1518825097619ecfe)
### python标准库 [weakref](https://pymotw.com/3/weakref/index.html)
1. 建立
```python
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

```
2. [好的文章](https://blog.louie.lu/2017/07/29/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-04-weakref/)