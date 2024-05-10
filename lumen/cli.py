""" LumenDocs CLI """

import click
from lumen import commands


@click.group()
def cli():
    """Guiding Light for Developers."""


cli.add_command(commands.qa)
cli.add_command(commands.summarize)
cli.add_command(commands.translate)


if __name__ == "__main__":
    cli()
