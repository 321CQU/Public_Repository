# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/notification_center/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7micro_services_protobuf/notification_center/event.proto\x12\x13notification_center\"\x89\x02\n\x1bUpdateEventSubscribeRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x0c\x12\x36\n\x05\x65vent\x18\x02 \x01(\x0e\x32\'.notification_center.NOTIFICATION_EVENT\x12\x14\n\x0cis_subscribe\x18\x03 \x01(\x08\x12N\n\nextra_data\x18\x04 \x01(\x0b\x32:.notification_center.UpdateEventSubscribeRequest.ExtraData\x1a?\n\tExtraData\x12\x0c\n\x04\x61uth\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x12\n\nextra_data\x18\x03 \x01(\t\"U\n\x1a\x46\x65tchSubscribeInfoResponse\x12\x37\n\x06\x65vents\x18\x01 \x03(\x0e\x32\'.notification_center.NOTIFICATION_EVENT*2\n\x12NOTIFICATION_EVENT\x12\x1c\n\x18NOTIFICATION_EVENT_SCORE\x10\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.notification_center.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NOTIFICATION_EVENT']._serialized_start=435
  _globals['_NOTIFICATION_EVENT']._serialized_end=485
  _globals['_UPDATEEVENTSUBSCRIBEREQUEST']._serialized_start=81
  _globals['_UPDATEEVENTSUBSCRIBEREQUEST']._serialized_end=346
  _globals['_UPDATEEVENTSUBSCRIBEREQUEST_EXTRADATA']._serialized_start=283
  _globals['_UPDATEEVENTSUBSCRIBEREQUEST_EXTRADATA']._serialized_end=346
  _globals['_FETCHSUBSCRIBEINFORESPONSE']._serialized_start=348
  _globals['_FETCHSUBSCRIBEINFORESPONSE']._serialized_end=433
# @@protoc_insertion_point(module_scope)
