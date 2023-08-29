import argparse
import re

from py_arib_parser.core import ARIBParser, Caption, Text, Time
from py_arib_parser.utils import load_srt, normalize_text, print_caption


def get_text(text: str) -> list[Text]:
    parser = ARIBParser()
    parser.feed(text)

    return parser.get_results()


def get_caption(filename: str, *, normalize: bool = False) -> dict[int, Caption]:
    srt = load_srt(filename=filename)

    captions = {}
    for idx in range(0, len(srt), 3):
        index = int(srt[idx])
        hs, ms, ss, mss, he, me, se, mse = [
            int(s) for s in re.split(r":|,|\s+-->\s+", srt[idx + 1])
        ]
        raw = srt[idx + 2]
        start = Time(hour=hs, minute=ms, second=ss, millisecond=mss)
        end = Time(hour=he, minute=me, second=se, millisecond=mse)
        caption = Caption(start=start, end=end, text=get_text(raw))

        if normalize:
            caption.text = normalize_text(caption.text)
        captions[index] = caption
    return captions


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    parser.add_argument(
        "--normalize",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="text normalization, default=True",
    )
    args = parser.parse_args()

    captions = get_caption(
        args.input,
        normalize=args.normalize,
    )

    for caption in captions.values():
        print_caption(caption)
