from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'Meow'


class Dog(Animal):
    def make_sound(self):
        return 'Wolf'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog()]
animal_sound(animals)
