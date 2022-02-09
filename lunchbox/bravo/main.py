import click


@click.group()
def cli():
    pass


@cli.command(
    short_help="Run this command to initialize the DB.", help="detailed help message"
)
def initdb():
    click.echo("Initialized the database")


@cli.command(
    short_help="Run this command to drop the DB.", help="detailed help message"
)
def dropdb():
    click.echo("Dropped the database")


@cli.command()
@click.option("--role", prompt="The role to grant privileges", type=str)
@click.option(
    "--object-type",
    "-o",
    type=click.Choice(["schema", "table", "function"]),
    multiple=True,
)
@click.option(
    "--privilege",
    "-p",
    type=click.Choice(["ALL", "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE"]),
    multiple=True,
)
def grantrole(role, object_type, privilege):
    click.echo(f"Role: {role}")
    click.echo(f"Object Types: {object_type}")
    click.echo(f"Privileges: {privilege}")


@cli.command()
@click.option("--user", prompt="The user")
@click.option(
    "--password", prompt="The password", hide_input=True, confirmation_prompt=True
)
def createuser(user, password):
    click.echo(f"User: {user}")
    click.echo(f"Password: {password}")


if __name__ == "__main__":
    cli()
