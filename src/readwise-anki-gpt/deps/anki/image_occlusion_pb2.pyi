"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetImageForOcclusionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    path: builtins.str
    def __init__(
        self,
        *,
        path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path"]) -> None: ...

global___GetImageForOcclusionRequest = GetImageForOcclusionRequest

@typing_extensions.final
class GetImageForOcclusionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    name: builtins.str
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "name", b"name"]) -> None: ...

global___GetImageForOcclusionResponse = GetImageForOcclusionResponse

@typing_extensions.final
class AddImageOcclusionNoteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_PATH_FIELD_NUMBER: builtins.int
    OCCLUSIONS_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    BACK_EXTRA_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    NOTETYPE_ID_FIELD_NUMBER: builtins.int
    image_path: builtins.str
    occlusions: builtins.str
    header: builtins.str
    back_extra: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    notetype_id: builtins.int
    def __init__(
        self,
        *,
        image_path: builtins.str = ...,
        occlusions: builtins.str = ...,
        header: builtins.str = ...,
        back_extra: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        notetype_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["back_extra", b"back_extra", "header", b"header", "image_path", b"image_path", "notetype_id", b"notetype_id", "occlusions", b"occlusions", "tags", b"tags"]) -> None: ...

global___AddImageOcclusionNoteRequest = AddImageOcclusionNoteRequest

@typing_extensions.final
class GetImageOcclusionNoteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_ID_FIELD_NUMBER: builtins.int
    note_id: builtins.int
    def __init__(
        self,
        *,
        note_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["note_id", b"note_id"]) -> None: ...

global___GetImageOcclusionNoteRequest = GetImageOcclusionNoteRequest

@typing_extensions.final
class GetImageOcclusionNoteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ImageOcclusionProperty(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class ImageOcclusionShape(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SHAPE_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        shape: builtins.str
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetImageOcclusionNoteResponse.ImageOcclusionProperty]: ...
        def __init__(
            self,
            *,
            shape: builtins.str = ...,
            properties: collections.abc.Iterable[global___GetImageOcclusionNoteResponse.ImageOcclusionProperty] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["properties", b"properties", "shape", b"shape"]) -> None: ...

    @typing_extensions.final
    class ImageOcclusion(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SHAPES_FIELD_NUMBER: builtins.int
        @property
        def shapes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetImageOcclusionNoteResponse.ImageOcclusionShape]: ...
        def __init__(
            self,
            *,
            shapes: collections.abc.Iterable[global___GetImageOcclusionNoteResponse.ImageOcclusionShape] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["shapes", b"shapes"]) -> None: ...

    @typing_extensions.final
    class ImageOcclusionNote(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        IMAGE_DATA_FIELD_NUMBER: builtins.int
        OCCLUSIONS_FIELD_NUMBER: builtins.int
        HEADER_FIELD_NUMBER: builtins.int
        BACK_EXTRA_FIELD_NUMBER: builtins.int
        TAGS_FIELD_NUMBER: builtins.int
        IMAGE_FILE_NAME_FIELD_NUMBER: builtins.int
        image_data: builtins.bytes
        @property
        def occlusions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetImageOcclusionNoteResponse.ImageOcclusion]: ...
        header: builtins.str
        back_extra: builtins.str
        @property
        def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        image_file_name: builtins.str
        def __init__(
            self,
            *,
            image_data: builtins.bytes = ...,
            occlusions: collections.abc.Iterable[global___GetImageOcclusionNoteResponse.ImageOcclusion] | None = ...,
            header: builtins.str = ...,
            back_extra: builtins.str = ...,
            tags: collections.abc.Iterable[builtins.str] | None = ...,
            image_file_name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["back_extra", b"back_extra", "header", b"header", "image_data", b"image_data", "image_file_name", b"image_file_name", "occlusions", b"occlusions", "tags", b"tags"]) -> None: ...

    NOTE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def note(self) -> global___GetImageOcclusionNoteResponse.ImageOcclusionNote: ...
    error: builtins.str
    def __init__(
        self,
        *,
        note: global___GetImageOcclusionNoteResponse.ImageOcclusionNote | None = ...,
        error: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error", b"error", "note", b"note", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "note", b"note", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["note", "error"] | None: ...

global___GetImageOcclusionNoteResponse = GetImageOcclusionNoteResponse

@typing_extensions.final
class UpdateImageOcclusionNoteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_ID_FIELD_NUMBER: builtins.int
    OCCLUSIONS_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    BACK_EXTRA_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    note_id: builtins.int
    occlusions: builtins.str
    header: builtins.str
    back_extra: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        note_id: builtins.int = ...,
        occlusions: builtins.str = ...,
        header: builtins.str = ...,
        back_extra: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["back_extra", b"back_extra", "header", b"header", "note_id", b"note_id", "occlusions", b"occlusions", "tags", b"tags"]) -> None: ...

global___UpdateImageOcclusionNoteRequest = UpdateImageOcclusionNoteRequest

@typing_extensions.final
class GetImageOcclusionFieldsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTETYPE_ID_FIELD_NUMBER: builtins.int
    notetype_id: builtins.int
    def __init__(
        self,
        *,
        notetype_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["notetype_id", b"notetype_id"]) -> None: ...

global___GetImageOcclusionFieldsRequest = GetImageOcclusionFieldsRequest

@typing_extensions.final
class GetImageOcclusionFieldsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> global___ImageOcclusionFieldIndexes: ...
    def __init__(
        self,
        *,
        fields: global___ImageOcclusionFieldIndexes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fields", b"fields"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields"]) -> None: ...

global___GetImageOcclusionFieldsResponse = GetImageOcclusionFieldsResponse

@typing_extensions.final
class ImageOcclusionFieldIndexes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OCCLUSIONS_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    BACK_EXTRA_FIELD_NUMBER: builtins.int
    occlusions: builtins.int
    image: builtins.int
    header: builtins.int
    back_extra: builtins.int
    def __init__(
        self,
        *,
        occlusions: builtins.int = ...,
        image: builtins.int = ...,
        header: builtins.int = ...,
        back_extra: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["back_extra", b"back_extra", "header", b"header", "image", b"image", "occlusions", b"occlusions"]) -> None: ...

global___ImageOcclusionFieldIndexes = ImageOcclusionFieldIndexes