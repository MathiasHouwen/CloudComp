# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: events.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65vents.proto\x12\x06\x65vents\" \n\x10GetEventsRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"2\n\x11GetEventsResponse\x12\x1d\n\x06\x65vents\x18\x01 \x03(\x0b\x32\r.events.Event\"9\n\x05\x45vent\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t2W\n\x0c\x45ventService\x12G\n\x10GetEventsFromDay\x12\x18.events.GetEventsRequest\x1a\x19.events.GetEventsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETEVENTSREQUEST']._serialized_start=24
  _globals['_GETEVENTSREQUEST']._serialized_end=56
  _globals['_GETEVENTSRESPONSE']._serialized_start=58
  _globals['_GETEVENTSRESPONSE']._serialized_end=108
  _globals['_EVENT']._serialized_start=110
  _globals['_EVENT']._serialized_end=167
  _globals['_EVENTSERVICE']._serialized_start=169
  _globals['_EVENTSERVICE']._serialized_end=256
# @@protoc_insertion_point(module_scope)
