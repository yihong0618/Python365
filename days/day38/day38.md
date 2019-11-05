## 第三十八天
### 索引
- Python标准库--subprocess
- Python好的文章[Python 源码: 复制列表元素时 Python 做了什么](https://github.com/shidenggui/blog/issues/16)
- [Python代码片段](day38.py)
- Python读书--None
- Python框架相关--None
- Python项目相关--None
- Python之外--[网络编程所需要熟悉的那些函数](https://jiajunhuang.com/articles/2019_11_01-network_programming.md.html)
### python标准库 [subprocess](https://pymotw.com/3/subprocess/index.html)
1. basic
```python
import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)
```
2. capturing output
```python
import subprocess

completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)
```