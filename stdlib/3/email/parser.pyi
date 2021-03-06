# Stubs for email.parser (Python 3.4)

from typing import Callable, Optional, TextIO, BinaryIO
import email.feedparser
from email.message import Message
from email.policy import Policy
import sys

FeedParser = email.feedparser.FeedParser
BytesFeedParser = email.feedparser.BytesFeedParser

class Parser:
    if sys.version_info >= (3, 3):
        def __init__(self, _class: Callable[[], Message] = ..., *,
                     policy: Policy = ...) -> None: ...
    else:
        # TODO `strict` is positional
        def __init__(self,  # type: ignore
                     _class: Callable[[], Message] = ..., *,
                     strict: Optional[bool]) -> None: ...
    def parse(self, fp: TextIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

class HeaderParser(Parser):
    if sys.version_info >= (3, 3):
        def __init__(self, _class: Callable[[], Message] = ..., *,
                     policy: Policy = ...) -> None: ...
    else:
        # TODO `strict` is positional
        def __init__(self,  # type: ignore
                     _class: Callable[[], Message] = ..., *,
                     strict: Optional[bool]) -> None: ...
    def parse(self, fp: TextIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

if sys.version_info >= (3, 3):
    class BytesHeaderParser(BytesParser):
        if sys.version_info >= (3, 3):
            def __init__(self, _class: Callable[[], Message] = ..., *,
                         policy: Policy = ...) -> None: ...
        else:
            # TODO `strict` is positional
            def __init__(self,  # type: ignore
                         _class: Callable[[], Message] = ..., *,
                         strict: Optional[bool]) -> None: ...
        def parse(self, fp: BinaryIO, headersonly: bool = ...) -> Message: ...
        def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

if sys.version_info >= (3, 2):
    class BytesParser:
        if sys.version_info >= (3, 3):
            def __init__(self, _class: Callable[[], Message] = ..., *,
                         policy: Policy = ...) -> None: ...
        else:
            # TODO `strict` is positional
            def __init__(self,  # type: ignore
                         _class: Callable[[], Message] = ..., *,
                         strict: Optional[bool]) -> None: ...
        def parse(self, fp: BinaryIO, headersonly: bool = ...) -> Message: ...
        def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

