import pkgutil

from jivago.inject.annoted_class_binder import AnnotatedClassBinder
from jivago.inject.provider_binder import ProviderBinder
from jivago.inject.class_registry import ClassRegistry, Annotation, Singleton, Component
from jivago.inject.scope_cache import ScopeCache
from jivago.inject.service_locator import ServiceLocator
from jivago.wsgi.router import Resource


class JivagoApplication(object):
    scopes = [Singleton]

    def __init__(self, root_module):
        self.rootModule = root_module
        self.__import_package_recursive(root_module)
        self.serviceLocator = ServiceLocator()
        self.__initialize_service_locator()

    def __import_package_recursive(self, package):
        prefix = package.__name__ + "."
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            module = __import__(modname, fromlist="dummy")
            if ispkg:
                self.__import_package_recursive(module)

    def __initialize_service_locator(self):
        AnnotatedClassBinder(self.rootModule.__name__, ClassRegistry(), Component).bind(self.serviceLocator)
        AnnotatedClassBinder(self.rootModule.__name__, ClassRegistry(), Resource).bind(self.serviceLocator)
        ProviderBinder(self.rootModule.__name__, ClassRegistry()).bind(self.serviceLocator)
        for scope in self.scopes:
            scoped_classes = self.get_annotated(scope)
            cache = ScopeCache(scope, scoped_classes)
            self.serviceLocator.register_scope(cache)

    def get_annotated(self, annotation: Annotation) -> list:
        return ClassRegistry().get_annotated_in_package(annotation, self.rootModule.__name__)
