
# print("Welcome to perform calculations:")
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))

# exp=input("Enter any symbols (+,-,*,/):")
# match exp:
#     case '+':
#         print("Addition of two numbers:",a+b)
#     case'-':

#         print("Subtraction of two numbers:",a-b)
#     case'*':
#         print("Multiplication of two numbers is:",a*b)
    
#     case'%':
#             print("Remainder of this operation:",a%b)

#     case'/':
#         if(b==0):
#             print("Error!!! Invalid user input")
      
    
#             choice=input("Choice---Yes -----OR-----No:")
#             match choice:
#                 case'Yes'|'yes':
#                     b=int(input("Enter divisor greater than 0:"))
#                     print("Division of two numbers:",a/b)
#                 case'No'|'no':
#                     print("Enter choice:No")
#         else:
#             print("Division of two numbers:",a/b)

#declaring variable
# course_name="Python Programming in BICTE"
# id=1.0
# # declaring constant
# CODE="ICT.Ed.477"

# #printing variables with constant
# print("Printing variables with constant")
# print(id,course_name,CODE)

# #printing datatypes of variables
# print("\nPrinting datatypes of variables")
# print(type(course_name))
# print(type(id))

# #Performing typecasting
# print("\nPerforming typecasting from float into int")
# print(int(id))


# A program to demonstrate the different types of operators and performing calculations
#Using method and switch case and if else statement
#Defining method
# def calculator(a,b,opt):
#     #switch case statement
#     match opt:
#         case '+':
#             return a+b
    
#         case'-':

#            return a-b
#         case'*':
#             return a*b
    
#         case'%':
#             return a%b

#         case'/':
#             if(b==0):
#                 return "Cannot divisible by zero!!!"
      
#             else:
#                return a/b
        
#         # _ is a wildcard that matches anything not previously matched.
#         # part of structural pattern matching
#         #a convention meaning “don’t care” or “match anything.”

#         case _:
#             return "Invalid input"

# # Taking input from users
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# opt=input("Enter any symbols (+,-,*,/,%):")

# #Calling the method
# result=calculator(a,b,opt)
# print("Result:",result)

#A program making use of I/O functions
#Taking input from users
# name=input("Enter your name:")
# address=input("Enter your address:")
# age=input("Enter your age:")


# #Printing values entered by users
# print("\nHello! your name is",name,"adress is",address,"and age is",age)


#taking input and displaying output using method
# def display():
#     name=input("Enter username:")
#     age=int(input("Enter age:"))
#     print("Username is",name)
#     print("Age is",age)

    
# display()




# def calculator(a,b,opt):
#     #switch case statement
#     match opt:
#         case '+':
#             return "Addition",a+b
    
#         case'-':

#            return "Subtraction",a-b
#         case'*':
#             return "Multiplication",a*b
    
#         case'%':
#             return "Remainder",a%b

#         case'/':
#             if(b==0):
#                 return "Cannot divisible by zero!!!"
      
#             else:
#                return "Division",a/b
            
        
#         # _ is a wildcard that matches anything not previously matched.
#         # part of structural pattern matching
#         #a convention meaning “don’t care” or “match anything.”

#         # case _:
#         #     return "Invalid input"

# # Taking input from users
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# opt=input("Enter any symbols (+,-,*,/,%):")

# #Calling the method
# result=calculator(a,b,opt)
# print("Result:",result)


a=12
b=12
print(12+a+b)