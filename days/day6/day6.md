## 第六天
### 索引
- Python标准库--pathlib
- Python好的文章[你应该使用pathlib代替os.path](https://www.dongwm.com/post/use-pathlib/)
- [Python代码片段](day6.py)
- Python读书--[Django企业开发实战day6])
- Python框架相关--[Django与wsgi.ref](http://www.ziawang.com/article/172/)
- Python项目相关--[py12306](https://github.com/pjialin/py12306)
- Python之外--[10分钟教会你看top](https://juejin.im/post/5d590126f265da03db0776b6?utm_source=gold_browser_extension)
### python标准库 [pathlib](https://pymotw.com/3/pathlib/index.html)
1. base
```python
import pathlib

usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)


usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())

root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)
```
2. replace glob
```python
import pathlib

ind = pathlib.PurePosixPath('source/pathlib/index.rst')
print(ind)

py = ind.with_name('pathlib_from_existing.py')
print(py)

pyc = py.with_suffix('.pyc')
print(pyc)
```
3. Parsing Paths
``` python
import pathlib

p = pathlib.PurePosixPath('/usr/local')
print(p.parts)
p = pathlib.PurePosixPath('/usr/local/lib')

print('parent: {}'.format(p.parent))

print('\nhierarchy:')
for up in p.parents:
    print(up)

import pathlib

p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print('path  : {}'.format(p))
print('name  : {}'.format(p.name))
print('suffix: {}'.format(p.suffix))
print('stem  : {}'.format(p.stem))
```
4. Directory Contents
```python
import pathlib

p = pathlib.Path('.')

for f in p.iterdir():
    print(f)

p = pathlib.Path('..')

for f in p.glob('*.rst'):
    print(f)
```
5. Reading and Writing Files
```python
import pathlib

f = pathlib.Path('example.txt')

f.write_bytes('This is the content'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print('read from open(): {!r}'.format(handle.read()))

print('read_text(): {!r}'.format(f.read_text('utf-8')))
```
6. os vs pathlib [这篇文字](https://www.dongwm.com/post/use-pathlib/)
### [Python代码片段--自动生成新的一天目录](day6.py)