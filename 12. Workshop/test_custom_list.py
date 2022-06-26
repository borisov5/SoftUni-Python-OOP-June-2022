from copy import deepcopy


class NoElementsInListError(Exception):
    pass


CUSTOM_INDEX_ERROR_MESSAGE = 'Invalid index'
CUSTOM_DATA_INDEX_ERROR_MESSAGE = 'Index is not a valid integer. Please pass an integer number'


class CustomList:
    def __init__(self):
        self.__values = []

    def append(self, val):
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


from unittest import main, TestCase


class TestCustomList(TestCase):
    def setUp(self):
        self.custom_list = CustomList()

    def test_append_adds_element_at_the_end_of_the_list(self):
        self.assertEqual([], self.custom_list._CustomList__values)
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

    def test_remove_element_invalid_index_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.remove(0)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_pass_invalid_integer_index_to_remove_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.remove("0")
        self.assertEqual(CUSTOM_DATA_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_remove_element_removes_and_returns(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)
        returned_element = self.custom_list.remove(0)
        self.assertEqual([], self.custom_list._CustomList__values)
        self.assertEqual(5, returned_element)

    def test_get_returns_element(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        element = self.custom_list.get(0)
        self.assertEqual(5, element)
        self.assertEqual([5], self.custom_list._CustomList__values)

    def test_get_invalid_index_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        # Pass invalid index right border
        with self.assertRaises(IndexError) as ex:
            self.custom_list.get(-2)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

        # Pass invalid index left border
        with self.assertRaises(IndexError) as ex:
            self.custom_list.get(1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_extend_appends_new_values(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        self.custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], self.custom_list._CustomList__values)

    def test_extend_with_non_iterable_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as ex:
            self.custom_list.extend(15)
        self.assertEqual("Extend method works only with iterables objects", str(ex.exception))

    def test_extend_returns_new_list(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)
        result_list = self.custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], self.custom_list._CustomList__values)
        self.assertEqual([5, 2, 3, 4], result_list)
        self.assertNotEqual(id(result_list), id(self.custom_list._CustomList__values))

    def test_insert_invalid_index_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.insert(0, 5)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_insert_invalid_index_data_type_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.insert("0", 5)
        self.assertEqual(CUSTOM_DATA_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_insert_returns_the_list_with_inserted_element(self):
        self.custom_list.append(5)
        self.custom_list.append(10)
        self.custom_list.append(15)
        self.assertEqual([5, 10, 15], self.custom_list._CustomList__values)

        my_list = self.custom_list.insert(1, -3)
        self.assertEqual([5, -3, 10, 15], self.custom_list._CustomList__values)
        self.assertEqual(id(my_list), id(self.custom_list._CustomList__values))

    def test_pop_with_no_elements_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(NoElementsInListError) as ex:
            self.custom_list.pop()
        self.assertEqual("No elements in the list", str(ex.exception))

    def test_pop_removes_and_returns_element(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        el = self.custom_list.pop()
        self.assertEqual(5, el)
        self.assertEqual([], self.custom_list._CustomList__values)

    def test_clear_no_elements_returns_empty_list(self):
        self.assertEqual([], self.custom_list._CustomList__values)
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomList__values)

    def test_clear(self):
        self.custom_list.append(5)
        self.custom_list.append(15)
        self.assertEqual([5, 15], self.custom_list._CustomList__values)

        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomList__values)


if __name__ == '__main__':
    main()
