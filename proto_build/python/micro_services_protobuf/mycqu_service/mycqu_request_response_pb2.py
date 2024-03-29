# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/mycqu_service/mycqu_request_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as micro__services__protobuf_dot_mycqu__service_dot_mycqu__model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBmicro_services_protobuf/mycqu_service/mycqu_request_response.proto\x12\rmycqu_service\x1a\x37micro_services_protobuf/mycqu_service/mycqu_model.proto\"/\n\rBaseLoginInfo\x12\x0c\n\x04\x61uth\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"7\n\x11\x46\x65tchBillResponse\x12\"\n\x05\x62ills\x18\x01 \x03(\x0b\x32\x13.mycqu_service.Bill\"n\n\x15\x46\x65tchEnergyFeeRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x10\n\x08is_hu_xi\x18\x02 \x01(\x08\x12\x0c\n\x04room\x18\x03 \x01(\t\"F\n\x17\x46\x65tchAllSessionResponse\x12+\n\x08sessions\x18\x01 \x03(\x0b\x32\x19.mycqu_service.CquSession\"S\n\x1b\x46\x65tchAllSessionInfoResponse\x12\x34\n\rsession_infos\x18\x01 \x03(\x0b\x32\x1d.mycqu_service.CquSessionInfo\"\x8e\x01\n\x1b\x46\x65tchCourseTimetableRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12*\n\x07session\x18\x03 \x01(\x0b\x32\x19.mycqu_service.CquSession\"Y\n\x1c\x46\x65tchCourseTimetableResponse\x12\x39\n\x11\x63ourse_timetables\x18\x01 \x03(\x0b\x32\x1e.mycqu_service.CourseTimetable\"b\n\x1b\x46\x65tchEnrollTimetableRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"g\n\x1c\x46\x65tchEnrollCourseInfoRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x10\n\x08is_major\x18\x02 \x01(\x08\"\x9c\x02\n\x1d\x46\x65tchEnrollCourseInfoResponse\x12H\n\x06result\x18\x01 \x03(\x0b\x32\x38.mycqu_service.FetchEnrollCourseInfoResponse.ResultEntry\x1a\x42\n\x11\x45nrollCourseInfos\x12-\n\x04info\x18\x01 \x03(\x0b\x32\x1f.mycqu_service.EnrollCourseInfo\x1am\n\x0bResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b\x32>.mycqu_service.FetchEnrollCourseInfoResponse.EnrollCourseInfos:\x02\x38\x01\"s\n\x1c\x46\x65tchEnrollCourseItemRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08is_major\x18\x03 \x01(\x08\"]\n\x1d\x46\x65tchEnrollCourseItemResponse\x12<\n\x13\x65nroll_course_items\x18\x01 \x03(\x0b\x32\x1f.mycqu_service.EnrollCourseItem\"Y\n\x10\x46\x65tchExamRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0e\n\x06stu_id\x18\x02 \x01(\t\"7\n\x11\x46\x65tchExamResponse\x12\"\n\x05\x65xams\x18\x01 \x03(\x0b\x32\x13.mycqu_service.Exam\"\\\n\x11\x46\x65tchScoreRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x10\n\x08is_minor\x18\x02 \x01(\x08\":\n\x12\x46\x65tchScoreResponse\x12$\n\x06scores\x18\x01 \x03(\x0b\x32\x14.mycqu_service.Score\"U\n\x16\x46\x65tchBorrowBookRequest\x12*\n\x04info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0f\n\x07is_curr\x18\x02 \x01(\x08\"F\n\x17\x46\x65tchBorrowBookResponse\x12+\n\nbook_infos\x18\x01 \x03(\x0b\x32\x17.mycqu_service.BookInfo\"O\n\x10RenewBookRequest\x12*\n\x04info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0f\n\x07\x62ook_id\x18\x02 \x01(\t\"$\n\x11RenewBookResponse\x12\x0f\n\x07message\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.mycqu_service.mycqu_request_response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY._options = None
  _FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY._serialized_options = b'8\001'
  _globals['_BASELOGININFO']._serialized_start=142
  _globals['_BASELOGININFO']._serialized_end=189
  _globals['_FETCHBILLRESPONSE']._serialized_start=191
  _globals['_FETCHBILLRESPONSE']._serialized_end=246
  _globals['_FETCHENERGYFEEREQUEST']._serialized_start=248
  _globals['_FETCHENERGYFEEREQUEST']._serialized_end=358
  _globals['_FETCHALLSESSIONRESPONSE']._serialized_start=360
  _globals['_FETCHALLSESSIONRESPONSE']._serialized_end=430
  _globals['_FETCHALLSESSIONINFORESPONSE']._serialized_start=432
  _globals['_FETCHALLSESSIONINFORESPONSE']._serialized_end=515
  _globals['_FETCHCOURSETIMETABLEREQUEST']._serialized_start=518
  _globals['_FETCHCOURSETIMETABLEREQUEST']._serialized_end=660
  _globals['_FETCHCOURSETIMETABLERESPONSE']._serialized_start=662
  _globals['_FETCHCOURSETIMETABLERESPONSE']._serialized_end=751
  _globals['_FETCHENROLLTIMETABLEREQUEST']._serialized_start=753
  _globals['_FETCHENROLLTIMETABLEREQUEST']._serialized_end=851
  _globals['_FETCHENROLLCOURSEINFOREQUEST']._serialized_start=853
  _globals['_FETCHENROLLCOURSEINFOREQUEST']._serialized_end=956
  _globals['_FETCHENROLLCOURSEINFORESPONSE']._serialized_start=959
  _globals['_FETCHENROLLCOURSEINFORESPONSE']._serialized_end=1243
  _globals['_FETCHENROLLCOURSEINFORESPONSE_ENROLLCOURSEINFOS']._serialized_start=1066
  _globals['_FETCHENROLLCOURSEINFORESPONSE_ENROLLCOURSEINFOS']._serialized_end=1132
  _globals['_FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY']._serialized_start=1134
  _globals['_FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY']._serialized_end=1243
  _globals['_FETCHENROLLCOURSEITEMREQUEST']._serialized_start=1245
  _globals['_FETCHENROLLCOURSEITEMREQUEST']._serialized_end=1360
  _globals['_FETCHENROLLCOURSEITEMRESPONSE']._serialized_start=1362
  _globals['_FETCHENROLLCOURSEITEMRESPONSE']._serialized_end=1455
  _globals['_FETCHEXAMREQUEST']._serialized_start=1457
  _globals['_FETCHEXAMREQUEST']._serialized_end=1546
  _globals['_FETCHEXAMRESPONSE']._serialized_start=1548
  _globals['_FETCHEXAMRESPONSE']._serialized_end=1603
  _globals['_FETCHSCOREREQUEST']._serialized_start=1605
  _globals['_FETCHSCOREREQUEST']._serialized_end=1697
  _globals['_FETCHSCORERESPONSE']._serialized_start=1699
  _globals['_FETCHSCORERESPONSE']._serialized_end=1757
  _globals['_FETCHBORROWBOOKREQUEST']._serialized_start=1759
  _globals['_FETCHBORROWBOOKREQUEST']._serialized_end=1844
  _globals['_FETCHBORROWBOOKRESPONSE']._serialized_start=1846
  _globals['_FETCHBORROWBOOKRESPONSE']._serialized_end=1916
  _globals['_RENEWBOOKREQUEST']._serialized_start=1918
  _globals['_RENEWBOOKREQUEST']._serialized_end=1997
  _globals['_RENEWBOOKRESPONSE']._serialized_start=1999
  _globals['_RENEWBOOKRESPONSE']._serialized_end=2035
# @@protoc_insertion_point(module_scope)
