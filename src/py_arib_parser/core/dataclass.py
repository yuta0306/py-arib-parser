from dataclasses import dataclass


@dataclass
class Time(object):
    hour: int
    minute: int
    second: int
    millisecond: int


@dataclass
class Text(object):
    content: str
    size: int | None = None
    color: str | None = None


@dataclass
class Caption(object):
    start: Time
    end: Time
    text: list[Text]
