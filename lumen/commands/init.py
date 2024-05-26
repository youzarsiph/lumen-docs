""" Initialize HF token """

import os
import platform
import subprocess
import click


@click.command()
@click.option(
    "-t",
    "--token",
    required=True,
    help="Hugging Face token",
)
def init(token: str):
    """
    Set HF Token env variable

    Example:\n
    lumen init -t "hf_**********************************"
    """

    click.echo(click.style("Initializing...", fg="yellow", bold=True))

    if platform.system() == "Windows":
        subprocess.check_call(["setx", "HF_TOKEN", token], shell=True)

    elif platform.system() == "Darwin" or platform.system() == "Linux":
        subprocess.check_call(["launchctl", "setenv", "HF_TOKEN", token])

    else:
        click.echo(click.style("Error: ", fg="red", bold=True) + "Unsupported OS")
        return

    os.environ["HF_TOKEN"] = token

    click.echo(click.style("Done!", fg="green", bold=True))
