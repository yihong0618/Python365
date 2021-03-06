## 计划
首先当然是列个计划, 目前大概设想是每天抽出一小时左右（更长的话更好），完成大概如下板块。

1. Python标准库（[来自《Python 3 Module of the Week》小的每天一个，大的多天一个，列举用法](https://pymotw.com/3/index.html))
2. Python好的文章
3. Python代码片段
4. Python读书
5. Python项目相关（自己的项目或学习其他的项目）
6. Python之外

365天坚持住的话真的是一笔挺大的财富，能完成的话对自己算是一个提升，完成不了的话也不过是互联网上一个无名小卒又一次失败的尝试，总之有勇气开始就已经是目的地的一半了，是吧。
2019.10.31 更新，完成了1/10，新开坑Front100

## 标准库

- [x] Text--Done 2019.9.21
    - [x] string — Text Constants and Templates
    - [x] textwrap — Formatting Text Paragraphs
    - [x] re — Regular Expressions
    - [x] difflib — Compare Sequences
- [ ] Data Structures
    - [x] enum – Enumeration Type
    - [ ] collections — Container Data Types
    - [ ] array — Sequence of Fixed-type Data
    - [x] heapq – Heap Sort Algorithm
    - [x] bisect — Maintain Lists in Sorted Order
    - [x] queue — Thread-Safe FIFO Implementation
    - [ ] struct — Binary Data Structures
    - [x] weakref — Impermanent References to Objects
    - [x] copy — Duplicate Objects
    - [x] pprint — Pretty-Print Data Structures
- [ ] Algorithms
    - [ ] functools — Tools for Manipulating Functions
    - [x] itertools — Iterator Functions
    - [x] operator — Functional Interface to Built-in Operators
    - [ ] contextlib — Context Manager Utilities
- [x] Dates and Times
    - [x] time — Clock Time
    - [x] datetime — Date and Time Value Manipulation
    - [x] calendar — Work with Dates
- [ ] Mathematics
    - [x] decimal — Fixed and Floating Point Math
    - [ ] fractions — Rational Numbers
    - [x] random — Pseudorandom Number Generators
    - [ ] math — Mathematical Functions
    - [ ] statistics — Statistical Calculations
- [ ] The File System
    - [x] os.path — Platform-independent Manipulation of Filenames
    - [x] pathlib — Filesystem Paths as Objects
    - [x] glob — Filename Pattern Matching
    - [x] fnmatch — Unix-style Glob Pattern Matching
    - [ ] linecache — Read Text Files Efficiently
    - [x] tempfile — Temporary File System Objects
    - [ ] shutil — High-level File Operations
    - [ ] filecmp — Compare Files
    - [ ] mmap — Memory-map Files
    - [ ] codecs — String Encoding and Decoding
    - [x] io — Text, Binary, and Raw Stream I/O Tools
- [ ] Data Persistence and Exchange
    - [x] pickle — Object Serialization
    - [ ] shelve — Persistent Storage of Objects
    - [ ] dbm — Unix Key-Value Databases
    - [ ] sqlite3 — Embedded Relational Database
    - [ ] xml.etree.ElementTree — XML Manipulation API
    - [x] csv — Comma-separated Value Files
- [ ] Data Compression and Archiving
    - [ ] zlib — GNU zlib Compression
    - [ ] gzip — Read and Write GNU zip Files
    - [ ] bz2 — bzip2 Compression
    - [ ] tarfile — Tar Archive Access
    - [ ] zipfile — ZIP Archive Access
- [ ] Cryptography
    - [x] hashlib — Cryptographic Hashing
    - [ ] hmac — Cryptographic Message Signing and Verification
- [ ] Concurrency with Processes, Threads, and Coroutines
    - [ ] subprocess — Spawning Additional Processes
    - [ ] signal — Asynchronous System Events
    - [x] threading — Manage Concurrent Operations Within a Process
    - [ ] multiprocessing — Manage Processes Like Threads
    - [ ] asyncio — Asynchronous I/O, event loop, and concurrency tools
    - [ ] concurrent.futures — Manage Pools of Concurrent Tasks
- [ ] Networking
    - [ ] ipaddress — Internet Addresses
    - [ ] socket — Network Communication
    - [ ] selectors — I/O Multiplexing Abstractions
    - [ ] select — Wait for I/O Efficiently
    - [ ] socketserver — Creating Network Servers
- [ ] The Internet
    - [ ] urllib.parse — Split URLs into Components
    - [ ] urllib.request — Network Resource Access
    - [ ] urllib.robotparser — Internet Spider Access Control
    - [ ] base64 — Encode Binary Data with ASCII
    - [ ] http.server — Base Classes for Implementing Web Servers
    - [ ] http.cookies — HTTP Cookies
    - [ ] webbrowser — Displays web pages
    - [x] uuid — Universally Unique Identifiers
    - [x] json — JavaScript Object Notation
    - [ ] xmlrpc.client — Client Library for XML-RPC
    - [ ] xmlrpc.server — An XML-RPC server
- [ ] Email
    - [ ] smtplib — Simple Mail Transfer Protocol Client
    - [ ] smtpd — Sample Mail Servers
    - [ ] mailbox — Manipulate Email Archives
    - [ ] imaplib — IMAP4 Client Library
- [ ] Application Building Blocks
    - [x] argparse — Command-Line Option and Argument Parsing
    - [ ] getopt — Command Line Option Parsing
    - [ ] readline — The GNU readline Library
    - [ ] getpass — Secure Password Prompt
    - [ ] cmd — Line-oriented Command Processors
    - [ ] shlex — Parse Shell-style Syntaxes
    - [ ] configparser — Work with Configuration Files
    - [ ] logging — Report Status, Error, and Informational Messages
    - [ ] fileinput — Command-Line Filter Framework
    - [ ] atexit — Program Shutdown Callbacks
    - [ ] sched — Timed Event Scheduler
- [ ] Internationalization and Localization
    - [ ] gettext — Message Catalogs
    - [ ] locale — Cultural Localization API
- [ ] Developer Tools
    - [ ] pydoc — Online Help for Modules
    - [ ] doctest — Testing Through Documentation
    - [ ] unittest — Automated Testing Framework
    - [x] trace — Follow Program Flow
    - [ ] traceback — Exceptions and Stack Traces
    - [ ] cgitb — Detailed Traceback Reports
    - [ ] pdb — Interactive Debugger
    - [ ] profile and pstats — Performance Analysis
    - [ ] timeit — Time the execution of small bits of Python code.
    - [ ] tabnanny — Indentation validator
    - [ ] compileall — Byte-compile Source Files
    - [ ] pyclbr — Class Browser
    - [ ] venv — Create Virtual Environments
    - [ ] ensurepip — Install the Python Package Installer
- [ ] Runtime Features
    - [ ] site — Site-wide Configuration
    - [ ] sys — System-specific Configuration
    - [ ] os — Portable access to operating system specific features
    - [ ] platform — System Version Information
    - [ ] resource — System Resource Management
    - [ ] gc — Garbage Collector
    - [ ] sysconfig — Interpreter Compile-time Configuration
- [ ] Language Tools
    - [ ] warnings — Non-fatal Alerts
    - [x] abc — Abstract Base Classes
    - [x] dis — Python Bytecode Disassembler
    - [x] inspect — Inspect Live Objects
- [ ] Modules and Packages
    - [ ] importlib — Python’s Import Mechanism
    - [ ] pkgutil — Package Utilities
    - [ ] zipimport — Load Python Code from ZIP Archives
    - [ ] Unix-specific Services
    - [ ] pwd — Unix Password Database
    - [ ] grp — Unix Group Database
- [ ] Porting Notes
    - [ ] References
    - [ ] New Modules
    - [ ] Renamed Modules
    - [ ] Removed Modules
    - [ ] Deprecated Modules
    - [ ] Summary of Changes to Modules
- [ ] Outside of the Standard Library
    - [ ] Text
    - [ ] Algorithms
    - [ ] Dates and Times
    - [ ] Mathematics
    - [ ] Data Persistence and Exchange
    - [ ] Cryptography
    - [ ] Concurrency with Processes, Threads, and Coroutines
    - [ ] The Internet
    - [ ] Email
    - [ ] Application Building Blocks
    - [ ] Developer Tools


## 读书
- [ ] 读完《Python Cookbook》
- [ ] 重读《流畅的Python》
- [ ] 重读《Python web开发》
- [ ] 读《TDD Python》
- [ ] 重读《Effective Python》
- [ ] 读《Mastering Python Design Patterns》
- [ ] 读《Cython》
- [ ] 重读《深入理解Python特性》
- [ ] 读《Django 文档》
- [ ] 读[《Django REST framework API 指南》](https://github.com/jianshijiuyou/django-rest-framework-api-guide)
- [ ] 重读《Python高性能编程》
- [ ] 读《利用Python进行数据分析 2e》
- [ ] 读《Python源码剖析》
- [ ] [重读《one-python-craftsman》](https://github.com/piglei/one-python-craftsman)
- [ ] [读Django设计模式与最佳实践](https://github.com/cundi/Django-Design-Patterns-and-Best-Practices)

## 项目相关
- [ ] [Python patterns](https://github.com/faif/python-patterns)
- [ ] [Let’s Build A Web Server](https://ruslanspivak.com/lsbaws-part1/)
- [ ] [Let’s Build A Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/)
- [ ] [数据结构和算法必知必会的50个代码实现](https://github.com/wangzheng0822/algo)
- [ ] [CPython-Internals](https://github.com/zpoint/CPython-Internals)
- [ ] [wtfpython](https://github.com/satwikkansal/wtfpython)
- [ ] [Web application from scratch](https://defn.io/2018/02/25/web-app-from-scratch-01/)
- [ ] [100-Days-Of-ML-Code](https://github.com/MLEveryday/100-Days-Of-ML-Code)
- [x] [Python实现的Python解释器](http://qingyunha.github.io/taotao/)

## Days
- [day1](days/day1/day1.md)--2019.09.05
  - Python标准库--time
  - Python好的文章--[Python之路](https://blog.laisky.com/p/python-road/)
  - [Python代码片段--asyncio](day1.py)
  - Python读书--[Django企业开发实战day1](http://product.dangdang.com/26509799.html)
  - Python项目相关--[funNLP](https://github.com/fighting41love/funNLP)
  - Python之外--[大型互联网公司分布式ID方案总结](https://juejin.im/post/5d6fc8eff265da03ef7a324b?utm_source=gold_browser_extension)
- [day2](days/day2/day2.md)--2019.09.06
  - Python标准库--datetime
  - Python好的文章--[Python WSGI初探](http://liaoph.com/python-wsgi/)
  - [Python代码片段--flask-socketio](day2.py)
  - Python读书--[Django企业开发实战day2](http://product.dangdang.com/26509799.html)
  - Python项目相关--[iredis](https://github.com/laixintao/iredis)
  - Python之外--[web前端学习指南](https://github.com/qianguyihao/Web)
- [day3](days/day3/day3.md)--2019.09.07
  - Python标准库--calendar
  - Python好的文章--[Python数据结构及算法](https://blog.laisky.com/p/algorithm/)
  - [Python代码片段](day3.py)
  - Python读书--[Django企业开发实战day3](http://product.dangdang.com/26509799.html)
  - Python项目相关--[python 解析器中文翻译](https://github.com/chinesehuazhou/guido_blog_translation)
  - Python之外--[梁少峰的个人博客](https://github.com/youngwind/blog)
- [day4](days/day4/day4.md)--2019.09.09
  - Python标准库--textwrap
  - Python好的文章--[Python实现简单的遗传算法](http://czrzchao.com/simpleGaByPython)
  - [Python代码片段](day4.py)
  - Python读书--[Django企业开发实战day4](http://product.dangdang.com/26509799.html)
  - Python项目相关--[python 解析器](http://qingyunha.github.io/taotao/)
  - Python之外--[如何想静静](https://yihui.name/cn/2019/07/inner-peace/)
- [day5](days/day5/day5.md)--2019.09.10
  - Python标准库--enum
  - Python好的文章--[python黑魔法描述符](https://www.jishuyiliu.com/archives/311.html)
  - [Python代码片段](day5.py)
  - Python读书--[Django企业开发实战day5](http://product.dangdang.com/26509799.html)
  - Python框架相关--[Django常用配置](http://www.ziawang.com/article/169/)
  - Python项目相关--[青岛大学平台](https://github.com/yihong0618/OnlineJudge)
  - Python之外--[正则表达式你不会写](https://juejin.im/post/5b96a8e2e51d450e6a2de115)
- [day6](days/day6/day6.md)--2019.09.12
  - Python标准库--pathlib
  - Python好的文章--[你应该使用pathlib代替os.path](https://www.dongwm.com/post/use-pathlib/)
  - [Python代码片段](day6.py)
  - Python读书--[Django企业开发实战day6](http://product.dangdang.com/26509799.html)
  - Python框架相关--[Django与wsgi.ref](http://www.ziawang.com/article/172/)
  - Python项目相关--[py12306](https://github.com/pjialin/py12306)
  - Python之外--[10分钟教会你看top](https://juejin.im/post/5d590126f265da03db0776b6?utm_source=gold_browser_extension)
- [day7](days/day7/day7.md)--2019.09.13
  - Python标准库--pprint
  - Python好的文章[Python中的坑](https://www.v2ai.cn/python/2019/01/01/PY-6.html)
  - [Python代码片段](day7.py)
  - Python读书--[Django企业开发实战day7](http://product.dangdang.com/26509799.html)
  - Python框架相关--[Django中间件](http://www.ziawang.com/article/322/)
  - Python项目相关--[快速转化「中文数字」和「阿拉伯数字」](https://www.dovolopor.com/cn2an)
  - Python之外--[一份详细HTTP学习指南](https://juejin.im/post/5b95bf226fb9a05d16586851)
- [day8](days/day8/day8.md)--2019.09.15
  - Python标准库--argparse
  - Python好的文章[Python Argparse Cookbook](https://mkaz.blog/code/python-argparse-cookbook/)
  - [Python代码片段](day8.py)
  - Python读书--Python Cookbook day1
  - Python框架相关--[Django中的request请求](http://www.ziawang.com/article/175/)
  - Python项目相关--[Leetcode](https://github.com/liweiwei1419/LeetCode-Solution-Python)
  - Python之外--[程序员应该怎样提高自己](https://blog.codingnow.com/2019/07/top_programmer.html#comments)

- [day9](days/day9/day9.md)--2019.09.17
  - Python标准库--difflib
  - Python好的文章[Python版本管理依赖的最终方案](https://linw1995.com/blog/Python-%E7%89%88%E6%9C%AC%E5%8F%8A%E4%BE%9D%E8%B5%96%E7%AE%A1%E7%90%86%E7%9A%84%E6%9C%80%E7%BB%88%E6%96%B9%E6%A1%88-pyenv-Pipenv/)
  - [Python代码片段](day9.py)
  - Python读书--[Python cookbook day2]()
  - Python框架相关--[Django中的response](http://www.ziawang.com/article/176/)
  - Python项目相关--[project-based-learning](https://github.com/tuvtran/project-based-learning)
  - Python之外--[git的技巧](https://github.com/521xueweihan/git-tips)

- [day10](days/day10/day10.md)--2019.09.19
  - Python标准库--re
  - Python好的文章[python 的静态类型检查工具 mypy](https://blog.laisky.com/p/mypy/)
  - [Python代码片段](day10.py)
  - Python读书--Python cookbook day3
  - Python框架相关--[Django路由系统](http://www.ziawang.com/article/179/)
  - Python项目相关--[mkdoc](https://github.com/mkdocs/mkdocs)
  - Python之外--[DarkSun的个人博客](http://blog.lujun9972.win/years/)

- [day11](days/day11/day11.md)--2019.09.20
  - Python标准库--queue
  - Python好的文章[web-app-from-scratch-01](https://defn.io/2018/02/25/web-app-from-scratch-01/)
  - [Python代码片段](day11.py)
  - Python读书--python cookbook day4
  - Python框架相关--[django admin路由系统源码剖析](http://www.ziawang.com/article/180/)
  - Python项目相关--[将微信接收的文章自动解析同步到Bear](https://github.com/howie6879/w2b)
  - Python之外--[pure-bash-bible](https://github.com/dylanaraps/pure-bash-bible#length)

- [day12](days/day12/day12.md)--2019.09.21
  - Python标准库--string
  - Python好的文章[Python格式化工具Black](https://leeweir.github.io/2018/07/20/Python%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%B7%A5%E5%85%B7Black/)
  - [Python代码片段](day12.py)
  - Python读书--python cookbook day5
  - Python框架相关--[Django Rest framework流程](http://www.ziawang.com/article/302/)
  - Python项目相关--[GadioVideo](https://github.com/rabbitism/GadioVideo)
  - Python之外--[Docker容器化部署Python应用](https://zhuanlan.zhihu.com/p/71251233)

- [day13](days/day13/day13.md)--2019.09.22
  - Python标准库--fnmatch
  - Python好的文章[Web开发简介系列](https://jiajunhuang.com/articles/2017_10_19-web_dev_series.md.html)
  - [Python代码片段](day13.py)
  - Python读书--Python cookbook day7
  - Python框架相关--[REST framework 认证流程源码分析](http://www.ziawang.com/article/303/)
  - Python项目相关--[pdir2](https://github.com/laike9m/pdir2)
  - Python之外--[重构读书笔记](http://www.wklken.me/posts/2017/06/17/refactoring-07.html)

- [day14](days/day14/day14.md)--2019.09.23
  - Python标准库--operator
  - Python好的文章[python 代码阅读和有趣的项目推荐](https://blog.kelu.org/tech/2017/07/28/python-opensource-intro.html)
  - [Python代码片段](day14.py)
  - Python读书--python cookbook day8
  - Python框架相关--[Bottle源码-启动篇](https://blog.dreamfever.me/2017/03/20/bottleyuan-ma-qi-dong-pian/)
  - Python项目相关--[bottle](https://github.com/bottlepy/bottle)
  - Python之外--[深入理解 HTTP 协议](https://juejin.im/post/5ba65296f265da0ac8493503)

- [day15](days/day15/day15.md)--2019.09.24
  - Python标准库--copy
  - Python好的文章[Flask 中的 Context 初探](https://manjusaka.itscoder.com/posts/2018/02/23/something-about-flask-context/)
  - [Python代码片段](day15.py)
  - Python读书--Django设计模式与最佳实践 day1
  - Python框架相关--[flask路由系统](http://www.ziawang.com/article/10/)
  - Python项目相关--[c9-python-getting-started](https://github.com/microsoft/c9-python-getting-started)
  - Python之外--[补蛇者说](https://pythonhunter.org/)

- [day16](days/day16/day16.md)--2019.09.25
  - Python标准库--contextlib
  - Python好的文章[从contextlib源码谈with语句](https://www.yukunweb.com/2018/8/Talking-with-from-the-ontextlib-source/)
  - [Python代码片段](day16.py)
  - Python读书--Django设计模式与最佳实践 day2
  - Python框架相关--[Bottle源码-应用主体](https://blog.dreamfever.me/2017/03/22/bottleyuan-ma-ying-yong-zhu-ti/)
  - Python项目相关--[person blog powered by flask ](https://github.com/Blackyukun/YuBlog)
  - Python之外--[TCP握手与socket通信细节](https://www.jianshu.com/p/3f42172f582b)

- [day17](days/day17/day17.md)--2019.09.26
  - Python标准库--bisect
  - Python好的文章[花了两个星期，我终于把 WSGI 整明白了](https://juejin.im/post/5cff300a6fb9a07ef06f8a43)
  - [Python代码片段](day17.py)
  - Python读书--Django设计模式与最佳实践 day3
  - Python框架相关--[Bottle源码-路由](https://blog.dreamfever.me/2017/03/25/bottleyuan-ma-lu-you/)
  - Python项目相关--[kuriyama](https://github.com/Hanaasagi/kuriyama)
  - Python之外--[学会这21条，你就是 Vim 大神！](https://juejin.im/post/5d4818a0e51d4561d54de912)

- [day18](days/day18/day18.md)--2019.09.27
  - Python标准库--weakref
  - Python好的文章[Python项目容器化实践(一) - Docker Compose](https://www.dongwm.com/post/use-dcker-compose/)
  - [Python代码片段](day18.py)
  - Python读书--Django设计模式与最佳实践 day4
  - Python框架相关--[Django restfulframework 权限](http://www.ziawang.com/article/304/)
  - Python项目相关--[lyanna](https://github.com/dongweiming/lyanna)
  - Python之外--[学完这篇你就会写正则](https://juejin.im/post/5d89edb1518825097619ecfe)

- [day19](days/day19/day19.md)--2019.09.28
  - Python标准库--random
  - Python好的文章[在Django View中使用asyncio](https://www.hongweipeng.com/index.php/archives/1814/)
  - [Python代码片段](day19.py)
  - Python读书-- 没读
  - Python框架相关--[Django restfulframework 限流](http://www.ziawang.com/article/305/)
  - Python项目相关--[diy-async-web-framework](https://github.com/hzlmn/diy-async-web-framework#asyncio-low-level-apis-transports--protocols)
  - Python之外--[计算机网络太难？了解这一篇就够了](https://juejin.im/post/5d896cccf265da03bd055c87)

- [day20](days/day20/day20.md)--2019.09.29
  - Python标准库--heapq
  - Python好的文章[PyCon小节](https://laike9m.com/blog/wo-de-2019-pycon-china-xiao-jie-xia,127/)
  - [Python代码片段](day20.py)
  - Python读书--None
  - Python框架相关--[django中自动重载机制探究](https://www.hongweipeng.com/index.php/archives/1365/)
  - Python项目相关--[Cyberbrain](https://github.com/laike9m/Cyberbrain)
  - Python之外--今天终于离职了，开心

- [day21](days/day21/day21.md)--2019.09.30
  - Python标准库--socket
  - Python好的文章[python3 f-string格式化字符串的高级用法](https://mlln.cn/2018/05/19/python3%20f-string%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95/#menu)
  - [Python代码片段](day21.py)
  - Python读书--None
  - Python框架相关--[Django 源码阅读(一):概览从入口到请求到响应](https://www.hongweipeng.com/index.php/archives/1369/)
  - Python项目相关--[poetry](https://github.com/sdispater/poetry)
  - Python之外--[TCP/IP简明教程 - 从零构建TCP/IP协议](https://jiajunhuang.com/articles/2017_08_12-tcp_ip.md.html)

- [day22](days/day22/day22.md)--2019.10.01
  - Python标准库--threading
  - Python好的文章[Python 源码: 复制列表元素时 Python 做了什么？](https://github.com/shidenggui/blog/issues/16)
  - [Python代码片段](day22.py)
  - Python读书--None
  - Python框架相关--[flask蓝图基础](http://www.ziawang.com/article/14/)
  - Python项目相关--[easytrader](https://github.com/shidenggui/easytrader)
  - Python之外--[使用Github的webhooks进行网站自动化部署](https://aotu.io/notes/2016/01/07/auto-deploy-website-by-webhooks-of-github/index.html)

- [day23](days/day23/day23.md)--2019.10.02
  - Python标准库--io
  - Python好的文章[Linux IO模式及 select、poll、epoll详解](https://taohuawu.club/linux-io-select-poll-epoll)
  - [Python代码片段](day23.py)
  - Python读书--None
  - Python框架相关--[flask请求生命周期](http://www.ziawang.com/article/15/)
  - Python项目相关--[fy](https://github.com/chenjiandongx/fy)
  - Python之外--[书单](https://taohuawu.club/reading-list#b3_solo_h1_0)

- [day24](days/day24/day24.md)--2019.10.03
  - Python标准库--glob
  - Python好的文章[A Python Interpreter Written in Python](http://qingyunha.github.io/taotao/)
  - [Python代码片段](day24.py)
  - Python读书--Python cookbook
  - Python框架相关--[flask CBV FBV](http://www.ziawang.com/article/16/)
  - Python项目相关--[Build a RESTful API with Flask – The TDD Way](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
  - Python之外--[计算机系统要素](https://github.com/woai3c/nand2tetris)

- [day25](days/day25/day25.md)--2019.10.05
  - Python标准库--decimal
  - Python好的文章[Python 工匠：使用数字与字符串的技巧](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/3-tips-on-numbers-and-strings.md)
  - [Python代码片段](day25.py)
  - Python读书--Python cookbook
  - Python框架相关--[Flask 上下文对象源码](http://www.ziawang.com/article/19/)
  - Python项目相关--[lsbasi](https://github.com/rspivak/lsbasi)
  - Python之外--[中英双语字幕精校版 CSAPP](https://github.com/EugeneLiu/translationCSAPP)

- [day26](days/day26/day26.md)--2019.10.07
  - Python标准库--logging
  - Python好的文章[asyncio 笔记](https://manjusaka.itscoder.com/posts/2017/06/07/some-note-for-asyncio/)
  - [Python代码片段](day26.py)
  - Python读书--Python cookbook
  - Python框架相关--[你所不知道的 Flask Part1:Route 初探](https://manjusaka.itscoder.com/posts/2017/08/13/what-the-fuck-about-flask-part1/)
  - Python项目相关--None
  - Python之外--[当···时发生了什么？](https://github.com/skyline75489/what-happens-when-zh_CN)

- [day27](days\day27\day27.md)--2019.10.10
  - Python标准库--hashlib
  - Python好的文章[跟着 Github 学习 Restful HTTP API 设计](https://cizixs.com/2016/12/12/restful-api-design-guide/)
  - [Python代码片段](day27.py)
  - Python读书--Python cookbook
  - Python框架相关--[Django 2.0 新特性抢先看](http://www.liujiangblog.com/blog/8/)
  - Python项目相关--[新闻网页正文通用抽取器 Alpha 版.](https://github.com/kingname/GeneralNewsExtractor)
  - Python之外--[130+vim基本命令](http://wklken.me/posts/2013/08/17/130-essential-vim-commands.html#stq=&stp=0)

- [day28](days\day28\day28.md)--2019.10.12
  - Python标准库--multiprocessing
  - Python好的文章[Python super 没那么简单](https://mozillazg.com/2016/12/python-super-is-not-as-simple-as-you-thought.html)
  - [Python代码片段](day28.py)--super
  - Python读书--None
  - Python框架相关--[django相关的一些列表](https://github.com/hhstore/blog/labels/Py-Django)
  - Python项目相关--[issues博客](https://github.com/hhstore/blog)
  - Python之外--[并行编程的各种锁](https://blog.laisky.com/p/concurrency-lock/)

- [day29](days/day29/day29.md)--2019.10.14
  - Python标准库--inspect
  - Python好的文章[socket in Python](https://realpython.com/python-sockets/)
  - [Python代码片段](day29.py)
  - Python读书--None
  - Python框架相关--[Django REST framework API 指南](https://juejin.im/post/5a991807518825558a060a77)
  - Python项目相关--[SOLID](https://github.com/dboyliao/SOLID)
  - Python之外--[在日本工作和生活是一种什么样的体验](https://justinyan.me/post/3927)

- [day30](days\day30\day30.md)--2019.10.15
  - Python标准库--os.path
  - Python好的文章[初解PYTHON并发](https://linw1995.com/blog/%E5%88%9D%E8%A7%A3Python%E5%B9%B6%E5%8F%91/)
  - [Python代码片段](day30.py)
  - Python读书--None
  - Python框架相关--[django rest framework mixins小结](https://juejin.im/post/5a66fc64f265da3e4e25c6e7)
  - Python项目相关--[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
  - Python之外--[grex](https://github.com/pemistahl/grex)

- [day31](days\day31\day31.md)--2019.10.16
  - Python标准库--select
  - Python好的文章[Python 3.8正式发布，带来那些新特性？](https://www.dongwm.com/post/whats-new-in-python-3-dot-8/)
  - [Python代码片段](day31.py)
  - Python读书--None
  - Python框架相关--[https://www.dongwm.com/post/113/](https://www.dongwm.com/post/113/)
  - Python项目相关--[https://www.dongwm.com/post/120/](不可错过的Python技术博客（网站）)
  - Python之外--[ASCII table in golang](https://github.com/olekukonko/tablewriter)

- [day32](days/day32/day32.md)--2019.10.18
  - Python标准库--csv
  - Python好的文章[How To Use Linux epoll with Python](http://scotdoyle.com/python-epoll-howto.html)
  - [Python代码片段](day32.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
  - Python之外--None

- [day33](days\day33\day33.md)--2019.10.21
  - Python标准库--pickle
  - Python好的文章[如何在静态检查中表达 sentinel](https://blog.dreamfever.me/2019/10/17/ru-he-zai-jing-tai-jian-cha-zhong-biao-da-sentinel/)
  - [Python代码片段](day33.py)
  - Python读书--Python cookbook
  - Python框架相关--None
  - Python项目相关--[code2sec.com 安全相关](https://github.com/bit4woo/code2sec.com)
  - Python之外--[程序员修炼之道第二版开始翻译了](https://blog.codingnow.com/2019/10/tpp2nd.html#more)

- [day34](days\day34\day34.md)--2019.10.22
  - Python标准库--itertools day1
  - Python好的文章[MENUEXPLORING UNITED STATES POLICING DATA USING PYTHON](https://blog.patricktriest.com/police-data-python/)
  - [Python代码片段](day34.py)
  - Python读书--None
  - Python框架相关--None
  - Python之外--[PayloadsAllTheThings][https://github.com/swisskyrepo/PayloadsAllTheThings]

- [day35](days\day36\day35.md)--2019.10.28
  - Python标准库--itertools day2
  - Python好的文章[[python]记录关于websocket的原理和使用](https://vimiix.com/post/2018/04/02/python-websocket/)
  - [Python代码片段](day35.py)
  - Python读书--None
  - Python框架相关--[Django Channels2.0 websocket最佳实践](https://vimiix.com/post/2018/07/26/channels2-tutorial/)
  - Python项目相关--[examiner](https://github.com/howie6879/examiner)
  - Python之外--[原生JS灵魂之问, 请问你能接得住几个？(上)](https://juejin.im/post/5dac5d82e51d45249850cd20)

- [day36](days\day36\day36.md)--2019.10.30
  - Python标准库--itertools day3
  - Python好的文章[Django使用Channels实现WebSocket--上篇](https://juejin.im/post/5cb67fc3e51d456e6a1d0237)
  - [Python代码片段](day36.py)
  - Python读书--None
  - Python框架相关--[Django 源码小剖: 应用程序入口 WSGIHandler](https://www.cnblogs.com/daoluanxiaozi/p/3315838.html)
  - Python项目相关--[Strava-local-heatmap](https://github.com/remisalmon/Strava-local-heatmap)
  - Python之外--[《Kubernetes In Action》 摘抄 & 笔记](https://blog.laisky.com/p/kubernetes-in-action/)

- [day37](days\day37\day37.md)--2019.10.30
  - Python标准库--urllib.parse
  - Python好的文章[Django配置Celery执行异步任务和定时任务](https://mp.weixin.qq.com/s/lXrp3igYo9W2UuE5Gauysg)
  - [Python代码片段](day37.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[Data-Science-Notes](https://github.com/fengdu78/Data-Science-Notes)

- [day38](days\day38\day38.md)--2019.11.05
  - Python标准库--subprocess
  - Python好的文章[Python 源码: 复制列表元素时 Python 做了什么](https://github.com/shidenggui/blog/issues/16)
  - [Python代码片段](day38.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[网络编程所需要熟悉的那些函数](https://jiajunhuang.com/articles/2019_11_01-network_programming.md.html)

- [day39](days\day39\day39.md)--2019.11.07
  - Python标准库--tempfile
  - Python好的文章[带你进入异步Django+Vue的世界 - Didi打车实战](https://www.jianshu.com/p/7e5f2090555d)
  - [Python代码片段](day39.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[《计算机网络－自顶向下方法》笔记](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)

- [day40](days\day40\day40.md)--2019.11.11
  - Python标准库--uuid
  - Python好的文章[Python 工匠：善用变量来改善代码质量](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/1-using-variables-well.md)
  - [Python代码片段](day40.py)
  - Python读书--编码DAY1
  - Python框架相关--None
  - Python项目相关--[pymxget](https://github.com/winterssy/pymxget)
  - Python之外--[css3用scale实现下划线动画](https://www.jianshu.com/p/f91e606a770c)

- [day41](days\day41\day41.md)--2019.11.13
  - Python标准库--abc
  - Python好的文章[我的技术栈选型](https://jiajunhuang.com/articles/2019_11_13-tech_stack.md.html)
  - [Python代码片段](day41.py)
  - Python读书--编码
  - Python框架相关--None
  - Python项目相关--[vscode-leetcode](https://github.com/jdneo/vscode-leetcode)
  - Python之外--[How to build an HTML calculator app from scratch using JavaScript](https://www.freecodecamp.org/news/how-to-build-an-html-calculator-app-from-scratch-using-javascript-4454b8714b98/)

- [day42](days\day42\day42.md)--2019.11.26
  - Python标准库--dis
  - Python好的文章[Python代码性能优化方法总结](https://hanfeng.ink/post/python_performance/)
  - [Python代码片段](day42.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--[Geo Heatmap](https://github.com/luka1199/geo-heatmap)
  - Python之外--[进程简介](https://hanfeng.ink/post/porcess/)

- [day43](days\day43\day43.md)--2019.11.29
  - Python标准库--json
  - Python好的文章[线程简介](https://hanfeng.ink/post/thread/)
  - [Python代码片段](day43.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[Git原理解析](https://hanfeng.ink/post/git_core/)

- [day44](days\day44\day44.md)--2019.12.04
  - Python标准库--sys day1
  - Python好的文章[Python后端架构演进](https://zhu327.github.io/2018/07/19/python%E5%90%8E%E7%AB%AF%E6%9E%B6%E6%9E%84%E6%BC%94%E8%BF%9B/)
  - [Python代码片段](day44.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--[problem-solving-with-algorithms-and-data-structure-using-python](https://facert.gitbooks.io/python-data-structure-cn/)
  - Python之外--[Gunicorn与uWSGI之我见](https://zhu327.github.io/2018/08/29/gunicorn%E4%B8%8Euwsgi%E4%B9%8B%E6%88%91%E8%A7%81/)

- [day45](days\day45\day45.md)--2019.12.05
  - Python标准库--sys day2
  - Python好的文章--[Django JSONField SQL注入漏洞（CVE-2019-14234）分析与影响](https://www.leavesongs.com/PENETRATION/django-jsonfield-cve-2019-14234.html)
  - [Python代码片段](day45.py)
  - Python读书--Python数据结构与算法 day1
  - Python框架相关--[Django优化](https://zhu327.github.io/2017/04/21/django-%E4%BC%98%E5%8C%96%E6%9D%82%E8%B0%88/)
  - Python项目相关--None
  - Python之外--[服务治理与RPC](https://zhu327.github.io/2018/03/24/%E6%9C%8D%E5%8A%A1%E6%B2%BB%E7%90%86%E4%B8%8Erpc/)

- [day47](days\day47\day47.md)--2019.12.09
  - Python标准库--ast
  - Python好的文章--[AST模块用Python修改Python代码](https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue3/static-modification-of-python-with-python-the-ast-module.html)
  - [Python代码片段](day47.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[leetcode的一篇博客](http://www.noteanddata.com/)

- [day49](days\day49\day49.md)--2019.12.11
  - Python标准库--None
  - Python好的文章--[chrome vim](chrome-extension://ihlenndgcmojhcghmfjfneahoeklbjjh/pages/mappings.html)
  - [Python代码片段](day49.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--[Python教育资源大全中文版](https://github.com/wwj718/awesome-python-in-education-zh)
  - Python之外--[putteteer教程](https://www.yuque.com/imhelloworld/share-day/xug9av)

- [day50](days\day50\day50.md)--2019.12.13
  - Python标准库--trace
  - Python好的文章--[[Python]内建函数getattr()函数详解](https://www.vimiix.com/post/2017/07/10/Introduce-getattr-function/)
  - [Python代码片段](day50.py)
  - Python读书--《编码》
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[排序算法之桶排序的深入理解以及性能分析](https://dailc.github.io/2016/12/03/baseKnowlenge_algorithm_sort_bucketSort.html)

- [day51](days\day51\day51.md)--2019.12.30
  - Python标准库--None
  - Python好的文章[如何在静态检查中表达 sentinel](https://blog.dreamfever.me/2019/10/17/ru-he-zai-jing-tai-jian-cha-zhong-biao-da-sentinel/)
  - [Python代码片段](day51.py)
  - Python读书--Problem Solving with Algorithms and Data Structures using Python--day2
  - Python框架相关--[papurika](https://github.com/Hanaasagi/papurika)
  - Python项目相关--None
  - Python之外--[How to implement a programming language in JavaScript](http://lisperator.net/pltut/)

- [day52](days\day52\day52.md)--2020.01.02
  - Python标准库--None
  - Python好的文章[Python 工匠：写好面向对象代码的原则（上）](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/12-write-solid-python-codes-part-1.md)
  - [Python代码片段](day52.py)
  - Python读书--Python数据结构算法 day2
  - Python框架相关--None
  - Python项目相关--None
  - Python之外--[我如何用三个月自学入门日语](http://numbbbbb.com/2016/07/04/20160704_%E6%88%91%E5%A6%82%E4%BD%95%E7%94%A8%E4%B8%89%E4%B8%AA%E6%9C%88%E5%85%A5%E9%97%A8%E6%97%A5%E8%AF%AD/)

- [day53](days\day53\day53.md)--2020.01.03
  - Python标准库--None
  - Python好的文章[python源码剖析-数据结构](http://wklken.me/posts/2016/03/01/python-source-datastructure.html)
  - [Python代码片段](day53.py)
  - Python读书--None
  - Python框架相关--[Django项目重构小结](http://wklken.me/posts/2018/12/06/python-refactor-django-project.html)
  - Python项目相关--None
  - Python之外--[操作系统 & 编译原理 学习攻略](https://hanfeng.ink/post/os_compiler_map/)

- [day54](days\day54\day54.md)--2020.01.20
  - Python标准库--None
  - Python好的文章[Python代码规范小结](http://wklken.me/posts/2016/11/03/python-code-style.html)
  - [Python代码片段](day54.py)
  - Python读书--None
  - Python框架相关--[httpx](https://github.com/encode/httpx)
  - Python项目相关--[Web安全学习笔记](https://github.com/LyleMi/Learn-Web-Hacking)
  - Python之外--[深入理解Node.js：核心思想与源码分析](https://github.com/yjhjstz/deep-into-node)

- [day55](days\day55\day55.md)--2020.02.03
  - Python标准库--None
  - Python好的文章[muridesu-lang](https://github.com/LanguageAsGarbage/muridesu-lang)
  - [Python代码片段](day55.py)
  - Python读书--None
  - Python框架相关--None
  - Python项目相关--[a_journey_into_math_of_ml](https://github.com/aespresso/a_journey_into_math_of_ml)
  - Python之外--[焦虑](https://yufree.cn/cn/2018/12/01/anxiety/)
