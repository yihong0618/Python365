## 第十六天
### 索引
- Python标准库--contextlib
- Python好的文章[从contextlib源码谈with语句](https://www.yukunweb.com/2018/8/Talking-with-from-the-ontextlib-source/)
- [Python代码片段](day16.py)
- Python读书--Django设计模式与最佳实践 day2
- Python框架相关--[Bottle源码-应用主体](https://blog.dreamfever.me/2017/03/22/bottleyuan-ma-ying-yong-zhu-ti/)
- Python项目相关--[person blog powered by flask ](https://github.com/Blackyukun/YuBlog)
- Python之外--[TCP握手与socket通信细节](https://www.jianshu.com/p/3f42172f582b)
### python标准库 [contextlib](https://pymotw.com/3/contextlib/index.html)
1. Context Manager API
```python
class WithinContext:

    def __init__(self, context):
        print('WithinContext.__init__({})'.format(context))

    def do_something(self):
        print('WithinContext.do_something()')

    def __del__(self):
        print('WithinContext.__del__')


class Context:

    def __init__(self):
        print('Context.__init__()')

    def __enter__(self):
        print('Context.__enter__()')
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')


with Context() as c:
    c.do_something()
```
2. From Generator to Context Manager
```python
import contextlib


@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        yield {}
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')


print('Normal:')
with make_context() as value:
    print('  inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')

from contextlib import contextmanager

@contextmanager
def opened(filename, mode="r"):
    file = open(filename, mode)
    print('start')
    try:
        yield file
    finally:
        file.close()
        print('end')

with opened("/etc/passwd") as f:
    for line in f:
        print(line.strip())
```