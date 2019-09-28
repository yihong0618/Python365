## 第十九天
### 索引
- Python标准库--random
- Python好的文章[在Django View中使用asyncio](https://www.hongweipeng.com/index.php/archives/1814/)
- [Python代码片段](day19.py)
- Python读书-- 没读
- Python框架相关--[Django restfulframework 限流](http://www.ziawang.com/article/305/)
- Python项目相关--[diy-async-web-framework](https://github.com/hzlmn/diy-async-web-framework#asyncio-low-level-apis-transports--protocols)
- Python之外--[计算机网络太难？了解这一篇就够了](https://juejin.im/post/5d896cccf265da03bd055c87)
### python标准库 [random](https://pymotw.com/3/random/index.html)
1. random random.random
```python
import random

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()

```
2. random.uniform
```python
import random

for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()

```
3. random.seed(2) 种子一样生成的值就一样
4. random.choice()接收个可迭代对象
5. random.shuffle()
6. random.sample() 不包含重复的