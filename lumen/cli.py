""" LumenDocs CLI """

import click
from lumen.commands import commands


@click.group()
def cli():
    """Guiding Light for Developers."""


for command in commands:
    cli.add_command(command)


if __name__ == "__main__":
    cli()
