import textwrap

def sanitize_json(text: str) -> str:
    sanitezed = text.replace("\"", "\'") \
        .replace("{", "") \
        .replace("}", "") \
        .replace("[", "") \
        .replace("]", "") \
        .replace("]", "")

    sanitezed = "".join(textwrap.wrap(sanitezed))

    return sanitezed
