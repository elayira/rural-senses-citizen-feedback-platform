import os
import click
from flask.cli import with_appcontext


@click.command("createSuperAdmin")
@with_appcontext
def createSuperAdmin():
    """Create a new admin user"""
    from src.user.service import UserService

    click.echo("create user")
    UserService().createuser(
        username=os.getenv('DEFAULT_ADMIN_USERNAME'), 
        password=os.getenv('DEFAULT_ADMIN_PASSWORD'), 
    )
    click.echo("created user admin")
