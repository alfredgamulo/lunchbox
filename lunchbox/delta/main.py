import typer
from lunchbox.delta.modules import commands

app = typer.Typer(help="Lunchbox 🍱")

for sub_command in commands:
    app.add_typer(sub_command)

if __name__ == "__main__":
    app()
