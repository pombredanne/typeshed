class sha384(object):
    name = ...  # type: str
    block_size = ...  # type: int
    digest_size = ...  # type: int
    digestsize = ...  # type: int
    def copy(self) -> "sha384": ...
    def digest(self) -> str: ...
    def hexdigest(self) -> str: ...
    def update(self, arg: str) -> None: ...

class sha512(object):
    name = ...  # type: str
    block_size = ...  # type: int
    digest_size = ...  # type: int
    digestsize = ...  # type: int
    def copy(self) -> "sha512": ...
    def digest(self) -> str: ...
    def hexdigest(self) -> str: ...
    def update(self, arg: str) -> None: ...