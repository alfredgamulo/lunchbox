import typer

from . import main

app = typer.Typer(name="chocolate")

app.add_typer(main.app)
