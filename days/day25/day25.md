## 第二十五天
### 索引
- Python标准库--decimal
- Python好的文章[Python 工匠：使用数字与字符串的技巧](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/3-tips-on-numbers-and-strings.md)
- [Python代码片段](day25.py)
- Python读书--Python cookbook
- Python框架相关--[Flask 上下文对象源码](http://www.ziawang.com/article/19/)
- Python项目相关--[lsbasi](https://github.com/rspivak/lsbasi)
- Python之外--[中英双语字幕精校版 CSAPP](https://github.com/EugeneLiu/translationCSAPP)
### python标准库 [decimal](https://pymotw.com/3/decimal/index.html)
1. basic 注意：Decimal中应该放的是字符串
```python
a = 4.2
b = 2.1

a + b != 6.3

from decimal import Decimal
c = Decimal("4.2")
d = Decimal("2.1")
c + d == Decimal("6.3")

```
2. localcontext 使用上下文表达式