## 第三十七天
### 索引
- Python标准库--urllib.parse
- Python好的文章[Django配置Celery执行异步任务和定时任务](https://mp.weixin.qq.com/s/lXrp3igYo9W2UuE5Gauysg)
- [Python代码片段](day37.py)
- Python读书--None
- Python框架相关--None
- Python项目相关--None
- Python之外--[Data-Science-Notes](https://github.com/fengdu78/Data-Science-Notes)
### python标准库 [urllib.parse](https://pymotw.com/3/urllib.parse/index.html)
1. basic parse
```python
from urllib.parse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed)

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print('scheme  :', parsed.scheme)
print('netloc  :', parsed.netloc)
print('path    :', parsed.path)
print('params  :', parsed.params)
print('query   :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port    :', parsed.port)
```
2. urlsplit
3. urldefrag
```python
from urllib.parse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print('original:', original)
d = urldefrag(original)
print('url     :', d.url)
print('fragment:', d.fragment)

```
4. urljoin
5. urlencode
```python
from urllib.parse import urlencode

query_args = {
    'q': 'query string',
    'foo': 'bar',
}
encoded_args = urlencode(query_args)
print('Encoded:', encoded_args)

query_args = {
    'foo': ['foo1', 'foo2'],
}
print('Single  :', urlencode(query_args))
print('Sequence:', urlencode(query_args, doseq=True))

```
6. parse_qs, parse_qsl
```python
from urllib.parse import parse_qs, parse_qsl

encoded = 'foo=foo1&foo=foo2'

print('parse_qs :', parse_qs(encoded))
print('parse_qsl:', parse_qsl(encoded))
```