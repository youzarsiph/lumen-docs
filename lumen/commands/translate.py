""" Command for translating text """

import click
from lumen.model import translator
from lumen.utils.process import process


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
    type=click.File(mode="r", encoding="utf-8"),
    help="File to translate",
)
@click.option("-u", "--url", help="URL to translate")
def translate(text: str, frm: str, to: str, file: str, url: str):
    """Translate text"""

    txt: str = f"translate {frm} to {to}: "

    if text:
        txt += process("text", text)

    elif file:
        txt += process("file", file)

    elif url:
        txt += process("url", url)
    else:
        click.echo(
            click.style("Error: ", fg="red", bold=True)
            + "No text, file or url provided"
        )
        return

    click.echo("Translating...")

    translation = translator(txt, max_length=512)
    click.echo(translation[0]["translation_text"])

    click.echo(click.style("Done!", fg="green", bold=True))
