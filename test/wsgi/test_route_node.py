import unittest

from jivago.wsgi.methods import GET
from jivago.wsgi.route_node import RouteNode
from jivago.wsgi.route_registration import RouteRegistration
from jivago.wsgi.unknown_path_exception import UnknownPathException


class RouteNodeTest(unittest.TestCase):
    A_SIMPLE_PATH = ['hello']
    HTTP_PRIMITIVE = GET
    A_WRAPPER = RouteRegistration(None, None, [""])
    A_LONGER_PATH = ['hello', 'goodbye']
    A_PATH_WITH_PARAMETERS = ["hello", "{id}", "delete"]
    A_PATH_WITH_DIFFERENT_PARAMETERS = ["hello", "{name}", "delete"]

    def setUp(self):
        self.rootNode = RouteNode()

    def test_whenRegisteringAPath_thenMethodInvocatorIsSavedLastChildNode(self):
        self.rootNode.register_child(self.A_SIMPLE_PATH, self.HTTP_PRIMITIVE, self.A_WRAPPER)

        self.assertEqual({self.HTTP_PRIMITIVE: [self.A_WRAPPER]}, self.rootNode.children['hello'].invocators)

    def test_givenPathOfMultipleElements_whenRegistering_thenMethodInvocatorIsOnlySavedAtLastChildNode(self):
        self.rootNode.register_child(self.A_LONGER_PATH, self.HTTP_PRIMITIVE, self.A_WRAPPER)

        self.assertEqual({self.HTTP_PRIMITIVE: [self.A_WRAPPER]},
                         self.rootNode.children['hello'].children['goodbye'].invocators)
        self.assertEqual(1, len(self.rootNode.children))
        self.assertEqual(1, len(self.rootNode.children['hello'].children))

    def test_whenExploring_thenWalkTheTreeWordByWord(self):
        self.rootNode.register_child(self.A_LONGER_PATH, self.HTTP_PRIMITIVE, self.A_WRAPPER)

        node = self.rootNode.explore(self.A_LONGER_PATH)

        self.assertEqual(self.A_WRAPPER, node.invocators[self.HTTP_PRIMITIVE][0])

    def test_givenUnknownPath_whenExploring_thenThrowUnknownPathException(self):
        with self.assertRaises(UnknownPathException):
            self.rootNode.explore(self.A_SIMPLE_PATH)

    def test_givenParameters_whenExploring_thenFollowPathRegardlessOfParameter(self):
        self.rootNode.register_child(self.A_PATH_WITH_PARAMETERS, self.HTTP_PRIMITIVE, self.A_WRAPPER)

        node = self.rootNode.explore(self.A_PATH_WITH_PARAMETERS)
        node2 = self.rootNode.explore(self.A_PATH_WITH_DIFFERENT_PARAMETERS)

        self.assertEqual(self.A_WRAPPER, node.invocators[self.HTTP_PRIMITIVE][0])
        self.assertEqual(node, node2)
