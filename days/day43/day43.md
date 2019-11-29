## 第四十三天
### 索引
- Python标准库--json
- Python好的文章[线程简介](https://hanfeng.ink/post/thread/)
- [Python代码片段](day43.py)
- Python读书--None
- Python框架相关--None
- Python项目相关--None
- Python之外--[Git原理解析](https://hanfeng.ink/post/git_core/)
### python标准库 [json](https://pymotw.com/3/json/index.html)
1. basic
```python
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

data_string = json.dumps(data)
print('JSON:', data_string)
```
2. ident
```python
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

print('NORMAL:', json.dumps(data, sort_keys=True))
print('INDENT:', json.dumps(data, sort_keys=True, indent=2))
```

3. io
```python
import io
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

f = io.StringIO()
json.dump(data, f)

print(f.getvalue())
```
4. command line
```python
$ python3 -m json.tool example.json

[
    {
        "a": "A",
        "c": 3.0,
        "b": [
            2,
            4
        ]
    }
]

$ python3 -m json.tool --sort-keys example.json

[
    {
        "a": "A",
        "b": [
            2,
            4
        ],
        "c": 3.0
    }
]
```