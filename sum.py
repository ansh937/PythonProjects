# sum=0
# while True: 
#   number=input("Enter the number that you want to add or write end to end the program: ")
#   if number.lower()=="end":
#     break
#   else:
#     sum+=int(number)
# print(sum)

#*  give only one number like 5 and the sum should be 15 ...5+4+3+2+1 like this

# num=int(input("enter a number "))
# sum2=0
# if num<0:
#   print("number should be greater than 0")
# else:
#   while num>0:
#     sum2+=num#first the sum will be 5 then 5+4 then 9+3 then 2 and 1 , one by one 
#     num-=1
#   print(sum2)  
    
#*python program to display the power of 2 using annonomous function(lambda function .. lambda functions are typically used for short, simple operations that are not reused elsewhere in the code.)
# The map function allows you to apply transformations to iterable objects in a single line of code.yashley sabai iterables ma function lagaidiney kam garcha 
#iterables are list tuples string 
nterms=int(input("enter a number "))
result=list(map(lambda x: 2**x,range(nterms+1)))
print(result)