from typing import Type

from jivago.lang.annotations import Override
from jivago.serialization.deserialization_object_hook import DeserializationObjectHook
from jivago.wsgi.invocation.incorrect_attribute_type_exception import IncorrectAttributeTypeException


class ListDeserializationHook(DeserializationObjectHook):

    @Override
    def can_handle_deserialization(self, declared_type: type) -> bool:
        return declared_type == list

    @Override
    def deserialize(self, obj, declared_type: Type[list]) -> list:
        if isinstance(obj, list):
            return obj
        raise IncorrectAttributeTypeException()
