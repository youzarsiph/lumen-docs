""" Command for Automatic Speech Recognition """

import click
from lumen import client


@click.command()
@click.option(
    "-f",
    "--file",
    type=click.File(mode="r", encoding="utf-8"),
    help="The content to transcribe. It can be raw audio bytes or local audio file.",
)
@click.option(
    "-u",
    "--url",
    help="The content to transcribe. It a URL to an audio file.",
)
def transcribe(question: str, file: str, url: str):
    """
    Perform automatic speech recognition (ASR or audio-to-text) on the given audio content.

    Example:\n
    lumen transcribe -f hello_world.flac\n
    lumen transcribe -u "https://example.com/hello_world.flac"
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

    click.echo(click.style("Transcribing...", fg="yellow", bold=True))

    result = client.automatic_speech_recognition(audio=input)

    click.echo(click.style("Answer: ", fg="blue", bold=True) + result.text)

    click.echo(click.style("Done!", fg="green", bold=True))
