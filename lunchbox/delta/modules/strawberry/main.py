import typer

app = typer.Typer(name="turtle")


@app.command()
def execute():
    typer.echo("Do something strawberry")


if __name__ == "__main__":
    app()
