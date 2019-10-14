## 第二十九天
### 索引
- Python标准库--inspect
- Python好的文章[socket in Python](https://realpython.com/python-sockets/)
- [Python代码片段](day29.py)
- Python读书--None
- Python框架相关--[Django REST framework API 指南](https://juejin.im/post/5a991807518825558a060a77)
- Python项目相关--[SOLID](https://github.com/dboyliao/SOLID)
- Python之外--[在日本工作和生活是一种什么样的体验](https://justinyan.me/post/3927)
### python标准库 [inspect](https://pymotw.com/3/inspect/index.html)
1. basic
```python
>>> import inspect
>>> inspect.ismodule(inspect)    # 检查 inspect 是否为模组
True
>>> inspect.ismethod(inspect)    # 检查 inspect 是否为对象方法
False
>>> inspect.isfunction(len)      # 检查 len 是否为函数
True
>>> inspect.isbuiltin(len)       # 检查 len 是否为内置函数
True
>>> inspect.isgenerator(inspect) # 检查 inspect 是否为生成器
False
>>> inspect.isawaitable(inspect) # 检查 inspect 是否可用于 await 表达式
False
>>>

```
2. Signature
3. bind
```python
from functools import wraps
def checked(func):
    ann=func.__annotations__
    sig=inspect.signature(func)
    @wraps(func)
    def wrapper(*args,**kwargs):
        bound=sig.bind(*args,**kwargs)
        for k,v in bound.arguments.items():
            if k in ann:
                assert isinstance(v,ann[k]),f'Type Error Expected {ann[k]}'
        return func(*args,**kwargs)
    return wrapper

>>> @checked
... def add(a: int, b: int) -> int:
...     while b:
...         a, b = b, a % b
...     return a
>>> add(2.7, 3.6)
Traceback (most recent call last):
  AssertionError: Type Error Expected <class 'int'>
>>> add(27, 36)
9

```