""" Command for Visual Question Answering """

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
def vqa(question: str, file: str, url: str):
    """
    Answering open-ended questions based on an image.

    Example:\n
    lumen vqa -q "What is the animal doing?" -f tiger.jpg\n
    lumen vqa -q "What is the animal doing?" -u "https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg"
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

    result = client.visual_question_answering(image=input, question=question)

    click.echo(
        click.style("Answer: ", fg="blue", bold=True)
        + "\n".join([i.answer for i in result])
    )

    click.echo(click.style("Done!", fg="green", bold=True))
