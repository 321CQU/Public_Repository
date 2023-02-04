from typing import Type, TypeVar, Tuple, Dict

from pydantic import BaseModel
from google.protobuf.json_format import ParseDict


MessageType = TypeVar('MessageType')


def model2protobuf(model: BaseModel, target: Type[MessageType]) -> MessageType:
    return ParseDict(model.dict(), target())


def model_list2protobuf(model: list[BaseModel], key: str, target: Type[MessageType]) -> MessageType:
    return ParseDict({key: [i.dict() for i in model]}, target())
