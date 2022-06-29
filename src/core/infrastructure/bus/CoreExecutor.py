from src.core.infrastructure.bus.Handler import Handler


class CoreExecutor:
    def __init__(self):
        self.__handlers = dict()

    def register_handler(self, handler: Handler):
        self.__handlers[handler.name] = handler

    def execute(self, request):
        try:
            self.__handlers[request.__class__.__name__].execute(request)
        except KeyError:
            raise Exception(f'Handler for {request.__class__.__name__} not registered')
