from pathlib import Path
from cn2an import an2cn

days_path = Path("days")


header = """## 第{day_name}天
### 索引
- Python标准库--
- Python好的文章[]()
- [Python代码片段]({day_py})
- Python读书--[]()
- Python框架相关--[]()
- Python项目相关--[]()
- Python之外--[]()
"""


def add_md_hearder(md_path):
    day_name_dig = str(md_path).split('/')[-2][-1]
    day_name = an2cn(day_name_dig)
    # 把md后缀转换为py后缀
    day_py = str(md_path).split('/')[-1][:-3] + ".py"
    with open(md_path, "w") as md:
        md.write(header.format(day_name=day_name, day_py=day_py))


def gen_new_day_dir(days_path):
    day_last = max(days_path.iterdir())
    day_new = str(day_last)[:-1] + str(int(str(day_last)[-1]) + 1)
    day_new_name = str(day_new).split("/")[-1]
    day_new_path = Path(day_new)
    day_new_path.mkdir()
    # 创建新的md 和 py 文件
    new_md, new_py = day_new_name + ".md", day_new_name + ".py"
    day_new_path_md = day_new_path / new_md
    day_new_path_py = day_new_path / new_py
    day_new_path_md.touch()
    day_new_path_py.touch()
    add_md_hearder(day_new_path_md)


if __name__ == "__main__":
    gen_new_day_dir(days_path)