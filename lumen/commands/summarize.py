""" Command for summarizing text """

import click
from lumen.model import summarizer
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
    """Summarize text"""

    txt: str = "summarize: "

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

    click.echo("Summarizing...")

    summary = summarizer(txt, max_length=2048)
    click.echo(len(txt))
    click.echo(len(summary[0]["summary_text"]))
    click.echo(summary[0]["summary_text"])

    click.echo(click.style("Done!", fg="green", bold=True))
