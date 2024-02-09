"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""
import anki.collection_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class NoteId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NID_FIELD_NUMBER: builtins.int
    nid: builtins.int
    def __init__(
        self,
        *,
        nid: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nid", b"nid"]) -> None: ...

global___NoteId = NoteId

@typing_extensions.final
class NoteIds(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_IDS_FIELD_NUMBER: builtins.int
    @property
    def note_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        note_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["note_ids", b"note_ids"]) -> None: ...

global___NoteIds = NoteIds

@typing_extensions.final
class Note(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    GUID_FIELD_NUMBER: builtins.int
    NOTETYPE_ID_FIELD_NUMBER: builtins.int
    MTIME_SECS_FIELD_NUMBER: builtins.int
    USN_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    id: builtins.int
    guid: builtins.str
    notetype_id: builtins.int
    mtime_secs: builtins.int
    usn: builtins.int
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        guid: builtins.str = ...,
        notetype_id: builtins.int = ...,
        mtime_secs: builtins.int = ...,
        usn: builtins.int = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        fields: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields", "guid", b"guid", "id", b"id", "mtime_secs", b"mtime_secs", "notetype_id", b"notetype_id", "tags", b"tags", "usn", b"usn"]) -> None: ...

global___Note = Note

@typing_extensions.final
class AddNoteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_FIELD_NUMBER: builtins.int
    DECK_ID_FIELD_NUMBER: builtins.int
    @property
    def note(self) -> global___Note: ...
    deck_id: builtins.int
    def __init__(
        self,
        *,
        note: global___Note | None = ...,
        deck_id: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["note", b"note"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deck_id", b"deck_id", "note", b"note"]) -> None: ...

global___AddNoteRequest = AddNoteRequest

@typing_extensions.final
class AddNoteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANGES_FIELD_NUMBER: builtins.int
    NOTE_ID_FIELD_NUMBER: builtins.int
    @property
    def changes(self) -> anki.collection_pb2.OpChanges: ...
    note_id: builtins.int
    def __init__(
        self,
        *,
        changes: anki.collection_pb2.OpChanges | None = ...,
        note_id: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["changes", b"changes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["changes", b"changes", "note_id", b"note_id"]) -> None: ...

global___AddNoteResponse = AddNoteResponse

@typing_extensions.final
class AddNotesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUESTS_FIELD_NUMBER: builtins.int
    @property
    def requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AddNoteRequest]: ...
    def __init__(
        self,
        *,
        requests: collections.abc.Iterable[global___AddNoteRequest] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["requests", b"requests"]) -> None: ...

global___AddNotesRequest = AddNotesRequest

@typing_extensions.final
class AddNotesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANGES_FIELD_NUMBER: builtins.int
    NIDS_FIELD_NUMBER: builtins.int
    @property
    def changes(self) -> anki.collection_pb2.OpChanges: ...
    @property
    def nids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        changes: anki.collection_pb2.OpChanges | None = ...,
        nids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["changes", b"changes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["changes", b"changes", "nids", b"nids"]) -> None: ...

global___AddNotesResponse = AddNotesResponse

@typing_extensions.final
class UpdateNotesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTES_FIELD_NUMBER: builtins.int
    SKIP_UNDO_ENTRY_FIELD_NUMBER: builtins.int
    @property
    def notes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Note]: ...
    skip_undo_entry: builtins.bool
    def __init__(
        self,
        *,
        notes: collections.abc.Iterable[global___Note] | None = ...,
        skip_undo_entry: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["notes", b"notes", "skip_undo_entry", b"skip_undo_entry"]) -> None: ...

global___UpdateNotesRequest = UpdateNotesRequest

@typing_extensions.final
class DefaultsForAddingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOME_DECK_OF_CURRENT_REVIEW_CARD_FIELD_NUMBER: builtins.int
    home_deck_of_current_review_card: builtins.int
    def __init__(
        self,
        *,
        home_deck_of_current_review_card: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["home_deck_of_current_review_card", b"home_deck_of_current_review_card"]) -> None: ...

global___DefaultsForAddingRequest = DefaultsForAddingRequest

@typing_extensions.final
class DeckAndNotetype(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DECK_ID_FIELD_NUMBER: builtins.int
    NOTETYPE_ID_FIELD_NUMBER: builtins.int
    deck_id: builtins.int
    notetype_id: builtins.int
    def __init__(
        self,
        *,
        deck_id: builtins.int = ...,
        notetype_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deck_id", b"deck_id", "notetype_id", b"notetype_id"]) -> None: ...

global___DeckAndNotetype = DeckAndNotetype

@typing_extensions.final
class RemoveNotesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_IDS_FIELD_NUMBER: builtins.int
    CARD_IDS_FIELD_NUMBER: builtins.int
    @property
    def note_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def card_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        note_ids: collections.abc.Iterable[builtins.int] | None = ...,
        card_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["card_ids", b"card_ids", "note_ids", b"note_ids"]) -> None: ...

global___RemoveNotesRequest = RemoveNotesRequest

@typing_extensions.final
class ClozeNumbersInNoteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NUMBERS_FIELD_NUMBER: builtins.int
    @property
    def numbers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        numbers: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["numbers", b"numbers"]) -> None: ...

global___ClozeNumbersInNoteResponse = ClozeNumbersInNoteResponse

@typing_extensions.final
class AfterNoteUpdatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NIDS_FIELD_NUMBER: builtins.int
    MARK_NOTES_MODIFIED_FIELD_NUMBER: builtins.int
    GENERATE_CARDS_FIELD_NUMBER: builtins.int
    @property
    def nids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    mark_notes_modified: builtins.bool
    generate_cards: builtins.bool
    def __init__(
        self,
        *,
        nids: collections.abc.Iterable[builtins.int] | None = ...,
        mark_notes_modified: builtins.bool = ...,
        generate_cards: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["generate_cards", b"generate_cards", "mark_notes_modified", b"mark_notes_modified", "nids", b"nids"]) -> None: ...

global___AfterNoteUpdatesRequest = AfterNoteUpdatesRequest

@typing_extensions.final
class FieldNamesForNotesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NIDS_FIELD_NUMBER: builtins.int
    @property
    def nids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        nids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nids", b"nids"]) -> None: ...

global___FieldNamesForNotesRequest = FieldNamesForNotesRequest

@typing_extensions.final
class FieldNamesForNotesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields"]) -> None: ...

global___FieldNamesForNotesResponse = FieldNamesForNotesResponse

@typing_extensions.final
class NoteFieldsCheckResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NoteFieldsCheckResponse._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NORMAL: NoteFieldsCheckResponse._State.ValueType  # 0
        EMPTY: NoteFieldsCheckResponse._State.ValueType  # 1
        DUPLICATE: NoteFieldsCheckResponse._State.ValueType  # 2
        MISSING_CLOZE: NoteFieldsCheckResponse._State.ValueType  # 3
        NOTETYPE_NOT_CLOZE: NoteFieldsCheckResponse._State.ValueType  # 4
        FIELD_NOT_CLOZE: NoteFieldsCheckResponse._State.ValueType  # 5

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    NORMAL: NoteFieldsCheckResponse.State.ValueType  # 0
    EMPTY: NoteFieldsCheckResponse.State.ValueType  # 1
    DUPLICATE: NoteFieldsCheckResponse.State.ValueType  # 2
    MISSING_CLOZE: NoteFieldsCheckResponse.State.ValueType  # 3
    NOTETYPE_NOT_CLOZE: NoteFieldsCheckResponse.State.ValueType  # 4
    FIELD_NOT_CLOZE: NoteFieldsCheckResponse.State.ValueType  # 5

    STATE_FIELD_NUMBER: builtins.int
    state: global___NoteFieldsCheckResponse.State.ValueType
    def __init__(
        self,
        *,
        state: global___NoteFieldsCheckResponse.State.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["state", b"state"]) -> None: ...

global___NoteFieldsCheckResponse = NoteFieldsCheckResponse