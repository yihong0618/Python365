## 第四十一天
### 索引
- Python标准库--abc
- Python好的文章[我的技术栈选型](https://jiajunhuang.com/articles/2019_11_13-tech_stack.md.html)
- [Python代码片段](day41.py)
- Python读书--编码
- Python框架相关--None
- Python项目相关--[vscode-leetcode](https://github.com/jdneo/vscode-leetcode)
- Python之外--[How to build an HTML calculator app from scratch using JavaScript](https://www.freecodecamp.org/news/how-to-build-an-html-calculator-app-from-scratch-using-javascript-4454b8714b98/)
### python标准库 [abc](https://pymotw.com/3/abc/index.html)
1. basic
> 1.抽象类概念
抽象类是一个特殊的类，只能被继承，不能实例化
2. 为什么要有抽象类
其实在未接触抽象类概念时，我们可以构造香蕉、苹果、梨之类的类，然后让它们继承水果这个的基类，水果的基类包含一个eat函数。
但是你有没有想过，我们可以将香蕉、苹果、梨实例化，去吃香蕉、苹果、梨。但是我们却不能将水果实例化，因为我们无法吃到叫水果的这个东西。
所以抽象类中只能有抽象方法（没有实现功能），该类不能被实例化，只能被继承，且子类必须实现抽象方法。
3. 抽象类的作用
在不同的模块中通过抽象基类来调用，可以用最精简的方式展示出代码之间的逻辑关系，让模块之间的依赖清晰简单。

```python
import abc


class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""

class LocalBaseClass:
    pass


@PluginBase.register
class RegisteredImplementation(LocalBaseClass):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)
```