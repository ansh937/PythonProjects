
"""Recursion in Python (and in programming generally) is a technique where a function calls itself directly or indirectly in order to solve a problem. Recursive functions break down complex problems into simpler sub-problems, which are easier to solve. This technique is especially useful for problems that have a naturally recursive structure, such as tree traversal, factorial calculation, Fibonacci sequence generation, and more.



Base Case:

Every recursive function must have a base case, which is a condition that stops the recursion. Without a base case, the recursion would continue indefinitely, leading to a stack overflow error.
Recursive Case:

The recursive case is where the function calls itself with a modified argument, gradually working toward the base case.
Call Stack:

Each recursive call is placed on the call stack, and when the base case is reached, the function calls start to resolve (or "unwind") in reverse order, returning the results up the call stack.


def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Testing the recursive function
result = factorial(5)
print(result)  # Output will be 120


How It Works
Base Case: if n == 0 or n == 1: return 1. This prevents the function from calling itself infinitely.
Recursive Case: return n * factorial(n - 1). This calls factorial() with a smaller value, gradually reducing n until it reaches the base case.
For factorial(5), the recursion unfolds as:

factorial(5) calls factorial(4)
factorial(4) calls factorial(3)
factorial(3) calls factorial(2)
factorial(2) calls factorial(1) which returns 1
Then the results are returned back up the call stack:

factorial(2) returns 2 * 1 = 2
factorial(3) returns 3 * 2 = 6
factorial(4) returns 4 * 6 = 24
factorial(5) returns 5 * 24 = 120
Pros and Cons of Recursion
Pros:

Simplicity: Recursive solutions are often more straightforward and easier to understand, especially for problems like tree traversal and divide-and-conquer algorithms.
Elegance: Recursion can lead to elegant solutions that closely align with the problem's natural structure.
Cons:

Performance: Recursive solutions can be less efficient, as each recursive call consumes stack space. In Python, deep recursion can lead to a stack overflow.
Memory Usage: Recursion uses more memory due to the call stack, which may lead to issues for large inputs.

"""
# 0,1,1,2,3,5,8,13
  #1 is 3rd   2 is 4th  and 3 is 5th term  so 5th term nikalna as 5 we have to add 3rd and the 4th term
def fibo(n):
  if n<=1:
    return n
  else:
    return fibo(n-1)+fibo(n-2)# vanna khojeko 5th nikalna xa vaney n vaneko 5 ho so 5-1 vaneko 4t term + n-2  3rd term 

n=int(input("'Enter a number"))                               #4th term +3rd term
if n<=0:
  print("Enter a positive number")
else:
  print("Fibonacci series")
  for i in range(n):
    print(fibo(i))
  


