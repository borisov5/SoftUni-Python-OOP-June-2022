class HashTable:
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.max_capacity == self.size():
            self.__resize()
        index = self.__calc_index(key)
        index = self.__get_index(index)
        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def __get_index(self, index):
        if index == self.max_capacity:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__get_index(index + 1)

    def size(self):
        return len([el for el in self.__keys if el is not None])

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2

    def __str__(self):
        keys_values = [f"{self.__keys[index]}: {self.__values[index]}"
                       for index in range(len(self.__keys))
                       if self.__keys[index] is not None]


table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["is_pet_owner"] = True
table["weight"] = 100
table["some"] = "Test"
table["name"] = "Ines"
a = 5

print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
