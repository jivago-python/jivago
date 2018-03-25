from typing import Callable


class RouteInvocationWrapper(object):
    def __init__(self, resource_class: type, route_function: Callable):
        self.resourceClass = resource_class
        self.routeFunction = route_function
