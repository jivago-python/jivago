from example_app.comp.beans import SomeBean
from jivago.lang.annotations import Inject
from jivago.wsgi.methods import GET, POST
from jivago.wsgi.router import Resource, Path


@Resource("/hello")
class HelloWorldResource(object):

    @Inject
    def __init__(self, some_bean: SomeBean):
        self.some_bean = some_bean

    @GET
    def get_hello(self) -> str:
        return self.some_bean.say_hello()

    @POST
    @Path("/{name}")
    def post_hello(self, name: str) -> str:
        print("name: {}".format(name))
        return self.some_bean.say_hello()
