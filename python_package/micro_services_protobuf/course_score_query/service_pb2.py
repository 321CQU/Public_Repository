# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/course_score_query/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_services_protobuf.course_score_query import model_pb2 as micro__services__protobuf_dot_course__score__query_dot_model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8micro_services_protobuf/course_score_query/service.proto\x12\x12\x63ourse_score_query\x1a\x36micro_services_protobuf/course_score_query/model.proto2\x86\x02\n\x10\x43ourseScoreQuery\x12m\n\x10\x46indCourseByName\x12+.course_score_query.FindCourseByNameRequest\x1a,.course_score_query.FindCourseByNameResponse\x12\x82\x01\n\x17\x46\x65tchLayeredScoreDetail\x12\x32.course_score_query.FetchLayeredScoreDetailRequest\x1a\x33.course_score_query.FetchLayeredScoreDetailResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.course_score_query.service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COURSESCOREQUERY._serialized_start=137
  _COURSESCOREQUERY._serialized_end=399
# @@protoc_insertion_point(module_scope)