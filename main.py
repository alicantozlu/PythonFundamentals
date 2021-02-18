from math import *
import usefull_tools
from Student import Student  # This means import Student class from Student.py file
from StudentClass import StudentClass
from Chef import Chef
from ChineseChef import ChineseChef

print("Hello World")

print("\n----------------\n")

character_name = "Can"
character_age = "25"
print("Your name is " + character_name + ", you are " + character_age.__str__() + " years old.")
character_name = "Ali Can"
character_age = 25
print("Your name is " + character_name + ", you are " + character_age.__str__() + " years old.")

print("\n----------------\n")

phrase = "Python"
print("Selam " + phrase)
print("Selam \n" + phrase)
print("phrase = \" Python \" ")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[3])
print(phrase.index("t"))
print(phrase.index("on"))
print(phrase.replace("on", "an"))
print(phrase)

print("\n----------------\n")

print(2.4123)
print(-2.4123)
print(-2.4123 * 3 - (3 + 8) / 5)
print(19 % 3)
my_num = 5
print(str(my_num) + " is my number")
ur_number = -12
print("abs " + abs(ur_number).__str__())
print("pow " + pow(2, 5).__str__())
print("max " + max(2, 5).__str__())
print("min " + min(2, 5).__str__())
print("round " + round(2.523).__str__())
print("round " + round(2.223).__str__())
print("floor " + floor(2.5).__str__())
print("ceil " + ceil(2.5).__str__())
print("sqr " + sqrt(36).__str__())

print("\n----------------\n")

# your_name = input("Enter your name :")
# your_age = input("Enter your age :")
# print("Hello " + your_name + " , you are " + your_age)

print("\n----------------\n")

# num1 = input("Enter first num :")
# num2 = input("Enter second num :")
# number = num1 + num2
# print(num1 + " + " + num2 + " = " + number)
# print("---")
# num1 = input("Enter first integer num :")
# num2 = input("Enter second integer num :")
# number = int(num1) + int(num2)
# print(num1.__str__() + " + " + num2.__str__() + " = " + number.__str__())
# print("---")
# num1 = input("Enter first float num :")
# num2 = input("Enter second float num :")
# number = float(num1) + float(num2)
# print(num1.__str__() + " + " + num2.__str__() + " = " + number.__str__())

print("\n----------------\n")

friends = ["Ali", "Can", "Mert"]
print(friends)
print(friends[-2])
print(friends[0])
print(friends[1])

fruits = ["Elma", "Armut", "Portakal", "Muz", "Çilek"]
print(fruits[0:])
print(fruits[2:])
print(fruits[4:])
print("---")
print(fruits[3:4])
print(fruits[4:3])
print(fruits[4:4])
print("---")
print(fruits[1:3])
print(fruits[2:4])
print(fruits[1:4])
print("---")
print(fruits[-1:-3])
print(fruits[-3:-1])
print("---")
fruits[4] = "Kiraz"
print(fruits[0:])

print("\n----------------\n")

numbers = [1, 5, 2, 4, 7, 9, 3, 2, 4]
things = ["masa", "sandalye", "kitap", "kalem", "defter"]
print("numbers : " + numbers.__str__())
numbers.extend(things)
print(numbers)
print("---")
new_numbers = [41, 15, 42, 45, 77, 19, 33, 29, 42]
print("new numbers : \n" + new_numbers.__str__())
new_numbers.append(11)
print(new_numbers)
new_numbers.insert(1, 110)
print(new_numbers)
new_numbers.remove(11)
print(new_numbers)
new_numbers.pop()
print(new_numbers)
print("---")
last_numbers = [5, 1, 7, 8, 3, 9, 8, 8, 8]
print(last_numbers.index(8))
print(last_numbers.count(8))
things = ["masa", "sandalye", "kitap", "kalem", "defter", "defter"]
print("count")
print(things.count("defter"))
print("sort")
things.sort()
print(things)
new_numbers.sort()
print(new_numbers)
print("reverse")
new_numbers.reverse()
print(new_numbers)
print("clear")
new_numbers.clear()
print(new_numbers)
print("---")
last_numbers_2 = last_numbers.copy()
print(last_numbers_2)

print("\n----------------\n")

# Tuples

coordinates = (4, 5)
print(coordinates[1])
# coordinates[1] = 10 -> tuple data cant be changed

coordinates_2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(coordinates_2[2])

print("\n----------------\n")


# Functions

def say_hi():
    print("Hello!")


print("Top")
say_hi()
print("Bottom")


def say_yo(name, age):
    print("Yo " + name + ", you are " + str(age))


say_yo("Can", 25)
say_yo("Ali", 26)

print("\n----------------\n")


# Return


def cube(num):
    return num * num * num


# print("not gonna print")


print(cube(3))
result = cube(4)
print(result)

print("\n----------------\n")

is_male = False
is_tall = True

if is_male:
    print("You are a male")
