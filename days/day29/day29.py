import inspect
from pprint import pprint

import example


for name, data in inspect.getmembers(example):
    if name.startswith("__"):
        continue
    print("{} : {!r}".format(name, data))

for name, data in inspect.getmembers(example, inspect.isclass):
    print("{} : {!r}".format(name, data))

pprint(inspect.getmembers(example.A, inspect.isfunction))

a = example.A(name="inspect_getmembers")
pprint(inspect.getmembers(a, inspect.ismethod))
