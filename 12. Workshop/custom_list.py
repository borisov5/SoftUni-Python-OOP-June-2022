from copy import deepcopy

from constants import CUSTOM_INDEX_ERROR_MESSAGE, CUSTOM_DATA_INDEX_ERROR_MESSAGE
from errors import NoElementsInListError, NoSuchValueError


class CustomIntList:
    def __init__(self):
        self.__values = []

    def append(self, val):
        if not isinstance(val, int):
            raise ValueError("Only ints are accepted")
        self.__values.append(val)

    def remove(self, index):
        try:
            el = self.__values.pop(index)
            return el
        except IndexError:
            raise IndexError(CUSTOM_INDEX_ERROR_MESSAGE)
        except TypeError:
            raise ValueError(CUSTOM_DATA_INDEX_ERROR_MESSAGE)

    def get(self, index):
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError(CUSTOM_INDEX_ERROR_MESSAGE)

    def extend(self, vals):
        try:
            for el in vals:
                if not isinstance(el, int):
                    raise ValueError("Only ints are accepted")
            self.__values.extend(vals)
            return deepcopy(self.__values)
        except TypeError:
            raise ValueError('Extend method works only with iterables objects')

    def insert(self, index, v):
        try:
            if index < 0 or index >= len(self.__values):
                raise IndexError
            self.__values.insert(index, v)
            return self.__values
        except IndexError:
            raise IndexError(CUSTOM_INDEX_ERROR_MESSAGE)
        except TypeError:
            raise ValueError(CUSTOM_DATA_INDEX_ERROR_MESSAGE)

    def pop(self):
        if not self.__values:
            raise NoElementsInListError("No elements in the list")
        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index_left(self, value):
        try:
            return self.__values.index(value)
        except ValueError:
            raise NoSuchValueError("No such value in the list")

    def index_right(self, value):
        for index in range(len(self.__values) - 1, -1, -1):
            if self.__values[index] == value:
                return index
        raise NoSuchValueError("No such value in the list")

    def count(self, val):
        return self.__values.count(val)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)
