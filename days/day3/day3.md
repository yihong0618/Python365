## 第三天
### 索引
- Python标准库--calendar
- Python好的文章--[Python数据结构及算法](https://blog.laisky.com/p/algorithm/)
- [Python代码片段](day3.py)
- Python读书--[Django企业开发实战day3](http://product.dangdang.com/26509799.html)
- Python项目相关--[python 解析器中文翻译](https://github.com/chinesehuazhou/guido_blog_translation)
- Python之外--[梁少峰的个人博客](https://github.com/youngwind/blog)
---

### python标准库 [calendar](https://pymotw.com/3/calendar/index.html)
1. The prmonth() method is a simple function that produces the formatted text output for a month.
```python
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2017, 7)
```
2. local
```python
import calendar

c = calendar.LocaleTextCalendar(locale='en_US')
c.prmonth(2017, 7)

print()

c = calendar.LocaleTextCalendar(locale='fr_FR')
c.prmonth(2017, 7)
```

### Python [代码片段](day3.py), [链接](https://www.fabfile.org/)
fabric基本使用