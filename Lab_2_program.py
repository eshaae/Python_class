# Write program to apply if, match, break and continuestatementsfor decision making.
print("Number Analyzer Program (type 'exit' to quit)")

while True:
    user_input = input("\nEnter a number: ").strip()
    
    # Use 'if' to check exit condition
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break  # break out of the loop
    
    # Use 'if' and 'continue' to validate input
    if not user_input.isdigit():
        print("Invalid input! Please enter digits only.")
        continue  # skip the rest and ask again
    
    number = int(user_input)
    
    # Use 'if' for simple decision
    if number == 0:
        print("It is  number zero")
    
    else:
        print("It is positive number")
    
    # Use 'match' (Python 3.10+) for pattern matching on number properties
    match number % 3:
        case 0:
            print("Divisible by 3")
        case 1:
            print("Remainder 1 when divided by 3")
        case 2:
            print("Remainder 2 when divided by 3")


# WAP using for loop statement
# num = int(input("Enter a number to find its factorial: "))
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(f"Factorial of {num} is {fact}")


#  # Write a program to create  patterns using nestedloop
# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()  


#Program to demonstrate input validation using loop(only alphabets)
# def is_valid_name(name):
#     return name.isalpha()

# name=input("Enter name(only letters):").strip() #strip removes unnecessary whitespace,tabs 

# while not is_valid_name(name):
#     print("Invalid input.PLease use alphabetic characters only.\n")
#     name=input("Enter name(only letters):")

# print(f"Helllo,{name}! You entered a valid name")


#Program to demonstrate input validation using loop (only numbers)
# def is_valid_digit(number):
#     return number.isdigit()

# number=input("Enter number:").strip()

# while not is_valid_digit(number):
#     print("Invalid input.PLease enter numbers only.\n")
#     number=input("Enter number only:").strip()

# print(f"Helllo,{number}! You entered a valid number")

#A program using infinite loop
# num=1
# while(num==1):
#     print(f"Infinite loop with number{1}")