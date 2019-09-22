## 第十三天
### 索引
- Python标准库--fnmatch
- Python好的文章[Web开发简介系列](https://jiajunhuang.com/articles/2017_10_19-web_dev_series.md.html)
- [Python代码片段](day13.py)
- Python读书--Python cookbook day7
- Python框架相关--[REST framework 认证流程源码分析](http://www.ziawang.com/article/303/)
- Python项目相关--[pdir2](https://github.com/laike9m/pdir2)
- Python之外--[重构读书笔记](http://www.wklken.me/posts/2017/06/17/refactoring-07.html)
### python标准库 [fnmatch](https://pymotw.com/3/fnmatch/index.html)
1. simple match (大小写是否敏感根据系统，如果强制敏感使用 fnmatchcase())
```python
import fnmatch
import os

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)
print()

files = os.listdir('.')
for name in sorted(files):
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatch(name, pattern)))
```
2. filter 返回列表
```python
import fnmatch
import os
import pprint

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)

files = list(sorted(os.listdir('.')))

print('\nFiles   :')
pprint.pprint(files)

print('\nMatches :')
pprint.pprint(fnmatch.filter(files, pattern))
```
3. translate (转换为标准的正则)
```python
import fnmatch

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)
print('Regex   :', fnmatch.translate(pattern))
```