def buildhash() -> str: ...
def open_backend(data: bytes) -> Backend: ...
def initialize_logging(log_file: str | None) -> Backend: ...
def syncserver() -> None: ...

class Backend:
    @classmethod
    def command(self, service: int, method: int, data: bytes) -> bytes: ...
    def db_command(self, data: bytes) -> bytes: ...
