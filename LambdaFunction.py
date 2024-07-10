#lambda functions are typically used for short, simple operations that are not reused elsewhere in the code.)
# The map function allows you to apply transformations to iterable objects in a single line of code.yashley sabai iterables ma function lagaidiney kam garcha 
#iterables are list tuples string 
#lambda  are often used where a simple function is required temporarily.
#*Using lambda and filter fnction()
#A lambda function in Python is a small anonymous function defined using the lambda keyword. It can take any number of arguments but can only have one expression. The expression is evaluated and returned. Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
# Regular function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

# Using the lambda function
print(add_lambda(3, 5))  # Output: 8




#*Filter function 
#*The filter function in your code is used to create a new list (or more accurately, an iterator) 
#The filter function in Python is used to construct an iterator from elements of an iterable for which a function returns true. It filters the elements based on the function provided.
#The filter function returns an iterator, so you often need to convert it to a list or another iterable to see the filtered results.
# A list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Regular function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Using filter with the regular function
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# Using filter with a lambda function
even_numbers_lambda = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers_lambda))  # Output: [2, 4, 6, 8, 10]#*lambda function ley true return gareko matrrai filter function ley as a iterator (list )ma store garera rakhxa natra fulse return gareko chai rakhdaina 

#*FILTER FUNCTION USE 
#*lambda x: x % 79 == 0: This is a lambda function that takes a number x and returns True if x is divisible by 79 (x % 79 == 0), and False otherwise.
#*filter: The filter function applies the lambda function to each number in the range from 1 to 999. It constructs an iterator that contains only the numbers for which the lambda function returns True.
def number_divisible_byanothernumber():
  print("the number divisible by 79 are ")
  numbers_divisible=filter(lambda x:x%79==0,range(1,1000))
  print(list(numbers_divisible))
number_divisible_byanothernumber()


#*python program to display the power of 2 using annonomous function(lambda function .. lambda functions are typically used for short, simple operations that are not reused elsewhere in the code.)
# The map function allows you to apply transformations to iterable objects in a single line of code.yashley sabai iterables ma function lagaidiney kam garcha 
#iterables are list tuples string 
nterms=int(input("enter a number "))
result=list(map(lambda x: 2**x,range(nterms+1)))
print(result)
