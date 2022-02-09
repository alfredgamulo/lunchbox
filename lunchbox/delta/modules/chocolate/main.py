import typer

app = typer.Typer(name="turtle")


@app.command()
def execute():
    typer.echo("Do something chocolatey")


if __name__ == "__main__":
    app()
