## 第三十天
### 索引
- Python标准库--os.path
- Python好的文章[初解PYTHON并发](https://linw1995.com/blog/%E5%88%9D%E8%A7%A3Python%E5%B9%B6%E5%8F%91/)
- [Python代码片段](day30.py)
- Python读书--None
- Python框架相关--[django rest framework mixins小结](https://juejin.im/post/5a66fc64f265da3e4e25c6e7)
- Python项目相关--[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- Python之外--[grex](https://github.com/pemistahl/grex)
### python标准库 [os.path](https://pymotw.com/3/os.path/index.html)
1. os.sep, os.extsep, os.pardir, os.curdir
2. os.path.join, os.path.splittext, os.path.abspath 
```python
import os.path

FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    '/',
    './broken_link',
]

for file in FILENAMES:
    print('File        : {!r}'.format(file))
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Mountpoint? :', os.path.ismount(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
    print()
```