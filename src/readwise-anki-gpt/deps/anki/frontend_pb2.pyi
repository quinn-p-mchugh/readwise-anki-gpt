"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""
import anki.scheduler_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SchedulingStatesWithContext(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATES_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    @property
    def states(self) -> anki.scheduler_pb2.SchedulingStates: ...
    @property
    def context(self) -> anki.scheduler_pb2.SchedulingContext: ...
    def __init__(
        self,
        *,
        states: anki.scheduler_pb2.SchedulingStates | None = ...,
        context: anki.scheduler_pb2.SchedulingContext | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context", b"context", "states", b"states"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["context", b"context", "states", b"states"]) -> None: ...

global___SchedulingStatesWithContext = SchedulingStatesWithContext

@typing_extensions.final
class SetSchedulingStatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    STATES_FIELD_NUMBER: builtins.int
    key: builtins.str
    @property
    def states(self) -> anki.scheduler_pb2.SchedulingStates: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        states: anki.scheduler_pb2.SchedulingStates | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["states", b"states"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "states", b"states"]) -> None: ...

global___SetSchedulingStatesRequest = SetSchedulingStatesRequest
