# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki/links.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki import generic_pb2 as anki_dot_generic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61nki/links.proto\x12\nanki.links\x1a\x12\x61nki/generic.proto\"\xdc\x04\n\x13HelpPageLinkRequest\x12\x36\n\x04page\x18\x01 \x01(\x0e\x32(.anki.links.HelpPageLinkRequest.HelpPage\"\x8c\x04\n\x08HelpPage\x12\r\n\tNOTE_TYPE\x10\x00\x12\x0c\n\x08\x42ROWSING\x10\x01\x12\x1d\n\x19\x42ROWSING_FIND_AND_REPLACE\x10\x02\x12\x17\n\x13\x42ROWSING_NOTES_MENU\x10\x03\x12\x16\n\x12KEYBOARD_SHORTCUTS\x10\x04\x12\x0b\n\x07\x45\x44ITING\x10\x05\x12\x18\n\x14\x41\x44\x44ING_CARD_AND_NOTE\x10\x06\x12\x16\n\x12\x41\x44\x44ING_A_NOTE_TYPE\x10\x07\x12\t\n\x05LATEX\x10\x08\x12\x0f\n\x0bPREFERENCES\x10\t\x12\t\n\x05INDEX\x10\n\x12\r\n\tTEMPLATES\x10\x0b\x12\x11\n\rFILTERED_DECK\x10\x0c\x12\r\n\tIMPORTING\x10\r\x12\x16\n\x12\x43USTOMIZING_FIELDS\x10\x0e\x12\x10\n\x0c\x44\x45\x43K_OPTIONS\x10\x0f\x12\x14\n\x10\x45\x44ITING_FEATURES\x10\x10\x12\x15\n\x11\x46ULL_SCREEN_ISSUE\x10\x11\x12\x17\n\x13\x43\x41RD_TYPE_DUPLICATE\x10\x12\x12\x1c\n\x18\x43\x41RD_TYPE_NO_FRONT_FIELD\x10\x13\x12\x1b\n\x17\x43\x41RD_TYPE_MISSING_CLOZE\x10\x14\x12\x1e\n\x1a\x43\x41RD_TYPE_EXTRANEOUS_CLOZE\x10\x15\x12\x1c\n\x18\x43\x41RD_TYPE_TEMPLATE_ERROR\x10\x16\x12\x13\n\x0fTROUBLESHOOTING\x10\x17\x32U\n\x0cLinksService\x12\x45\n\x0cHelpPageLink\x12\x1f.anki.links.HelpPageLinkRequest\x1a\x14.anki.generic.String2\x15\n\x13\x42\x61\x63kendLinksServiceB\x02P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anki.links_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _HELPPAGELINKREQUEST._serialized_start=53
  _HELPPAGELINKREQUEST._serialized_end=657
  _HELPPAGELINKREQUEST_HELPPAGE._serialized_start=133
  _HELPPAGELINKREQUEST_HELPPAGE._serialized_end=657
  _LINKSSERVICE._serialized_start=659
  _LINKSSERVICE._serialized_end=744
  _BACKENDLINKSSERVICE._serialized_start=746
  _BACKENDLINKSSERVICE._serialized_end=767
# @@protoc_insertion_point(module_scope)