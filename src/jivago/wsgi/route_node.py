from typing import List

from jivago.inject.registry import Annotation
from jivago.wsgi.ambiguous_routing_exception import AmbiguousRoutingException
from jivago.wsgi.route_invocation_wrapper import RouteInvocationWrapper

PATH_PARAMETER = '{param}'


class RouteNode(object):
    def __init__(self):
        self.children = {}
        self.invocators = {}

    def register_child(self, path: List[str], http_primitive: Annotation, invocation_wrapper: RouteInvocationWrapper):
        if len(path) == 0:
            if http_primitive in self.invocators:
                raise AmbiguousRoutingException(http_primitive, invocation_wrapper)
            self.invocators[http_primitive] = invocation_wrapper
        else:
            next_path_element = PATH_PARAMETER if path[0].startswith("{") and path[0].endswith('}') else path[0]
            if next_path_element not in self.children:
                self.children[next_path_element] = RouteNode()
            self.children[next_path_element].register_child(path[1::], http_primitive, invocation_wrapper)
