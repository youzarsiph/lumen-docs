""" Process input text """

from io import TextIOWrapper
from lumen.utils import parser


def process(type: str, input: str | TextIOWrapper) -> str:
    """Process input text"""

    text: str = ""

    match type:
        case "text":
            text = parser.parse_text(str(input))

        case "file":
            text = parser.parse_file(input)

        case "url":
            text = parser.parse_url(str(input))

        case _:
            raise ValueError("Invalid type")

    return text
