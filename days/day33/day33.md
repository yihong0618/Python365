## 第三十三天
### 索引
- Python标准库--pickle
- Python好的文章[如何在静态检查中表达 sentinel](https://blog.dreamfever.me/2019/10/17/ru-he-zai-jing-tai-jian-cha-zhong-biao-da-sentinel/)
- [Python代码片段](day33.py)
- Python读书--Python cookbook
- Python框架相关--None
- Python项目相关--[code2sec.com 安全相关](https://github.com/bit4woo/code2sec.com)
- Python之外--[程序员修炼之道第二版开始翻译了](https://blog.codingnow.com/2019/10/tpp2nd.html#more)
### python标准库 [pickle](https://pymotw.com/3/pickle/index.html)
1. basic
```python
import pickle
import pprint

data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('BEFORE: ', end=' ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print('AFTER : ', end=' ')
pprint.pprint(data2)

print('SAME? :', (data1 is data2))
print('EQUAL?:', (data1 == data2))
```
2. with file
```python
import pickle
import pprint
import sys

filename = sys.argv[1]

with open(filename, 'rb') as in_s:
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print('READ: {} ({})'.format(
                o.name, o.name_backwards))

```
3. Unpicklable Objects
``` python
import pickle


class State:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'State({!r})'.format(self.__dict__)


class MyClass:

    def __init__(self, name):
        print('MyClass.__init__({})'.format(name))
        self._set_name(name)

    def _set_name(self, name):
        self.name = name
        self.computed = name[::-1]

    def __repr__(self):
        return 'MyClass({!r}) (computed={!r})'.format(
            self.name, self.computed)

    def __getstate__(self):
        state = State(self.name)
        print('__getstate__ -> {!r}'.format(state))
        return state

    def __setstate__(self, state):
        print('__setstate__({!r})'.format(state))
        self._set_name(state.name)


inst = MyClass('name here')
print('Before:', inst)

dumped = pickle.dumps(inst)

reloaded = pickle.loads(dumped)
print('After:', reloaded)

```