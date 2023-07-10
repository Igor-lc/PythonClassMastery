'''Task 1: AddConstantFunctor
Create a functor called AddConstantFunctor that adds a constant value to a given number. For example, if the constant is 5, the functor should add 5 to any number passed to it.

Task 2: StringLengthCheckFunctor
Implement a functor called StringLengthCheckFunctor that checks whether a given string has more than 5 characters. The functor should return true if the string is longer than 5 characters and false otherwise.

Task 3: MultiplyFunctor
Create a functor called MultiplyFunctor that multiplies two numbers together. The functor should take two arguments and return their product.

Task 4: CelsiusToFahrenheitFunctor
Implement a functor called CelsiusToFahrenheitFunctor that converts a temperature in Celsius to Fahrenheit. The functor should take a temperature in Celsius as an argument and return the equivalent temperature in Fahrenheit.

Task 5: IntegerSortingFunctor
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
