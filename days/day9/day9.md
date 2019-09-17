## 第九天
### 索引
- Python标准库--difflib
- Python好的文章[Python版本管理依赖的最终方案](https://linw1995.com/blog/Python-%E7%89%88%E6%9C%AC%E5%8F%8A%E4%BE%9D%E8%B5%96%E7%AE%A1%E7%90%86%E7%9A%84%E6%9C%80%E7%BB%88%E6%96%B9%E6%A1%88-pyenv-Pipenv/)
- [Python代码片段](day9.py)
- Python读书--[Python cookbook day2]()
- Python框架相关--[Django中的response](http://www.ziawang.com/article/176/)
- Python项目相关--[project-based-learning](https://github.com/tuvtran/project-based-learning)
- Python之外--[git的技巧](https://github.com/521xueweihan/git-tips)
### python标准库  [difflib](https://pymotw.com/3/difflib/index.html)
1. Differ
```python
import difflib

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))


diff = difflib.unified_diff(
    text1_lines,
    text2_lines,
    lineterm='',
)
```
2. SequenceMatcher
```python
from difflib import SequenceMatcher


def show_results(match):
    print('  a    = {}'.format(match.a))
    print('  b    = {}'.format(match.b))
    print('  size = {}'.format(match.size))
    i, j, k = match
    print('  A[a:a+size] = {!r}'.format(A[i:i + k]))
    print('  B[b:b+size] = {!r}'.format(B[j:j + k]))


A = " abcd"
B = "abcd abcd"

print('A = {!r}'.format(A))
print('B = {!r}'.format(B))

print('\nWithout junk detection:')
s1 = SequenceMatcher(None, A, B)
match1 = s1.find_longest_match(0, len(A), 0, len(B))
show_results(match1)

print('\nTreat spaces as junk:')
s2 = SequenceMatcher(lambda x: x == " ", A, B)
match2 = s2.find_longest_match(0, len(A), 0, len(B))
show_results(match2)
```
