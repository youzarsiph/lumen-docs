""" Command for translating text """

import click
from lumen.model import translator
from lumen.utils.prettify import prettify
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

    click.echo(click.style("Translating...", fg="yellow", bold=True))

    translation = translator(prettify(txt))

    click.echo(
        click.style("Summary: ", fg="blue", bold=True)
        + prettify("\n".join([t["translation_text"] for t in translation]))
    )

    click.echo(click.style("Done!", fg="green", bold=True))
