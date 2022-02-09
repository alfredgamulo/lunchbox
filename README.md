# lunchbox: CLI Examples

## Alpha
Basic. This module will show what "batteries" are included in Python for taking input and creating CLIs.
* sys.argv
* argparse
* getopt

N.B. I've been so accustomed to using click or typer that these examples are rather poor. I didn't want to spend too much time on trying to make these examples more complex. 


## Bravo
Stage 1. This module will explore using Click -- the "Command Line Interface Creation Kit."
Click in three points (according to [Click](https://click.palletsprojects.com/en/8.0.x/)):
* arbitrary nesting of commands
* automatic help page generation
* supports lazy loading of subcommands at runtime

## Charlie
Stage 2. This module builds upon the first two by implementing Typer, the "FastAPI of CLIs."
Key features of Typer (according to [Typer](https://typer.tiangolo.com/)):
* **Intuitive to write**: Great editor support. Completion everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
* **Easy to use**: It's easy to use for the final users. Automatic help, and automatic completion for all shells.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Start Simple**: The simplest example adds only 2 lines of code to your app: 1 import, 1 function call.
* **Grow large**: Grow in complexity as much as you want, create arbitrarily complex trees of commands and groups of subcommands, with options and arguments.


## Delta
Legendary.
