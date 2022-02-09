import typer

from . import main

app = typer.Typer(name="strawberry")

app.add_typer(main.app)
