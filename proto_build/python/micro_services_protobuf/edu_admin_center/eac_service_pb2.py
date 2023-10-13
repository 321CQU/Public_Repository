# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/edu_admin_center/eac_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as micro__services__protobuf_dot_mycqu__service_dot_mycqu__model__pb2
from micro_services_protobuf.mycqu_service import mycqu_request_response_pb2 as micro__services__protobuf_dot_mycqu__service_dot_mycqu__request__response__pb2
from micro_services_protobuf.edu_admin_center import eac_models_pb2 as micro__services__protobuf_dot_edu__admin__center_dot_eac__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:micro_services_protobuf/edu_admin_center/eac_service.proto\x12\x10\x65\x64u_admin_center\x1a\x37micro_services_protobuf/mycqu_service/mycqu_model.proto\x1a\x42micro_services_protobuf/mycqu_service/mycqu_request_response.proto\x1a\x39micro_services_protobuf/edu_admin_center/eac_models.proto2\xb7\x05\n\x0e\x45\x64uAdminCenter\x12T\n\x0cValidateAuth\x12\x1c.mycqu_service.BaseLoginInfo\x1a&.edu_admin_center.ValidateAuthResponse\x12r\n\x15\x46\x65tchEnrollCourseInfo\x12+.mycqu_service.FetchEnrollCourseInfoRequest\x1a,.mycqu_service.FetchEnrollCourseInfoResponse\x12r\n\x15\x46\x65tchEnrollCourseItem\x12+.mycqu_service.FetchEnrollCourseItemRequest\x1a,.mycqu_service.FetchEnrollCourseItemResponse\x12N\n\tFetchExam\x12\x1f.mycqu_service.FetchExamRequest\x1a .mycqu_service.FetchExamResponse\x12u\n\x14\x46\x65tchCourseTimetable\x12-.edu_admin_center.FetchCourseTimetableRequest\x1a..edu_admin_center.FetchCourseTimetableResponse\x12T\n\nFetchScore\x12#.edu_admin_center.FetchScoreRequest\x1a!.mycqu_service.FetchScoreResponse\x12J\n\x0f\x46\x65tchGpaRanking\x12\x1c.mycqu_service.BaseLoginInfo\x1a\x19.mycqu_service.GpaRankingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.edu_admin_center.eac_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EDUADMINCENTER']._serialized_start=265
  _globals['_EDUADMINCENTER']._serialized_end=960
# @@protoc_insertion_point(module_scope)
