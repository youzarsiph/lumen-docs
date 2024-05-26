""" Command for Document Question Answering """

import click
from lumen import client


@click.command()
@click.option(
    "-q",
    "--question",
    required=True,
    help="Question to answer",
)
@click.option(
    "-f",
    "--file",
    type=click.File(mode="r", encoding="utf-8"),
    help="Image file that the answer will be extracted from",
)
@click.option(
    "-u",
    "--url",
    help="Image URL that the answer will be extracted from",
)
def dqa(question: str, file: str, url: str):
    """
    Answer questions on document images.

    Example:\n
    lumen dqa -q "What is the invoice number?" -f image.png\n
    lumen dqa -q "What is the invoice number?" -u "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png"
    """

    input = None

    if file:
        input = file

    elif url:
        input = url

    else:
        click.echo(
            click.style("Error: ", fg="red", bold=True) + "No file or url provided"
        )
        return

    click.echo(click.style("Extracting the answer...", fg="yellow", bold=True))

    result = client.document_question_answering(image=input, question=question)

    click.echo(
        click.style("Answer: ", fg="blue", bold=True)
        + "\n".join([i.answer for i in result])
    )

    click.echo(click.style("Done!", fg="green", bold=True))
