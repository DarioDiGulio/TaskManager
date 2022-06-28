class Id:
    def __init__(self, value: int):
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Id) and self.__value == o.value

    def __repr__(self) -> str:
        return f'Id({self.__value})'
