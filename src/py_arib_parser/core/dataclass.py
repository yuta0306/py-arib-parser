from dataclasses import dataclass


@dataclass
class Time(object):
    hour: int
    minute: int
    second: int
    millisecond: int

    def __repr__(self) -> str:
        return f"""Time(
    hour        = {self.hour}
    minute      = {self.minute}
    second      = {self.second}
    millisecond = {self.millisecond}
)"""


@dataclass
class Text(object):
    content: str
    size: int | None = None
    color: str | None = None

    def __repr__(self) -> str:
        return f"""Text(
    content = {self.content}
    size    = {self.size}
    color   = {self.color}
)"""


@dataclass
class Caption(object):
    start: Time
    end: Time
    text: list[Text]

    def __repr__(self) -> str:
        start = self.start
        end = self.end
        return f"""Caption(
    start = {start.hour:02d}:{start.minute:02d}:{start.second:02d}.{start.millisecond:03d}
    end   = {end.hour:02d}:{end.minute:02d}:{end.second:02d}.{end.millisecond:03d}
    text  = {self.text}
)"""
