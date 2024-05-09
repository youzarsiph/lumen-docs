""" Command for summarizing text """

import click
import requests
from lumen.model import summarizer


@click.command()
@click.option(
    "-t",
    "--text",
    help="Text to summarize",
)
@click.option(
    "-f",
    "--file",
    type=click.Path(exists=True, dir_okay=False),
    help="File to summarize",
)
@click.option("-u", "--url", help="URL to summarize")
def summarize(text: str, file: str, url: str):
    """Summarize text"""

    txt: str = "summarize: "

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

    click.echo("Summarizing...")

    summary = summarizer(txt, max_length=512)
    click.echo(len(text))
    click.echo(len(summary[0]["summary_text"]))
    click.echo(summary[0]["summary_text"])

    click.echo(click.style("Done!", fg="green", bold=True))
