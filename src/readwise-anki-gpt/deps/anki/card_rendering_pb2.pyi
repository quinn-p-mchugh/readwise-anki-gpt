"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""
import anki.notes_pb2
import anki.notetypes_pb2
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
class ExtractAvTagsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    QUESTION_SIDE_FIELD_NUMBER: builtins.int
    text: builtins.str
    question_side: builtins.bool
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        question_side: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["question_side", b"question_side", "text", b"text"]) -> None: ...

global___ExtractAvTagsRequest = ExtractAvTagsRequest

@typing_extensions.final
class ExtractAvTagsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    AV_TAGS_FIELD_NUMBER: builtins.int
    text: builtins.str
    @property
    def av_tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AVTag]: ...
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        av_tags: collections.abc.Iterable[global___AVTag] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["av_tags", b"av_tags", "text", b"text"]) -> None: ...

global___ExtractAvTagsResponse = ExtractAvTagsResponse

@typing_extensions.final
class AVTag(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOUND_OR_VIDEO_FIELD_NUMBER: builtins.int
    TTS_FIELD_NUMBER: builtins.int
    sound_or_video: builtins.str
    @property
    def tts(self) -> global___TTSTag: ...
    def __init__(
        self,
        *,
        sound_or_video: builtins.str = ...,
        tts: global___TTSTag | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sound_or_video", b"sound_or_video", "tts", b"tts", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["sound_or_video", b"sound_or_video", "tts", b"tts", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["sound_or_video", "tts"] | None: ...

global___AVTag = AVTag

@typing_extensions.final
class TTSTag(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELD_TEXT_FIELD_NUMBER: builtins.int
    LANG_FIELD_NUMBER: builtins.int
    VOICES_FIELD_NUMBER: builtins.int
    SPEED_FIELD_NUMBER: builtins.int
    OTHER_ARGS_FIELD_NUMBER: builtins.int
    field_text: builtins.str
    lang: builtins.str
    @property
    def voices(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    speed: builtins.float
    @property
    def other_args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        field_text: builtins.str = ...,
        lang: builtins.str = ...,
        voices: collections.abc.Iterable[builtins.str] | None = ...,
        speed: builtins.float = ...,
        other_args: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["field_text", b"field_text", "lang", b"lang", "other_args", b"other_args", "speed", b"speed", "voices", b"voices"]) -> None: ...

global___TTSTag = TTSTag

@typing_extensions.final
class ExtractLatexRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    SVG_FIELD_NUMBER: builtins.int
    EXPAND_CLOZES_FIELD_NUMBER: builtins.int
    text: builtins.str
    svg: builtins.bool
    expand_clozes: builtins.bool
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        svg: builtins.bool = ...,
        expand_clozes: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expand_clozes", b"expand_clozes", "svg", b"svg", "text", b"text"]) -> None: ...

global___ExtractLatexRequest = ExtractLatexRequest

@typing_extensions.final
class ExtractLatexResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    LATEX_FIELD_NUMBER: builtins.int
    text: builtins.str
    @property
    def latex(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExtractedLatex]: ...
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        latex: collections.abc.Iterable[global___ExtractedLatex] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["latex", b"latex", "text", b"text"]) -> None: ...

global___ExtractLatexResponse = ExtractLatexResponse

@typing_extensions.final
class ExtractedLatex(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILENAME_FIELD_NUMBER: builtins.int
    LATEX_BODY_FIELD_NUMBER: builtins.int
    filename: builtins.str
    latex_body: builtins.str
    def __init__(
        self,
        *,
        filename: builtins.str = ...,
        latex_body: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filename", b"filename", "latex_body", b"latex_body"]) -> None: ...

global___ExtractedLatex = ExtractedLatex

@typing_extensions.final
class EmptyCardsReport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class NoteWithEmptyCards(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NOTE_ID_FIELD_NUMBER: builtins.int
        CARD_IDS_FIELD_NUMBER: builtins.int
        WILL_DELETE_NOTE_FIELD_NUMBER: builtins.int
        note_id: builtins.int
        @property
        def card_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        will_delete_note: builtins.bool
        def __init__(
            self,
            *,
            note_id: builtins.int = ...,
            card_ids: collections.abc.Iterable[builtins.int] | None = ...,
            will_delete_note: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["card_ids", b"card_ids", "note_id", b"note_id", "will_delete_note", b"will_delete_note"]) -> None: ...

    REPORT_FIELD_NUMBER: builtins.int
    NOTES_FIELD_NUMBER: builtins.int
    report: builtins.str
    @property
    def notes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EmptyCardsReport.NoteWithEmptyCards]: ...
    def __init__(
        self,
        *,
        report: builtins.str = ...,
        notes: collections.abc.Iterable[global___EmptyCardsReport.NoteWithEmptyCards] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["notes", b"notes", "report", b"report"]) -> None: ...

global___EmptyCardsReport = EmptyCardsReport

@typing_extensions.final
class RenderExistingCardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CARD_ID_FIELD_NUMBER: builtins.int
    BROWSER_FIELD_NUMBER: builtins.int
    PARTIAL_RENDER_FIELD_NUMBER: builtins.int
    card_id: builtins.int
    browser: builtins.bool
    partial_render: builtins.bool
    """If true, rendering will stop when an unknown filter is encountered,
    and caller will need to complete rendering. This is done to allow
    Python code to modify the rendering.
    """
    def __init__(
        self,
        *,
        card_id: builtins.int = ...,
        browser: builtins.bool = ...,
        partial_render: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["browser", b"browser", "card_id", b"card_id", "partial_render", b"partial_render"]) -> None: ...

global___RenderExistingCardRequest = RenderExistingCardRequest

@typing_extensions.final
class RenderUncommittedCardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_FIELD_NUMBER: builtins.int
    CARD_ORD_FIELD_NUMBER: builtins.int
    TEMPLATE_FIELD_NUMBER: builtins.int
    FILL_EMPTY_FIELD_NUMBER: builtins.int
    PARTIAL_RENDER_FIELD_NUMBER: builtins.int
    @property
    def note(self) -> anki.notes_pb2.Note: ...
    card_ord: builtins.int
    @property
    def template(self) -> anki.notetypes_pb2.Notetype.Template: ...
    fill_empty: builtins.bool
    partial_render: builtins.bool
    """If true, rendering will stop when an unknown filter is encountered,
    and caller will need to complete rendering. This is done to allow
    Python code to modify the rendering.
    """
    def __init__(
        self,
        *,
        note: anki.notes_pb2.Note | None = ...,
        card_ord: builtins.int = ...,
        template: anki.notetypes_pb2.Notetype.Template | None = ...,
        fill_empty: builtins.bool = ...,
        partial_render: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["note", b"note", "template", b"template"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["card_ord", b"card_ord", "fill_empty", b"fill_empty", "note", b"note", "partial_render", b"partial_render", "template", b"template"]) -> None: ...

global___RenderUncommittedCardRequest = RenderUncommittedCardRequest

@typing_extensions.final
class RenderUncommittedCardLegacyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTE_FIELD_NUMBER: builtins.int
    CARD_ORD_FIELD_NUMBER: builtins.int
    TEMPLATE_FIELD_NUMBER: builtins.int
    FILL_EMPTY_FIELD_NUMBER: builtins.int
    PARTIAL_RENDER_FIELD_NUMBER: builtins.int
    @property
    def note(self) -> anki.notes_pb2.Note: ...
    card_ord: builtins.int
    template: builtins.bytes
    fill_empty: builtins.bool
    partial_render: builtins.bool
    """If true, rendering will stop when an unknown filter is encountered,
    and caller will need to complete rendering. This is done to allow
    Python code to modify the rendering.
    """
    def __init__(
        self,
        *,
        note: anki.notes_pb2.Note | None = ...,
        card_ord: builtins.int = ...,
        template: builtins.bytes = ...,
        fill_empty: builtins.bool = ...,
        partial_render: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["note", b"note"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["card_ord", b"card_ord", "fill_empty", b"fill_empty", "note", b"note", "partial_render", b"partial_render", "template", b"template"]) -> None: ...

global___RenderUncommittedCardLegacyRequest = RenderUncommittedCardLegacyRequest

@typing_extensions.final
class RenderCardResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUESTION_NODES_FIELD_NUMBER: builtins.int
    ANSWER_NODES_FIELD_NUMBER: builtins.int
    CSS_FIELD_NUMBER: builtins.int
    LATEX_SVG_FIELD_NUMBER: builtins.int
    @property
    def question_nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RenderedTemplateNode]: ...
    @property
    def answer_nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RenderedTemplateNode]: ...
    css: builtins.str
    latex_svg: builtins.bool
    def __init__(
        self,
        *,
        question_nodes: collections.abc.Iterable[global___RenderedTemplateNode] | None = ...,
        answer_nodes: collections.abc.Iterable[global___RenderedTemplateNode] | None = ...,
        css: builtins.str = ...,
        latex_svg: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["answer_nodes", b"answer_nodes", "css", b"css", "latex_svg", b"latex_svg", "question_nodes", b"question_nodes"]) -> None: ...

global___RenderCardResponse = RenderCardResponse

@typing_extensions.final
class RenderedTemplateNode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    REPLACEMENT_FIELD_NUMBER: builtins.int
    text: builtins.str
    @property
    def replacement(self) -> global___RenderedTemplateReplacement: ...
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        replacement: global___RenderedTemplateReplacement | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["replacement", b"replacement", "text", b"text", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["replacement", b"replacement", "text", b"text", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value", b"value"]) -> typing_extensions.Literal["text", "replacement"] | None: ...

global___RenderedTemplateNode = RenderedTemplateNode

@typing_extensions.final
class RenderedTemplateReplacement(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELD_NAME_FIELD_NUMBER: builtins.int
    CURRENT_TEXT_FIELD_NUMBER: builtins.int
    FILTERS_FIELD_NUMBER: builtins.int
    field_name: builtins.str
    current_text: builtins.str
    @property
    def filters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        field_name: builtins.str = ...,
        current_text: builtins.str = ...,
        filters: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["current_text", b"current_text", "field_name", b"field_name", "filters", b"filters"]) -> None: ...

global___RenderedTemplateReplacement = RenderedTemplateReplacement

@typing_extensions.final
class RenderMarkdownRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MARKDOWN_FIELD_NUMBER: builtins.int
    SANITIZE_FIELD_NUMBER: builtins.int
    markdown: builtins.str
    sanitize: builtins.bool
    def __init__(
        self,
        *,
        markdown: builtins.str = ...,
        sanitize: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["markdown", b"markdown", "sanitize", b"sanitize"]) -> None: ...

global___RenderMarkdownRequest = RenderMarkdownRequest

@typing_extensions.final
class StripHtmlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Mode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[StripHtmlRequest._Mode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NORMAL: StripHtmlRequest._Mode.ValueType  # 0
        PRESERVE_MEDIA_FILENAMES: StripHtmlRequest._Mode.ValueType  # 1

    class Mode(_Mode, metaclass=_ModeEnumTypeWrapper): ...
    NORMAL: StripHtmlRequest.Mode.ValueType  # 0
    PRESERVE_MEDIA_FILENAMES: StripHtmlRequest.Mode.ValueType  # 1

    TEXT_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    text: builtins.str
    mode: global___StripHtmlRequest.Mode.ValueType
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        mode: global___StripHtmlRequest.Mode.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode", "text", b"text"]) -> None: ...

global___StripHtmlRequest = StripHtmlRequest

@typing_extensions.final
class HtmlToTextLineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    PRESERVE_MEDIA_FILENAMES_FIELD_NUMBER: builtins.int
    text: builtins.str
    preserve_media_filenames: builtins.bool
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        preserve_media_filenames: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["preserve_media_filenames", b"preserve_media_filenames", "text", b"text"]) -> None: ...

global___HtmlToTextLineRequest = HtmlToTextLineRequest

@typing_extensions.final
class CompareAnswerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPECTED_FIELD_NUMBER: builtins.int
    PROVIDED_FIELD_NUMBER: builtins.int
    expected: builtins.str
    provided: builtins.str
    def __init__(
        self,
        *,
        expected: builtins.str = ...,
        provided: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expected", b"expected", "provided", b"provided"]) -> None: ...

global___CompareAnswerRequest = CompareAnswerRequest

@typing_extensions.final
class ExtractClozeForTypingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    ORDINAL_FIELD_NUMBER: builtins.int
    text: builtins.str
    ordinal: builtins.int
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        ordinal: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ordinal", b"ordinal", "text", b"text"]) -> None: ...

global___ExtractClozeForTypingRequest = ExtractClozeForTypingRequest

@typing_extensions.final
class AllTtsVoicesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATE_FIELD_NUMBER: builtins.int
    validate: builtins.bool
    def __init__(
        self,
        *,
        validate: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["validate", b"validate"]) -> None: ...

global___AllTtsVoicesRequest = AllTtsVoicesRequest

@typing_extensions.final
class AllTtsVoicesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class TtsVoice(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        LANGUAGE_FIELD_NUMBER: builtins.int
        AVAILABLE_FIELD_NUMBER: builtins.int
        id: builtins.str
        name: builtins.str
        language: builtins.str
        available: builtins.bool
        def __init__(
            self,
            *,
            id: builtins.str = ...,
            name: builtins.str = ...,
            language: builtins.str = ...,
            available: builtins.bool | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["_available", b"_available", "available", b"available"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["_available", b"_available", "available", b"available", "id", b"id", "language", b"language", "name", b"name"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_available", b"_available"]) -> typing_extensions.Literal["available"] | None: ...

    VOICES_FIELD_NUMBER: builtins.int
    @property
    def voices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AllTtsVoicesResponse.TtsVoice]: ...
    def __init__(
        self,
        *,
        voices: collections.abc.Iterable[global___AllTtsVoicesResponse.TtsVoice] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["voices", b"voices"]) -> None: ...

global___AllTtsVoicesResponse = AllTtsVoicesResponse

@typing_extensions.final
class WriteTtsStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    VOICE_ID_FIELD_NUMBER: builtins.int
    SPEED_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    path: builtins.str
    voice_id: builtins.str
    speed: builtins.float
    text: builtins.str
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        voice_id: builtins.str = ...,
        speed: builtins.float = ...,
        text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "speed", b"speed", "text", b"text", "voice_id", b"voice_id"]) -> None: ...

global___WriteTtsStreamRequest = WriteTtsStreamRequest
