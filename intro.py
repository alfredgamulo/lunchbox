from dataclasses import dataclass

from rich import inspect
from rich.console import Console
from rich.markdown import Markdown


@dataclass
class Whoami:
    _name: str
    _job: str
    _company: str
    _past: dict
    _hobbies: dict


if __name__ == "__main__":
    me = Whoami(
        "Alfred Gamulo",
        "Principal Engineer",
        "Stacklet",
        {
            "Amazon": [
                "CloudHSM",
                "Inspector",
            ],
            "Capital One": ["Cloud-Custodian", "DX Gateway"],
        },
        {
            "Programming": ["Python", "Lua", "Infrastructure"],
            "Hacking": ["InfoSec", "Cryptography", "Wi-Fi/RF", "Locksport"],
            "Conferences": ["ShmooCon", "BSides", "DEF CON", "Re:Invent"],
        },
    )
    inspect(me)

    while input() != "":
        continue

    console = Console()
    with open("README.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)

    while input() != "":
        continue

    with open("NOTES.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)
