from typing import Any

class Property:
    __attributes = {}

    def __init__(self) -> None:
        self.include('address')

    def include(self, attribute_name: str):
        if attribute_name in self.__attributes:
            print('attribute:', attribute_name, 'already included')
        else:
            self.__attributes[attribute_name] = None
            print('attribute:', attribute_name, 'added')

    def items(self):
        return self.__attributes.items()

    def set(self, name: str, value: Any) -> None:
        if name in self.__attributes:
            self.__attributes[name] = value
        else:
            print('attribute', name, 'doesn\'t exist')

