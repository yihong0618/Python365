## 第二十三天
### 索引
- Python标准库--io
- Python好的文章[Linux IO模式及 select、poll、epoll详解](https://taohuawu.club/linux-io-select-poll-epoll)
- [Python代码片段](day23.py)
- Python读书--None
- Python框架相关--[flask请求生命周期](http://www.ziawang.com/article/15/)
- Python项目相关--[fy](https://github.com/chenjiandongx/fy)
- Python之外--[书单](https://taohuawu.club/reading-list#b3_solo_h1_0)
### python标准库 [io](https://pymotw.com/3/io/index.html)
1. basic
```python
import io

# Writing to a buffer
output = io.StringIO()
output.write('This goes into the buffer. ')
print('And so does this.', file=output)

# Retrieve the value written
print(output.getvalue())

output.close()  # discard buffer memory

# Initialize a read buffer
input = io.StringIO('Inital value for read buffer')

# Read from the buffer
print(input.read())
```