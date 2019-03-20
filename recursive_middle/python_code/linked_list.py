from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, val: T = None):
        self.__val = val
        self.__next = None

    def set_next(self, node: 'Node[T]'):
        self.__next = node

    def get_next(self) -> 'Optional[Node[T]]':
        return self.__next

    def has_next(self) -> bool:
        return self.__next is not None

    def get_val(self) -> T:
        return self.__val


class Linked(Generic[T]):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def append(self, val: T):
        new_node = Node(val)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def head(self) -> Node[T]:
        return self.__head