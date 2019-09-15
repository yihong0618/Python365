import argparse

parser = argparse.ArgumentParser(description="Example with nonoptional arguments")

parser.add_argument("count", action="store", type=int)
parser.add_argument("units", action="store")


parser.add_argument(
    "-s", action="store", dest="simple_value", help="Store a simple value"
)

parser.add_argument(
    "-c",
    action="store_const",
    dest="constant_value",
    const="value-to-store",
    help="Store a constant value",
)

parser.add_argument(
    "-t",
    action="store_true",
    default=False,
    dest="boolean_t",
    help="Set a switch to true",
)
parser.add_argument(
    "-f",
    action="store_false",
    default=True,
    dest="boolean_f",
    help="Set a switch to false",
)

parser.add_argument(
    "-a",
    action="append",
    dest="collection",
    default=[],
    help="Add repeated values to a list",
)

parser.add_argument(
    "-A",
    action="append_const",
    dest="const_collection",
    const="value-1-to-append",
    default=[],
    help="Add different values to list",
)
parser.add_argument(
    "-B",
    action="append_const",
    dest="const_collection",
    const="value-2-to-append",
    help="Add different values to list",
)

parser.add_argument("--version", action="version", version="%(prog)s 1.0")
