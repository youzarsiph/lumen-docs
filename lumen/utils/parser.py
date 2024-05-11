""" Utility to parse input text """

from io import TextIOWrapper
import requests
from bs4 import BeautifulSoup


def parse_text(text: str):
    """Parse input text"""

    return text.strip()


def parse_file(file: TextIOWrapper) -> str:
    """Process input file"""

    return parse_text(file.read())


def parse_url(url: str) -> str:
    """Process input url"""

    response = requests.get(url)

    if not response.ok:
        raise Exception("Error fetching url")

    soup = BeautifulSoup(response.text, "html.parser")

    return parse_text(" ".join(soup.stripped_strings))
