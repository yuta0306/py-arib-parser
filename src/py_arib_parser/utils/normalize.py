from src.py_arib_parser.core.dataclass import Text


def normalize_text(texts: list[Text]) -> list[Text]:
    normalized = []
    color = texts[0].color
    size = texts[0].size
    merged = ""
    for text in texts:
        if color == text.color:
            merged += text.content
        else:
            normalized.append(Text(content=merged, size=size, color=color))
            color = text.color
            size = text.size
            merged = text.content
    if merged != "":
        normalized.append(Text(content=merged, size=size, color=color))
    return normalized
