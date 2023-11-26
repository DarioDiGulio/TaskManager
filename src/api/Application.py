from flask import Flask

from src.api.controllers.GetAllController import get_all_bp
from src.core.infrastructure.Core import Core


class Application:
    def __init__(self, core: Core) -> None:
        self.__http_server = Flask(__name__)
        self.__http_server.name = 'Task manager'
        self._core = core
        self.register_controllers()

    def register_controllers(self) -> None:
        self.__http_server.register_blueprint(get_all_bp)

    def run(self) -> None:
        self.__http_server.run()
