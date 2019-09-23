## 第十四天
### 索引
- Python标准库--operator
- Python好的文章[python 代码阅读和有趣的项目推荐](https://blog.kelu.org/tech/2017/07/28/python-opensource-intro.html)
- [Python代码片段](day14.py)
- Python读书--python cookbook day8
- Python框架相关--[Bottle源码-启动篇](https://blog.dreamfever.me/2017/03/20/bottleyuan-ma-qi-dong-pian/)
- Python项目相关--[bottle](https://github.com/bottlepy/bottle)
- Python之外--[深入理解 HTTP 协议](https://juejin.im/post/5ba65296f265da0ac8493503)
### python标准库 [operator](https://pymotw.com/3/operator/index.html)
1. 逻辑运算符
2. 比较操作符
3. 算术操作符号（注意floordiv和truediv）
4. 序列操作符
5. 原地操作符
6. attrgetter
```python
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)  # Calls p.distance(0, 0)
import operator
operator.methodcaller('distance', 0, 0)(p)

points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]
# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))
```
