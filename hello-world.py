import math 

message = 'Hello, world!'
print(message)


def hello_world(name):
    print('Hello, ' + name + '!')


hello_world('Kevin')


def hello_world_template(name):
    print("Hello, %s!" % name)


hello_world_template('Kevin')


list_example = []
list_example.append(1)
list_example.append(3)
list_example.append(5)
list_example.append(7)

print(list_example)

for i in list_example:
    print(i)

for x in range(3, 8):
    print(x)


count = 3

while count < 9:
    print(count)
    count += 1


class ClassTest:
    name = "Kevin"

    def print_name(self):
        return ("Hey, you found this message! Nice work, %s!" % self.name)


objectx = ClassTest()

print(objectx.print_name())

objectx.name = "Dane"

print(objectx.print_name())


# FizzBuzz working function:
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num


# Given a string, find the first consecutively repeating character in it
# and return it's index. If there are no repeating characters, return -1.
def find_repeat(str):
    reference = {}
    for char in str:
        if char in reference:
            index = str.index(char)
            return char, str.index(char, index + 1)
        else:
            reference[char] = 0
    return -1


# Given list of 1s and 0s, find the maximum number of consecutive
# '1s' in this list. This does not work.
def consecutive_numbers(numberlist):
    result = 0
    for i in numberlist:
        if numberlist[i] == 1:
            result += 1
    return print(result)


def squared_cubed(numbers):
	if math.sqrt(numbers[0]) ** 3 == numbers[1]:
		return True
	else:
		return False

print(squared_cubed([9, 27]))
