import typer

from . import main

app = typer.Typer(name="vanilla")

app.add_typer(main.app)
