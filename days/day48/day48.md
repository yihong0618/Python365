## 第四十八天
### 索引
- Python标准库--os
- Python好的文章[后端工程师学前端(三): CSS进阶(特指度、单位和字体族)](https://jiajunhuang.com/articles/2019_07_04-learn_front_end_3.md.html)
- [Python代码片段](day48.py)
- Python读书--None
- Python框架相关--None
- Python项目相关--None
- Python之外--[Implementing a Simple Compiler on 25 Lines of JavaScript](https://blog.mgechev.com/2017/09/16/developing-simple-interpreter-transpiler-compiler-tutorial/)
### python标准库 [os](https://pymotw.com/3/os/index.html)
1. os.pid
2. environment
```python
import os

print('Initial value:', os.environ.get('TESTVAR', None))
print('Child process:')
os.system('echo $TESTVAR')

os.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED'

print()
print('Changed value:', os.environ['TESTVAR'])
print('Child process:')
os.system('echo $TESTVAR')

del os.environ['TESTVAR']

print()
print('Removed value:', os.environ.get('TESTVAR', None))
print('Child process:')
os.system('echo $TESTVAR')
```
4. os.fork