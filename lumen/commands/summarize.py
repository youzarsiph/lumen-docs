""" Command for Summarization """

import click
from lumen import client
from lumen.utils.prettify import prettify
from lumen.utils.process import process


@click.command()
@click.option(
    "-t",
    "--text",
    help="Text to summarize",
)
@click.option(
    "-f",
    "--file",
    type=click.File(mode="r", encoding="utf-8"),
    help="File to summarize",
)
@click.option("-u", "--url", help="URL to summarize")
def summarize(text: str, file: str, url: str):
    """
    Generate a summary of a given text.

    Examples:\n
    lumen summarize -t "The Eiffel tower..."\n
    lumen summarize -f input.txt\n
    lumen summarize -u "https://example.com"
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

    click.echo(click.style("Summarizing...", fg="yellow", bold=True))

    summary = client.summarization(txt)

    click.echo(
        click.style("Summary: ", fg="blue", bold=True) + prettify(summary.summary_text)
    )

    click.echo(click.style("Done!", fg="green", bold=True))
