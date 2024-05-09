""" Command for translating text """

import click
import requests
from lumen.model import translator


@click.command()
@click.option(
    "-t",
    "--text",
    help="Text to summarize",
)
@click.option(
    "--frm",
    default="English",
    type=click.Choice(
        ["English", "Deutsch", "French", "Romanian"],
        case_sensitive=False,
    ),
    help="Language to translate from",
)
@click.option(
    "--to",
    default="French",
    type=click.Choice(
        ["English", "Deutsch", "French", "Romanian"],
        case_sensitive=False,
    ),
    help="Language to translate to",
)
@click.option(
    "-f",
    "--file",
    type=click.Path(exists=True, dir_okay=False),
    help="File to translate",
)
@click.option("-u", "--url", help="URL to translate")
def translate(text: str, frm: str, to: str, file: str, url: str):
    """Translate text"""

    txt: str = f"translate {frm} to {to}: "

    if text:
        txt += text

    elif file:
        txt = open(file, "r").read()

    elif url:
        response = requests.get(url)

        if response.ok:
            pass

        else:
            click.Abort("Invalid URL")

    click.echo("Translating...")

    translation = translator(txt, max_length=512)
    click.echo(translation[0]["translation_text"])

    click.echo(click.style("Done!", fg="green", bold=True))
