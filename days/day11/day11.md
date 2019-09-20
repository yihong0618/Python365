## 第十一天
### 索引
- Python标准库--queue
- Python好的文章[web-app-from-scratch-01](https://defn.io/2018/02/25/web-app-from-scratch-01/)
- [Python代码片段](day11.py)
- Python读书--python cookbook day4
- Python框架相关--[django admin路由系统源码剖析](http://www.ziawang.com/article/180/)
- Python项目相关--[将微信接收的文章自动解析同步到Bear](https://github.com/howie6879/w2b)
- Python之外--[pure-bash-bible](https://github.com/dylanaraps/pure-bash-bible#length)
### python标准库 [queue](https://pymotw.com/3/queue/index.html)-- Thread-Safe FIFO Implementatio
1. basic
```python
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
```
2. LIFO Queue¶
```python
import queue

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
```
3. [Priority Queue](day11.py)