elif not is_tall:
    print("You are tall")
elif is_male or is_tall:
    print("You are male or tall")
elif is_male and is_tall:
    print("You are male and tall")
else:
    print("You are not male and not tall")

print("\n----------------\n")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


number_1 = 1
if number_1 == 1:
    print("True")
else:
    print("False")

number_2 = 2
if number_2 != 2:
    print("True")
else:
    print("False")

at = "at"
if "at" == at:
    print("True")
else:
    print("False")

print(max_num(3, 8, 6))

print("\n----------------\n")

# Dictionaries

monthConversions = {
    0: "January",
    1: "February",
    "Mar": "March",
    "Apr": "April"
}

print(monthConversions["Apr"])
print(monthConversions.get("Mar"))
print(monthConversions.get(0))
print(monthConversions.get("ttt"))

print("\n----------------\n")

# While Loop

i = 1
while i <= 3:
    print(i)
    i += 1

print("Done with loop " + str(i))

print("\n----------------\n")

# For Loop

for letter in "Ali Can Tozlu":
    print(letter)
print("---")
toys = ["Car", "Lamb", "Doll", "House"]
for t in toys:
    print(t)
print("---")
for index in range(10):
    print(index)
print("---")
numero = 2
for index in range((4 - 2), (10 + numero)):
    print(index)
print("---")
toy_cars = ["Car_1", "Car_2", "Car_3", "Car_4"]
for index in range(len(toy_cars)):
    print(toy_cars[index])
print("---")

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first.")

print("\n----------------\n")

# Exponent Function

print(2 ** 3)


def raise_to_power(base_num, pow_num):
    result_1 = 1
    for index_1 in range(pow_num):
        result_1 *= base_num
    return result_1


print(raise_to_power(3, 2))

print("\n----------------\n")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][1])
print("---")

for row in number_grid:
    for col in row:
        print(col)

print("\n----------------\n")


def translate(phrase_1):
    translation_1 = ""
    for letter_1 in phrase_1:
        if letter_1 in "AEOUIaeiou":
            translation_1 = translation_1 + "g"
        else:
            translation_1 = translation_1 + letter_1
    return translation_1


# print(translate(input("Enter a phrase: ")))
print("---")


def translation_11(phrase_1):
    translation_1 = ""
    for letter_1 in phrase_1:
        if letter_1.lower() in "aeiou":
            if letter_1.isupper():
                translation_1 = translation_1 + "G"
            else:
                translation_1 = translation_1 + "g"
        else:
            translation_1 = translation_1 + letter_1
    return translation_1


# print(translation_11(input("Enter a phrase: ")))

'''
Comment
Comment 
Comment
'''

print("\n----------------\n")

# Try Except
'''

try:
    number_4 = int(input("Enter a number: "))
    print(number_4)
except:
    print("Invalid input")


try:
    value = 10/0
    number_3 = int(input("Enter a number: "))
    print(number_3)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
'''

print("\n----------------\n")

# Read File
'''
open("employee.txt", "r")  # read
open("employee.txt", "r+")  # read and write
open("employee.txt", "w")  # write
open("employee.txt", "a")  # append
'''
employee_file = open("employee.txt", "r")  # read
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readable())
print("---")
print(employee_file.read())
print("---")
'''
Okuma işlemi için en başta 2 kere readline çalıştırdıktan sonra read denildiğinde dosyanın geri kalanını gösteriyor
Aynı şekilde eğer önce read komutu çalışırsa sonrasında readline herhangi çıktı vermiyor
'''

employee_file.close()
employee_file = open("employee.txt", "r")
print(employee_file.readlines())
employee_file.close()

print("---")

employee_file = open("employee.txt", "r")
print(employee_file.readlines()[2])
employee_file.close()

print("---")

employee_file = open("employee.txt", "r")

for employees in employee_file.readlines():
    print(employees)

employee_file.close()

print("---")

employee_file = open("employee.txt", "a")

employee_file.write("\nMerve - Diyetisyen")

employee_file.close()

print("---")

employee_file = open("index.html", "a")

employee_file.write("\n<h1>HTML File</h1>")
employee_file.close()

print("---")

employee_file = open("index.html", "w")
employee_file.write("This erased the appended h1 tag abov")
employee_file.close()

print("\n----------------\n")

# Modules and pip

# import usefull_tools to this file

print(usefull_tools.roll_dice(10))

print("\n----------------\n")

# classes & objects

# Student class created and filled with attributes

# import Student.py

Student_1 = Student("Can", "PC", 3.2, False)

print(Student_1.name)

print("\n----------------\n")

# app.py created / Question.py created - quiz finished

print("\n----------------\n")

# object functions

student1 = StudentClass("Oscar", "Accounting", 3.1)
student2 = StudentClass("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())

print("\n----------------\n")

# inheritance - Chef.py created / ChineseChef.py created

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_sushi()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
