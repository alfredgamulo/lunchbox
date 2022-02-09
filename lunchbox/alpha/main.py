import argparse
import getopt
import sys

from rich.console import Console


def builtin():
    console = Console()
    # sys.argv
    console.print("sys.argv:\n", style="bold underline")
    print(sys.argv[1:])

    # argparse
    console.print("\nargparse:\n", style="bold underline")
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string")
    args = parser.parse_args()
    print(args.echo)

    # getopt
    # console.print("\ngetopt:\n", style="bold underline")
    # print(getopt.getopt(sys.argv[1:], "e:", ["echo="]))

    print()


if __name__ == "__main__":
    builtin()
