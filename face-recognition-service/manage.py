from flask.cli import FlaskGroup
from src.app import create_app
import click

app = create_app('dev')

def create_app_cli():
    return create_app('dev')

@click.group(cls=FlaskGroup, create_app=create_app_cli)
def cli():
    """Management script for the Flask application."""


@cli.command("run")
@click.option('-h', '--host', default='127.0.0.1', help='The interface to bind to.')
@click.option('-p', '--port', default=5000, help='The port to bind to.')
def run_server(host, port):
    app = create_app('dev')
    app.run(host=host, port=port)

if __name__ == "__main__":
    cli()