import argparse
import re
from datetime import datetime
from pathlib import Path

from cn2an import an2cn

DAYS_PATH = Path("days")


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

readme_header = "- [{day_name}]({day_path})--{date_name}"


def find_max_day_num(day_path: Path) -> int:

    max_day_pattern = re.search(r"\d+", str(day_path))
    if max_day_pattern is None:
        return 0
    return int(max_day_pattern.group(0))


def get_max_day(days_path: Path) -> Path:
    return max(days_path.iterdir(), key=find_max_day_num)


def add_md_hearder(md_path: Path) -> None:
    day_name_dig = re.search(r"\d+", str(md_path.parent))
    if day_name_dig is None:
        return
    day_name = day_name_dig.group(0)

    day_name = an2cn(day_name)
    # 把md后缀转换为py后缀
    day_py = str(md_path.stem) + ".py"
    with open(md_path, "w") as md:
        md.write(header.format(day_name=day_name, day_py=day_py))


def gen_new_day_dir(days_path: Path) -> None:
    day_last = get_max_day(days_path)
    day_num = re.search(r"\d+", str(day_last.stem))
    if day_num is None:
        return
    day_num_str = day_num.group(0)
    day_new = "day" + str(int(day_num_str) + 1)
    day_new_path_name = day_last.parent / day_new
    day_new_path = Path(day_new_path_name)
    day_new_path.mkdir()
    # 创建新的md 和 py 文件
    new_md = Path(day_new_path_name, day_new + ".md")
    new_py = Path(day_new_path_name, day_new + ".py")
    new_md.touch()
    new_py.touch()
    add_md_hearder(new_md)


def add_readme_info(day: Path) -> None:
    date_name = str(datetime.today()).split(" ")[0].replace("-", ".")
    new_day = get_max_day(DAYS_PATH)

    day_name = str(new_day.stem)
    day_path = Path(new_day, day_name + ".md")

    print(day_name, day_path, date_name)
    with open("README.md", "a+", encoding="utf-8") as md, open(
        day_path, "r", encoding="utf-8"
    ) as day_md:
        day_info = day_md.readlines()[2:9]
        md.write("\n")
        md.write(
            readme_header.format(
                day_name=day_name, day_path=day_path, date_name=date_name
            )
        )
        md.write("\n")
        for info in day_info:
            md.write("  " + info)


parser = argparse.ArgumentParser(description="parser arg to different function")
parser.add_argument("-g", "--gen")
args = parser.parse_args()


if __name__ == "__main__":
    if args.gen:
        add_readme_info(DAYS_PATH)
    else:
        gen_new_day_dir(DAYS_PATH)
