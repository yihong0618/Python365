## 第五十天
### 索引
- Python标准库--trace
- Python好的文章--[[Python]内建函数getattr()函数详解](https://www.vimiix.com/post/2017/07/10/Introduce-getattr-function/)
- [Python代码片段](day50.py)
- Python读书--《编码》
- Python框架相关--None
- Python项目相关--None
- Python之外--[排序算法之桶排序的深入理解以及性能分析](https://dailc.github.io/2016/12/03/baseKnowlenge_algorithm_sort_bucketSort.html)
### python标准库 [trace](https://pymotw.com/3/trace/index.html)
1. basic--cli
    - python -m --trace
    - python -m trace --count
    - python -m trace --coverdir --count
    - python -m trace --coverdir --report --summary 
2. coding
```python
import trace
from trace_example.recurse import recurse

tracer = trace.Trace(count=False, trace=True)
tracer.run('recurse(2)')
``` 