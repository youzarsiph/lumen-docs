""" Command for Question Answering """

import click
from lumen import client
from lumen.utils.prettify import prettify
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
    """
    Retrieve the answer to a question from a given text.

    Examples:\n
    lumen qa -q "What's my name?" -t "My name is Clara and I live in Berkeley."\n
    lumen qa -q "What's my name?" -f input.txt\n
    lumen qa -q "What's my name?" -u https://example.com
    """

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

    click.echo(click.style("Extracting the answer...", fg="yellow", bold=True))

    result = client.question_answering(context=ctx, question=question)

    click.echo(click.style("Answer: ", fg="blue", bold=True) + prettify(result.answer))

    click.echo(click.style("Done!", fg="green", bold=True))
