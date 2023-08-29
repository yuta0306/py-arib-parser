from src.py_arib_parser.core.dataclass import Caption


def print_caption(caption: Caption) -> None:
    start = caption.start
    end = caption.end
    print(
        f"\033[4m{start.hour:02d}:{start.minute:02d}:{start.second:02d},{start.millisecond:03d} --> "
        f"{end.hour:02d}:{end.minute:02d}:{end.second:02d},{end.millisecond:03d}\033[0m"
    )
    for text in caption.text:
        color = text.color
        if color is None:
            color = "ffffff"
        color = color.replace("#", "")
        r = int(color[:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:], 16)
        print(f"\033[38;2;{r};{g};{b}m{text.content}\033[0m")
    print()
