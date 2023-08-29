def load_srt(filename: str, remove_blank: bool = True) -> list[str]:
    with open(filename, "r") as f:
        text = f.readlines()

    if remove_blank:
        text = list(filter(lambda line: line != "\n", text))
        text = list(map(lambda line: line.replace("\n", ""), text))

    return text
