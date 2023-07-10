'''Task 1: AddConstantFunctor
Create a functor called AddConstantFunctor that adds a constant value to a given number. For example, if the constant is 5, the functor should add 5 to any number passed to it.

Task 2: StringLengthCheckFunctor
Implement a functor called StringLengthCheckFunctor that checks whether a given string has more than 5 characters. The functor should return true if the string is longer than 5 characters and false otherwise.

Task 3: CelsiusToFahrenheitFunctor
Implement a functor called CelsiusToFahrenheitFunctor that converts a temperature in Celsius to Fahrenheit. The functor should take a temperature in Celsius as an argument and return the equivalent temperature in Fahrenheit.

Task 4: IntegerSortingFunctor
Create a functor called IntegerSortingFunctor that sorts a list of integers in ascending order. You can use any sorting algorithm of your choice (e.g., bubble sort or insertion sort) to implement the functor.'''

class AddConstantFunctor:
    def __init__(self, constant_value):
        self.constant_value = constant_value

    def __call__(self, value):
        return value + self.constant_value

    def call(self, value):
        return value + self.constant_value

obj = AddConstantFunctor(5)
print(obj(2))
print(obj.call(2))


class StringLengthCheckFunctor:
    def __init__(self, lenght=5):
        self.lenght = lenght

    def __call__(self, string):
        return len(string) > self.lenght

obj = StringLengthCheckFunctor()
print(obj('123456'))


class CelsiusToFahrenheitFunctor:
    def __call__(self, celsius):
        return celsius * 9 / 5 + 32

obj = CelsiusToFahrenheitFunctor()
print(obj(20))