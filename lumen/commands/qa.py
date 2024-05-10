""" Command question answering """

import click
from lumen.model import question_answerer
from lumen.utils.process import process


@click.command()
@click.option(
    "-q",
    "--question",
    required=True,
    help="Question to answer",
)
@click.option(
    "-t",
    "--text",
    help="Text that the answer will be extracted from",
)
@click.option(
    "-f",
    "--file",
    type=click.File(mode="r", encoding="utf-8"),
    help="File that the answer will be extracted from",
)
@click.option(
    "-u",
    "--url",
    help="URL that the answer will be extracted from",
)
def qa(question: str, text: str, file: str, url: str):
    """Answer questions"""

    ctx: str = ""

    if text:
        ctx = process("text", text)

    elif file:
        ctx = process("file", file)

    elif url:
        ctx = process("url", url)
    else:
        click.echo(
            click.style("Error: ", fg="red", bold=True)
            + "No text, file or url provided"
        )
        return

    click.echo("Summarizing...")

    answer = question_answerer({"context": ctx, "question": question})
    click.echo(answer)

    click.echo(click.style("Done!", fg="green", bold=True))
