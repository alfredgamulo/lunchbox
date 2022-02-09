import typer

app = typer.Typer(help="Charlie 🤯")


@app.command()
def createuser(
    user: str,
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
    local: bool = True,
):
    typer.echo(f"User: {user}")
    typer.echo(f"Password: {password}")
    typer.echo(f"Is local: {local}")


@app.command()
def createuser2(
    user: str = typer.Option(..., "--user"),
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
    local: bool = True,
):
    typer.echo(f"User: {user}")
    typer.echo(f"Password: {password}")
    typer.echo(f"Is local: {local}")


@app.command()
def placeholder():
    typer.echo("Do nothing.")


if __name__ == "__main__":
    app()
