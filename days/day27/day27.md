## 第二十七天
### 索引
- Python标准库--hashlib
- Python好的文章[跟着 Github 学习 Restful HTTP API 设计](https://cizixs.com/2016/12/12/restful-api-design-guide/)
- [Python代码片段](day27.py)
- Python读书--Python cookbook
- Python框架相关--[Django 2.0 新特性抢先看](http://www.liujiangblog.com/blog/8/)
- Python项目相关--[新闻网页正文通用抽取器 Alpha 版.](https://github.com/kingname/GeneralNewsExtractor)
- Python之外--[130+vim基本命令](http://wklken.me/posts/2013/08/17/130-essential-vim-commands.html#stq=&stp=0)
### python标准库 [hashlib](https://pymotw.com/3/hashlib/index.html)
1. 都有什么
```python
import hashlib


print('Guaranteed:\n{}\n'.format(
    ', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}'.format(
    ', '.join(sorted(hashlib.algorithms_available))))
```
2. 基本使用
```python
import hashlib

lorem = '''Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.''

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

```
3. Update
```python
import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()


def chunkize(size, text):
    "Return parts of the text in size-based increments."
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return


h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)
line_by_line = h.hexdigest()

print('All at once :', all_at_once)
print('Line by line:', line_by_line)
print('Same        :', (all_at_once == line_by_line))
```