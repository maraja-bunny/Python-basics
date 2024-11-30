
# # End goal -- doing analysis
# # Print hellow world command
# print("Hello World\n\n\n\n")

# """1. IDE Installation vscode/pycharm-- Integrated Developement Environment. 
# 2. Github - 3. Python Basics 4. Data analysispandas - """

# # Adding two numbers
# num1 = 4
# num2 = 5
# answer = num1+num2
# print(answer," This is the sum of num1 and num2\n\n")


# # adding two numbers using a function.
# def add_two_numbers(num1,num2):
#     answer = num1+num2
#     print(answer," This is the sum of num1 and num2\n\n")

# # Call the function
# add_two_numbers(4,7)
# add_two_numbers(4,8)
# add_two_numbers(12,7)

# # My name function

# def girl_name(name):
#     print("Her name is: ",name)
    
# girl_name("Beril")  
# girl_name("Carol")
# girl_name("Nazi")
    
# #Substract two numbers
# def subtract_two_numbers(num1,num2):
#     answer = num1-num2
#     print(answer," This is the difference of num1 and num2")

# #Call the function
# subtract_two_numbers(10,8)
# subtract_two_numbers(10,11)

# def subtracttwonumbers(num2):
#     num1 = 10
#     answer = num1-num2
#     print(answer," This is the difference of num1 and num2")
    
# subtracttwonumbers(5)
# subtracttwonumbers(2)
    
#a and b 
# a is known but b is not known
# c is the prduct of the two.
# c is known
# find b
print("\n\n\n")
def product(a,c):
    b=c//a
    print(b," Is the missing number")


# product(2,10)


#Devide the number by 2 then if there is a remainder the number is odd and if there is no remainder the number is even

def even_or_odd(x):
    if x%2 > 0 :
        print("Odd")
    else:
        print("Even")

even_or_odd(2)