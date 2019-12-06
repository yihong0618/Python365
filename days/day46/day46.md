## 第四十六天
### 索引
- Python标准库--sys
- Python好的文章[The Zen of Python](https://farer.org/2016/08/24/the-zen-of-python/)
- [Python代码片段](day46.py)
- Python读书--Python 数据结构算法 day2
- Python框架相关--None
- Python项目相关--None
- Python之外--[尾递归](https://farer.org/2017/03/10/tail-recursion/)
### python标准库 [sys](https://pymotw.com/3/sys/index.html)
1. sys.getsizeof(obj)
```python
import sys


class WithAttributes:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return

    def __sizeof__(self):
        return object.__sizeof__(self) + \
            sum(sys.getsizeof(v) for v in self.__dict__.values())


my_inst = WithAttributes()
print(sys.getsizeof(my_inst))
```
2. sys.getrecursionlimit(), sys.setrecursionlimit(10)
3. sys.maxsize, sys.maxunicode
4. float
```python
import sys

print('Smallest difference (epsilon):', sys.float_info.epsilon)
print()
print('Digits (dig)              :', sys.float_info.dig)
print('Mantissa digits (mant_dig):', sys.float_info.mant_dig)
print()
print('Maximum (max):', sys.float_info.max)
print('Minimum (min):', sys.float_info.min)
print()
print('Radix of exponents (radix):', sys.float_info.radix)
print()
print('Maximum exponent for radix (max_exp):',
      sys.float_info.max_exp)
print('Minimum exponent for radix (min_exp):',
      sys.float_info.min_exp)
print()
print('Max. exponent power of 10 (max_10_exp):',
      sys.float_info.max_10_exp)
print('Min. exponent power of 10 (min_10_exp):',
      sys.float_info.min_10_exp)
print()
print('Rounding for addition (rounds):', sys.float_info.rounds)
```
5. Integer Values
```python
import sys

print('Number of bits used to hold each digit:',
      sys.int_info.bits_per_digit)
print('Size in bytes of C type used to hold each digit:',
      sys.int_info.sizeof_digit)
```