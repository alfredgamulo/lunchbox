import typer

app = typer.Typer(name="turtle")


@app.command()
def execute():
    typer.echo("Do something vanilla-y??")


if __name__ == "__main__":
    app()
