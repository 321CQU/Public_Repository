# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/control_center/control_center_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_services_protobuf.control_center import control_center_models_pb2 as micro__services__protobuf_dot_control__center_dot_control__center__models__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCmicro_services_protobuf/control_center/control_center_service.proto\x12\x0e\x63ontrol_center\x1a\x42micro_services_protobuf/control_center/control_center_models.proto\x1a\x1bgoogle/protobuf/empty.proto2\xbf\x01\n\x14ImportantInfoService\x12Y\n\x1d\x46orceRefreshHomepageInfoCache\x12\x16.google.protobuf.Empty\x1a .control_center.HomepageResponse\x12L\n\x10GetHomepageInfos\x12\x16.google.protobuf.Empty\x1a .control_center.HomepageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.control_center.control_center_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_IMPORTANTINFOSERVICE']._serialized_start=185
  _globals['_IMPORTANTINFOSERVICE']._serialized_end=376
# @@protoc_insertion_point(module_scope)
