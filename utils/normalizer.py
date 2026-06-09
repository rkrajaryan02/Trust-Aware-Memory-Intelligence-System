import re


def normalize_text(text):

    text = text.lower()

    text = text.replace(
        "five million dollars",
        "$5m"
    )

    text = text.replace(
        "eight million dollars",
        "$8m"
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()