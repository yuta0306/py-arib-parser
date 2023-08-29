from html.parser import HTMLParser

from src.py_arib_parser.core.dataclass import Text


class ARIBParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.text: list[Text] = []
        self.nest: int = 0
        self.attrs: dict[str, int | str] = {}
        self.content: str = ""

    def feed(self, data: str) -> None:
        self.text = []
        self.nest = 0
        self.attrs = {}
        self.content = ""
        return super().feed(data)

    def handle_starttag(self, tag, attrs):
        self.attrs.update(dict(attrs))
        self.nest += 1

    def handle_endtag(self, tag):
        self.nest -= 1
        if self.nest == 0:
            self.text.append(Text(content=self.content, **self.attrs))
            self.content = ""
            self.attrs = {}

    def handle_data(self, data):
        self.content += data

    def get_results(self) -> list[Text]:
        return self.text
