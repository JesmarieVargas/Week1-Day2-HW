# Task 1 Decisions at the Crossroad

number = int(input("Enter a number:"))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else: 
    print("The number is negative.")

# Task 2 The Greatest Showdown

user_input1 = int(input("Enter first number:"))
user_input2 = int(input("Enter second number:"))
user_input3 = int(input("Enter third number:"))

if user_input1 > user_input2 and user_input1 > user_input3:
    print("The largest number is", user_input1)
elif user_input2 > user_input1 and user_input2 > user_input3:
    print("The largest number is", user_input2)
elif user_input3 > user_input2 and user_input3 > user_input1:
    print("The largest number is", user_input3)
