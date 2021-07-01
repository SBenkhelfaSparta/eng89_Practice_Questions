# Q1) Declare a function called username that takes one argument as a string and return the name

# def username(name):
#     return(name)
#
# print(username("Salem"))


# - Not in the question
# name = input("Enter name:").title()
# print(username(name))


# Q2) Declare a list with nbumbers 1:5. Iterate through the list and display it

# ls = [1,2,3,4,5]
# for i in ls:
#      print(i)


# Q3) AND - && - & - ==. which one return the boolean value?

# name = "Salem"
#
# if name == "Salem":    #This one
# if name AND "Salem":
# if name && "Salem":
# if name & "Salem":


# Q4) What is the differene between a list and a tuple?

# - A list is mutable. syntax []
# - A tuple is immutable. syntax ()

# Q5) Can we add an element to list and a tuple?
# Can the element of tuple be different types?


# - list yes. tuple no.
# - tuple - yes


# Q6) Create a dictionary with key, value pairs , first_name and last_name

# dict = {'firstname' : "Salem",
#         'lastname' : "Benkhelfa"}
# print(type(dict))
# print(dict)


# Q7) Add and remove a new key value and print out a key

# dict = {'firstname' : "Salem",
#         'lastname' : "Benkhelfa"}
#
# dict['course'] = 'devops' # Adds a key/value
# del dict['course'] # Deletes a key/value
#
# print(dict)
# print(dict['lastname']) # Print a specific key/value


# Q8) Create a class called student, initialise a class and create an object of the class

# class Student:
#     def __init__(self):
#         pass
#
# obj = Student()


#Q9) Create two functions that take two arguments each. f1 called AddValues and f2 called SubtractValues and return the addition and subtraction

# def AddValues(num1,num2):
#     return num1 + num2
#
# def SubtractValues( num1, num2):
#     return num1 - num2
#
# print(AddValues(1,2))
# print(SubtractValues(4,2))


# - Q10) Declare a dictionary with three shopping items with cost. eggs = 1.2, milk = 2.3, and bread 1
# - write a function that returns the total value
#
# shopping_list = {'eggs' : 1.2, 'milk': 2.3, 'bread': 1}
#
#
# def total_value():
#      return shopping_list['eggs'] + shopping_list['milk'] + shopping_list['bread']
#
# print(total_value())


#print(shopping_list)
#print(type(shopping_list['eggs']))


# - Q11) prompt the user to enter an int, declare a function that checks if the number is odd or even and dispkay back to the user : the number you have entered is odd/even

# def odd_even(num):
#     if num % 2 == 0:
#         print(f"The number you entered is even: {num}")
#     else:
#         print(f"The number you entered is odd {num}")
#
# odd_even(int(input("Please enter a number: ")))


# - Q12) select the correct syntax- 1 -super.__init(). 2- super()__init(). 3 super().__init(). 4 - super().__init__()

# - Answer is (4) super().__init__()


# - Q13) Declare a tuple with three values of your choice. Iterate through the tuple and display the values.
# - Delete the last index-- YOU CANNOT
#
# tuple = ('this', 2, 'test')
#
# for i in tuple:
#     print(i)
#


# Q14) Create a class called Student with one method called student_data that returns student_name. Create another class called devops_student which inherits the Student class.

#class Student:
#     def student_data(self):
#         return "Salem"
#
# class DevopsStudent(Student):
#     def __init__(self):
#         super().__init__()
#
# obj = DevopsStudent()
# print(obj.student_data())
# # OR
# print(DevopsStudent().student_data())


# Q15 )Declare a variable called city. Declare a method that takes city as an argument and value of the city as london and method checks if value islondon then true, if not False
#
# city = "London"
#
# def check_city(cityname):
#     if cityname == "London":
#         return True
#     else:
#         return False
#
# print(check_city(city))

# - Q16) import sys module, import math, print the random method.
# -Create a function that takes two arguments and calculate the percentage of the two arguments and return the answer


# import random
# import sys
# import math
#
# def percentage(num1, num2):
#     return (num1 *100) / num2
#
# print(percentage(random.randint(0,100), random.randint(0,100)))
