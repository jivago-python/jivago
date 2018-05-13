from typing import List, Type

from jivago.config.production_jivago_context import ProductionJivagoContext
from jivago.inject.registry import Registry
from jivago.lang.annotations import Override
from jivago.wsgi.filters.exception.application_exception_filter import ApplicationExceptionFilter
from jivago.wsgi.filters.exception.debug_exception_filter import DebugExceptionFilter
from jivago.wsgi.filters.exception.unknown_exception_filter import UnknownExceptionFilter
from jivago.wsgi.filters.filter import Filter
from jivago.wsgi.filters.json_serialization_filter import JsonSerializationFilter
from jivago.wsgi.filters.no_cors_filter import NoCorsFilter


class DebugJivagoContext(ProductionJivagoContext):

    def __init__(self, root_package: str, registry: Registry):
        super().__init__(root_package, registry)

    @Override
    def get_filters(self, path: str) -> List[Type[Filter]]:
        return [NoCorsFilter, UnknownExceptionFilter, DebugExceptionFilter, JsonSerializationFilter,
                ApplicationExceptionFilter]