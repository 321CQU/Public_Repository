from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomepageResponse(_message.Message):
    __slots__ = ["homepages"]
    class HomepageInfo(_message.Message):
        __slots__ = ["img_url", "img_pos", "jump_type", "jump_param"]
        class ImgPos(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            LOCAL: _ClassVar[HomepageResponse.HomepageInfo.ImgPos]
            COS: _ClassVar[HomepageResponse.HomepageInfo.ImgPos]
        LOCAL: HomepageResponse.HomepageInfo.ImgPos
        COS: HomepageResponse.HomepageInfo.ImgPos
        class JumpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            NONE: _ClassVar[HomepageResponse.HomepageInfo.JumpType]
            MD: _ClassVar[HomepageResponse.HomepageInfo.JumpType]
            URL: _ClassVar[HomepageResponse.HomepageInfo.JumpType]
            WECHAT_MINI_PROGRAM: _ClassVar[HomepageResponse.HomepageInfo.JumpType]
        NONE: HomepageResponse.HomepageInfo.JumpType
        MD: HomepageResponse.HomepageInfo.JumpType
        URL: HomepageResponse.HomepageInfo.JumpType
        WECHAT_MINI_PROGRAM: HomepageResponse.HomepageInfo.JumpType
        IMG_URL_FIELD_NUMBER: _ClassVar[int]
        IMG_POS_FIELD_NUMBER: _ClassVar[int]
        JUMP_TYPE_FIELD_NUMBER: _ClassVar[int]
        JUMP_PARAM_FIELD_NUMBER: _ClassVar[int]
        img_url: str
        img_pos: HomepageResponse.HomepageInfo.ImgPos
        jump_type: HomepageResponse.HomepageInfo.JumpType
        jump_param: str
        def __init__(self, img_url: _Optional[str] = ..., img_pos: _Optional[_Union[HomepageResponse.HomepageInfo.ImgPos, str]] = ..., jump_type: _Optional[_Union[HomepageResponse.HomepageInfo.JumpType, str]] = ..., jump_param: _Optional[str] = ...) -> None: ...
    HOMEPAGES_FIELD_NUMBER: _ClassVar[int]
    homepages: _containers.RepeatedCompositeFieldContainer[HomepageResponse.HomepageInfo]
    def __init__(self, homepages: _Optional[_Iterable[_Union[HomepageResponse.HomepageInfo, _Mapping]]] = ...) -> None: ...
