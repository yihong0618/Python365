## 第十七天
### 索引
- Python标准库--bisect
- Python好的文章[花了两个星期，我终于把 WSGI 整明白了](https://juejin.im/post/5cff300a6fb9a07ef06f8a43)
- [Python代码片段](day17.py)
- Python读书--Django设计模式与最佳实践 day3
- Python框架相关--[Bottle源码-路由](https://blog.dreamfever.me/2017/03/25/bottleyuan-ma-lu-you/)
- Python项目相关--[kuriyama](https://github.com/Hanaasagi/kuriyama)
- Python之外--[学会这21条，你就是 Vim 大神！](https://juejin.im/post/5d4818a0e51d4561d54de912)
### python标准库 [bisect](https://pymotw.com/3/bisect/index.html
1. insort
```python
import bisect

# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3}  {:3}'.format(i, position), l)
```