# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bidirectional.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x62idirectional.proto\x12\x0fshoppingService\"\x14\n\x04Item\x12\x0c\n\x04name\x18\x01 \x01(\t\"<\n\x0e\x43lientItemList\x12*\n\x0b\x63lientItems\x18\x01 \x03(\x0b\x32\x15.shoppingService.Item\"O\n\x0eServerItemList\x12*\n\x0bserverItems\x18\x01 \x03(\x0b\x32\x15.shoppingService.Item\x12\x11\n\ttimestamp\x18\x02 \x01(\t2e\n\x0fServerStreaming\x12R\n\x08GetOrder\x12\x1f.shoppingService.ClientItemList\x1a\x1f.shoppingService.ServerItemList\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bidirectional_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ITEM']._serialized_start=40
  _globals['_ITEM']._serialized_end=60
  _globals['_CLIENTITEMLIST']._serialized_start=62
  _globals['_CLIENTITEMLIST']._serialized_end=122
  _globals['_SERVERITEMLIST']._serialized_start=124
  _globals['_SERVERITEMLIST']._serialized_end=203
  _globals['_SERVERSTREAMING']._serialized_start=205
  _globals['_SERVERSTREAMING']._serialized_end=306
# @@protoc_insertion_point(module_scope)
