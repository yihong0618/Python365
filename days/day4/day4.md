## 第四天
### 索引
- Python标准库--textwrap
- Python好的文章--[Python实现简单的遗传算法](http://czrzchao.com/simpleGaByPython)
- [Python代码片段](day4.py)
- Python读书--[Django企业开发实战day4](http://product.dangdang.com/26509799.html)
- Python项目相关--[python 解析器](http://qingyunha.github.io/taotao/)
- Python之外--[如何想静静](https://yihui.name/cn/2019/07/inner-peace/)
### python标准库 [textwrap](https://pymotw.com/3/textwrap/index.html)
1. fill
```python
import textwrap
sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
print(textwrap.fill(sample_text, width=50))
```
2. dedent
```python
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()
This produces outputs in th
```
3. indent
```python
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print('Quoted block:\n')
print(final)
```
4. shorten
```python
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Original:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShortened:\n')
print(shortened_wrapped)
```