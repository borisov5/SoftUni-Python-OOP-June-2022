CUSTOM_INDEX_ERROR_MESSAGE = 'Invalid index'


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
            raise IndexError('Invalid index')
        except TypeError:
            raise ValueError('Index is not a valid integer. Please pass an integer number')

    def get(self, index):
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError(CUSTOM_INDEX_ERROR_MESSAGE)

    def extend(self, vals):
        try:
            self.__values.extend(vals)
        except TypeError:
            raise ValueError('Extend method works only with iterables objects')


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
        self.assertEqual('Invalid index', str(ex.exception))

    def test_pass_invalid_integer_index_to_remove_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.remove("0")
        self.assertEqual('Index is not a valid integer. Please pass an integer number', str(ex.exception))

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


if __name__ == '__main__':
    main()
