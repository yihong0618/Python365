## 第二十四天
### 索引
- Python标准库--glob
- Python好的文章[A Python Interpreter Written in Python](http://qingyunha.github.io/taotao/)
- [Python代码片段](day24.py)
- Python读书--Python cookbook
- Python框架相关--[flask CBV FBV](http://www.ziawang.com/article/16/)
- Python项目相关--[Build a RESTful API with Flask – The TDD Way](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
- Python之外--[计算机系统要素](https://github.com/woai3c/nand2tetris)
### python标准库 [glob](https://pymotw.com/3/glob/index.html)
1. basic
```python
import glob
for name in sorted(glob.glob('dir/*')):
    print(name)

for name in sorted(glob.glob('dir/file?.txt')):
    print(name)

for name in sorted(glob.glob('dir/*[0-9].*')):
    print(name)
```
