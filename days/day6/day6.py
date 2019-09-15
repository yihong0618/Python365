from pathlib import Path

days_path = Path("days")


def gen_new_day(days_path):
    day_last = max(days_path.iterdir())
    day_new = str(day_last)[:-1] + str(int(str(day_last)[-1]) + 1)
    day_new_name = str(day_new).split("/")[-1]
    day_new_path = Path(day_new)
    day_new_path.mkdir()
    day_new_path_md = day_new_path / (day_new_name + ".md")
    day_new_path_py = day_new_path / (day_new_name + ".py")
    day_new_path_md.touch()
    day_new_path_py.touch()


if __name__ == "__main__":
    gen_new_day(days_path)
