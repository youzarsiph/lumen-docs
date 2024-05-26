""" Command for translating text """

import click
from lumen import client
from lumen.utils.prettify import prettify
from lumen.utils.process import process


@click.command()
@click.option(
    "-i",
    "--text",
    help="Text to translate",
)
@click.option(
    "-f",
    "--file",
    type=click.File(mode="r", encoding="utf-8"),
    help="File to translate",
)
@click.option(
    "-u",
    "--url",
    help="URL to translate",
)
@click.option(
    "-s",
    "--source",
    default="en_XX",
    help="Source language",
)
@click.option(
    "-t",
    "--target",
    default="ar_XX",
    help="Target language",
)
def translate(text: str, source: str, target: str, file: str, url: str):
    """
    Convert text from one language to another.

    Example:\n
    lumen translate -i "My name is Sarah Jessica Parker but you can call me Jessica" -s en_XX -t ar_XX\n
    lumen translate -f input.txt -s en_XX -t ar_XX\n
    lumen translate -u https://example.com -s en_XX -t ar_XX
    """

    txt: str = ""

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

    translation = client.translation(prettify(txt), src_lang=source, tgt_lang=target)

    click.echo(
        click.style("Translation: ", fg="blue", bold=True)
        + prettify(translation.translation_text)
    )

    click.echo(click.style("Done!", fg="green", bold=True))
