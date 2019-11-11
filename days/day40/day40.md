## 第四十天
### 索引
- Python标准库--uuid
- Python好的文章[Python 工匠：善用变量来改善代码质量](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/1-using-variables-well.md)
- [Python代码片段](day40.py)
- Python读书--编码DAY1
- Python框架相关--None
- Python项目相关--[pymxget](https://github.com/winterssy/pymxget)
- Python之外--[css3用scale实现下划线动画](https://www.jianshu.com/p/f91e606a770c)
### python标准库 [uuid](https://pymotw.com/3/uuid/index.html)
1. MAC Address--uuid.getnode()
2. uuid.uuid1()
3. uuid3 and uuid5 --- Name-Based Values
```python
import uuid

hostnames = ['www.doughellmann.com', 'blog.doughellmann.com']

for name in hostnames:
    print(name)
    print('  MD5   :', uuid.uuid3(uuid.NAMESPACE_DNS, name))
    print('  SHA-1 :', uuid.uuid5(uuid.NAMESPACE_DNS, name))
    print()
```
4. uuid4 Random Values

### 善用变量来改善代码质量
1. 多使用 nametuple/dict 来让函数返回多个值
2. 控制单个函数内变量数量
3. 及时删掉没用的变量
4. 能不定义变量就不定义