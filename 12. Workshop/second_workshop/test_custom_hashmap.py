# Coll
# Overflow
# Same key -> should not be duplicated
# Test __str__ logic


from unittest import main, TestCase

from custom_hashmap import HashTable


class TestHashTable(TestCase):
    def test_init(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        self.assertEqual([None, None, None, None], table._HashTable__values)
        self.assertEqual(4, table.max_capacity)

    def test_get_item_dunder(self):
        table = HashTable()
        table["name"] = "Test"
        table["age"] = 0
        result = table["name"]
        self.assertEqual("Test", result)

    def test_get_item_dunder_non_existing_key_raises(self):
        table = HashTable()
        table["name"] = "Test"
        table["age"] = 0
        with self.assertRaises(KeyError) as ex:
            # Non existing key
            table["asd"]
        self.assertEqual("asd", str(ex.exception.args[0]))




if __name__ == "__main__":
    main()
