## 第三十九天
### 索引
- Python标准库--tempfile
- Python好的文章[带你进入异步Django+Vue的世界 - Didi打车实战](https://www.jianshu.com/p/7e5f2090555d)
- [Python代码片段](day39.py)
- Python读书--None
- Python框架相关--None
- Python项目相关--None
- Python之外--[《计算机网络－自顶向下方法》笔记](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)
### python标准库 [tempfile](https://pymotw.com/3/tempfile/index.html)
1. basic 文件关闭后自动删除
```python
import os
import tempfile

print('Building a filename with PID:')
filename = '/tmp/guess_my_name.{}.txt'.format(os.getpid())
with open(filename, 'w+b') as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

# Clean up the temporary file yourself.
os.remove(filename)

print()
print('TemporaryFile:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Some data')

    temp.seek(0)
    print(temp.read())
```
