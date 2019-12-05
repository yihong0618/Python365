## 第四十五天
### 索引
- Python标准库--sys day2
- Python好的文章--[Django JSONField SQL注入漏洞（CVE-2019-14234）分析与影响](https://www.leavesongs.com/PENETRATION/django-jsonfield-cve-2019-14234.html)
- [Python代码片段](day45.py)
- Python读书--Python数据结构与算法 day1
- Python框架相关--[Django优化](https://zhu327.github.io/2017/04/21/django-%E4%BC%98%E5%8C%96%E6%9D%82%E8%B0%88/)
- Python项目相关--None
- Python之外--[服务治理与RPC](https://zhu327.github.io/2018/03/24/%E6%9C%8D%E5%8A%A1%E6%B2%BB%E7%90%86%E4%B8%8Erpc/)
### python标准库 [sys](https://pymotw.com/3/sys/index.html)
1. sys.argv
```python
import sys

print('Arguments:', sys.argv)
```
2. sys.stderr
```python
import sys

print('STATUS: Reading from stdin', file=sys.stderr)

data = sys.stdin.read()

print('STATUS: Writing data to stdout', file=sys.stderr)

sys.stdout.write(data)
sys.stdout.flush()

print('STATUS: Done', file=sys.stderr)
```
3. sys.getrefcount()
```python
import sys

one = []
print('At start         :', sys.getrefcount(one))

two = one

print('Second reference :', sys.getrefcount(one))

del two

print('After del        :', sys.getrefcount(one))
```