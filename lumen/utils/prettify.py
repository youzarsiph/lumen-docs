""" Prettify model output """


def prettify(text: str) -> str:
    """Pretty print model output"""

    return ". ".join(
        [t.strip().replace(". ", ".").replace(" .", ". ") for t in text.split(" . ")]
    )
