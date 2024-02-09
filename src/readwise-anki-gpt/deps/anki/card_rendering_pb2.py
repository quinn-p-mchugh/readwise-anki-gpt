# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki/card_rendering.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki import generic_pb2 as anki_dot_generic__pb2
from anki import notes_pb2 as anki_dot_notes__pb2
from anki import notetypes_pb2 as anki_dot_notetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61nki/card_rendering.proto\x12\x13\x61nki.card_rendering\x1a\x12\x61nki/generic.proto\x1a\x10\x61nki/notes.proto\x1a\x14\x61nki/notetypes.proto\";\n\x14\x45xtractAvTagsRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rquestion_side\x18\x02 \x01(\x08\"R\n\x15\x45xtractAvTagsResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\x12+\n\x07\x61v_tags\x18\x02 \x03(\x0b\x32\x1a.anki.card_rendering.AVTag\"V\n\x05\x41VTag\x12\x18\n\x0esound_or_video\x18\x01 \x01(\tH\x00\x12*\n\x03tts\x18\x02 \x01(\x0b\x32\x1b.anki.card_rendering.TTSTagH\x00\x42\x07\n\x05value\"]\n\x06TTSTag\x12\x12\n\nfield_text\x18\x01 \x01(\t\x12\x0c\n\x04lang\x18\x02 \x01(\t\x12\x0e\n\x06voices\x18\x03 \x03(\t\x12\r\n\x05speed\x18\x04 \x01(\x02\x12\x12\n\nother_args\x18\x05 \x03(\t\"G\n\x13\x45xtractLatexRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03svg\x18\x02 \x01(\x08\x12\x15\n\rexpand_clozes\x18\x03 \x01(\x08\"X\n\x14\x45xtractLatexResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x32\n\x05latex\x18\x02 \x03(\x0b\x32#.anki.card_rendering.ExtractedLatex\"6\n\x0e\x45xtractedLatex\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x12\n\nlatex_body\x18\x02 \x01(\t\"\xbe\x01\n\x10\x45mptyCardsReport\x12\x0e\n\x06report\x18\x01 \x01(\t\x12G\n\x05notes\x18\x02 \x03(\x0b\x32\x38.anki.card_rendering.EmptyCardsReport.NoteWithEmptyCards\x1aQ\n\x12NoteWithEmptyCards\x12\x0f\n\x07note_id\x18\x01 \x01(\x03\x12\x10\n\x08\x63\x61rd_ids\x18\x02 \x03(\x03\x12\x18\n\x10will_delete_note\x18\x03 \x01(\x08\"U\n\x19RenderExistingCardRequest\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\x03\x12\x0f\n\x07\x62rowser\x18\x02 \x01(\x08\x12\x16\n\x0epartial_render\x18\x03 \x01(\x08\"\xb1\x01\n\x1cRenderUncommittedCardRequest\x12\x1e\n\x04note\x18\x01 \x01(\x0b\x32\x10.anki.notes.Note\x12\x10\n\x08\x63\x61rd_ord\x18\x02 \x01(\r\x12\x33\n\x08template\x18\x03 \x01(\x0b\x32!.anki.notetypes.Notetype.Template\x12\x12\n\nfill_empty\x18\x04 \x01(\x08\x12\x16\n\x0epartial_render\x18\x05 \x01(\x08\"\x94\x01\n\"RenderUncommittedCardLegacyRequest\x12\x1e\n\x04note\x18\x01 \x01(\x0b\x32\x10.anki.notes.Note\x12\x10\n\x08\x63\x61rd_ord\x18\x02 \x01(\r\x12\x10\n\x08template\x18\x03 \x01(\x0c\x12\x12\n\nfill_empty\x18\x04 \x01(\x08\x12\x16\n\x0epartial_render\x18\x05 \x01(\x08\"\xb8\x01\n\x12RenderCardResponse\x12\x41\n\x0equestion_nodes\x18\x01 \x03(\x0b\x32).anki.card_rendering.RenderedTemplateNode\x12?\n\x0c\x61nswer_nodes\x18\x02 \x03(\x0b\x32).anki.card_rendering.RenderedTemplateNode\x12\x0b\n\x03\x63ss\x18\x03 \x01(\t\x12\x11\n\tlatex_svg\x18\x04 \x01(\x08\"x\n\x14RenderedTemplateNode\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12G\n\x0breplacement\x18\x02 \x01(\x0b\x32\x30.anki.card_rendering.RenderedTemplateReplacementH\x00\x42\x07\n\x05value\"X\n\x1bRenderedTemplateReplacement\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63urrent_text\x18\x02 \x01(\t\x12\x0f\n\x07\x66ilters\x18\x03 \x03(\t\";\n\x15RenderMarkdownRequest\x12\x10\n\x08markdown\x18\x01 \x01(\t\x12\x10\n\x08sanitize\x18\x02 \x01(\x08\"\x8c\x01\n\x10StripHtmlRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x38\n\x04mode\x18\x02 \x01(\x0e\x32*.anki.card_rendering.StripHtmlRequest.Mode\"0\n\x04Mode\x12\n\n\x06NORMAL\x10\x00\x12\x1c\n\x18PRESERVE_MEDIA_FILENAMES\x10\x01\"G\n\x15HtmlToTextLineRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12 \n\x18preserve_media_filenames\x18\x02 \x01(\x08\":\n\x14\x43ompareAnswerRequest\x12\x10\n\x08\x65xpected\x18\x01 \x01(\t\x12\x10\n\x08provided\x18\x02 \x01(\t\"=\n\x1c\x45xtractClozeForTypingRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0f\n\x07ordinal\x18\x02 \x01(\r\"\'\n\x13\x41llTtsVoicesRequest\x12\x10\n\x08validate\x18\x01 \x01(\x08\"\xb8\x01\n\x14\x41llTtsVoicesResponse\x12\x42\n\x06voices\x18\x01 \x03(\x0b\x32\x32.anki.card_rendering.AllTtsVoicesResponse.TtsVoice\x1a\\\n\x08TtsVoice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x16\n\tavailable\x18\x04 \x01(\x08H\x00\x88\x01\x01\x42\x0c\n\n_available\"T\n\x15WriteTtsStreamRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08voice_id\x18\x02 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x02\x12\x0c\n\x04text\x18\x04 \x01(\t2\xf2\t\n\x14\x43\x61rdRenderingService\x12\x66\n\rExtractAvTags\x12).anki.card_rendering.ExtractAvTagsRequest\x1a*.anki.card_rendering.ExtractAvTagsResponse\x12\x63\n\x0c\x45xtractLatex\x12(.anki.card_rendering.ExtractLatexRequest\x1a).anki.card_rendering.ExtractLatexResponse\x12K\n\rGetEmptyCards\x12\x13.anki.generic.Empty\x1a%.anki.card_rendering.EmptyCardsReport\x12m\n\x12RenderExistingCard\x12..anki.card_rendering.RenderExistingCardRequest\x1a\'.anki.card_rendering.RenderCardResponse\x12s\n\x15RenderUncommittedCard\x12\x31.anki.card_rendering.RenderUncommittedCardRequest\x1a\'.anki.card_rendering.RenderCardResponse\x12\x7f\n\x1bRenderUncommittedCardLegacy\x12\x37.anki.card_rendering.RenderUncommittedCardLegacyRequest\x1a\'.anki.card_rendering.RenderCardResponse\x12\x39\n\x0bStripAvTags\x12\x14.anki.generic.String\x1a\x14.anki.generic.String\x12R\n\x0eRenderMarkdown\x12*.anki.card_rendering.RenderMarkdownRequest\x1a\x14.anki.generic.String\x12<\n\x0e\x45ncodeIriPaths\x12\x14.anki.generic.String\x1a\x14.anki.generic.String\x12<\n\x0e\x44\x65\x63odeIriPaths\x12\x14.anki.generic.String\x1a\x14.anki.generic.String\x12H\n\tStripHtml\x12%.anki.card_rendering.StripHtmlRequest\x1a\x14.anki.generic.String\x12R\n\x0eHtmlToTextLine\x12*.anki.card_rendering.HtmlToTextLineRequest\x1a\x14.anki.generic.String\x12P\n\rCompareAnswer\x12).anki.card_rendering.CompareAnswerRequest\x1a\x14.anki.generic.String\x12`\n\x15\x45xtractClozeForTyping\x12\x31.anki.card_rendering.ExtractClozeForTypingRequest\x1a\x14.anki.generic.String2\x9f\x02\n\x1b\x42\x61\x63kendCardRenderingService\x12H\n\tStripHtml\x12%.anki.card_rendering.StripHtmlRequest\x1a\x14.anki.generic.String\x12\x63\n\x0c\x41llTtsVoices\x12(.anki.card_rendering.AllTtsVoicesRequest\x1a).anki.card_rendering.AllTtsVoicesResponse\x12Q\n\x0eWriteTtsStream\x12*.anki.card_rendering.WriteTtsStreamRequest\x1a\x13.anki.generic.EmptyB\x02P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anki.card_rendering_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _EXTRACTAVTAGSREQUEST._serialized_start=110
  _EXTRACTAVTAGSREQUEST._serialized_end=169
  _EXTRACTAVTAGSRESPONSE._serialized_start=171
  _EXTRACTAVTAGSRESPONSE._serialized_end=253
  _AVTAG._serialized_start=255
  _AVTAG._serialized_end=341
  _TTSTAG._serialized_start=343
  _TTSTAG._serialized_end=436
  _EXTRACTLATEXREQUEST._serialized_start=438
  _EXTRACTLATEXREQUEST._serialized_end=509
  _EXTRACTLATEXRESPONSE._serialized_start=511
  _EXTRACTLATEXRESPONSE._serialized_end=599
  _EXTRACTEDLATEX._serialized_start=601
  _EXTRACTEDLATEX._serialized_end=655
  _EMPTYCARDSREPORT._serialized_start=658
  _EMPTYCARDSREPORT._serialized_end=848
  _EMPTYCARDSREPORT_NOTEWITHEMPTYCARDS._serialized_start=767
  _EMPTYCARDSREPORT_NOTEWITHEMPTYCARDS._serialized_end=848
  _RENDEREXISTINGCARDREQUEST._serialized_start=850
  _RENDEREXISTINGCARDREQUEST._serialized_end=935
  _RENDERUNCOMMITTEDCARDREQUEST._serialized_start=938
  _RENDERUNCOMMITTEDCARDREQUEST._serialized_end=1115
  _RENDERUNCOMMITTEDCARDLEGACYREQUEST._serialized_start=1118
  _RENDERUNCOMMITTEDCARDLEGACYREQUEST._serialized_end=1266
  _RENDERCARDRESPONSE._serialized_start=1269
  _RENDERCARDRESPONSE._serialized_end=1453
  _RENDEREDTEMPLATENODE._serialized_start=1455
  _RENDEREDTEMPLATENODE._serialized_end=1575
  _RENDEREDTEMPLATEREPLACEMENT._serialized_start=1577
  _RENDEREDTEMPLATEREPLACEMENT._serialized_end=1665
  _RENDERMARKDOWNREQUEST._serialized_start=1667
  _RENDERMARKDOWNREQUEST._serialized_end=1726
  _STRIPHTMLREQUEST._serialized_start=1729
  _STRIPHTMLREQUEST._serialized_end=1869
  _STRIPHTMLREQUEST_MODE._serialized_start=1821
  _STRIPHTMLREQUEST_MODE._serialized_end=1869
  _HTMLTOTEXTLINEREQUEST._serialized_start=1871
  _HTMLTOTEXTLINEREQUEST._serialized_end=1942
  _COMPAREANSWERREQUEST._serialized_start=1944
  _COMPAREANSWERREQUEST._serialized_end=2002
  _EXTRACTCLOZEFORTYPINGREQUEST._serialized_start=2004
  _EXTRACTCLOZEFORTYPINGREQUEST._serialized_end=2065
  _ALLTTSVOICESREQUEST._serialized_start=2067
  _ALLTTSVOICESREQUEST._serialized_end=2106
  _ALLTTSVOICESRESPONSE._serialized_start=2109
  _ALLTTSVOICESRESPONSE._serialized_end=2293
  _ALLTTSVOICESRESPONSE_TTSVOICE._serialized_start=2201
  _ALLTTSVOICESRESPONSE_TTSVOICE._serialized_end=2293
  _WRITETTSSTREAMREQUEST._serialized_start=2295
  _WRITETTSSTREAMREQUEST._serialized_end=2379
  _CARDRENDERINGSERVICE._serialized_start=2382
  _CARDRENDERINGSERVICE._serialized_end=3648
  _BACKENDCARDRENDERINGSERVICE._serialized_start=3651
  _BACKENDCARDRENDERINGSERVICE._serialized_end=3938
# @@protoc_insertion_point(module_scope)
