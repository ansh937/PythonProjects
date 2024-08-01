#FInd the ACII
# number_or_char=input("enter the number or symbol or character to find the ACII value of: ")
# print("The ACII value of the given term is",ord(number_or_char))

#*FInd the HCF of the number (two number)
"""
lets find the HCF in common way of 12 and 30 
6|12
2|2
 |1
 
6|30
5|5
 |1
 
SO here the HCF is 6 , 30 can be divided by 15 as a HCF but once the 12 is divided by 6 so we choose 6

Sure, here’s the process formatted for easy copying:

### Prime Factorize each number:

**Prime factors of 12:**
\[ 
12 = 2^2 \times 3^1 
\]

**Prime factors of 30:**
\[ 
30 = 2^1 \times 3^1 \times 5^1 
\]

### Identify the common prime factors:

**Common prime factors of 12 and 30 are \(2\) and \(3\).**

### Multiply the lowest powers of the common prime factors:

**The lowest power of 2 is \(2^1\).**

**The lowest power of 3 is \(3^1\).**

### Therefore, the HCF is:
\[ 
2^1 \times 3^1 = 2 \times 3 = 6 
\]

**So, the HCF of 12 and 30 is 6.**

"""
#lets look at 12 and 30 , yaha chai sano 12 xa ani sano lai kun la devide garxa teshaila pani thulo lao devide garna paro HCF likalna ko lagi so yaha hamley sano linxau (thulo ko HCF sano lai namilna ne sakxa )
def HCF(x,y):
  
  if x>y:
    smaller=y
  else:
    smaller=x 
  for i in range(1,smaller+1):
    if(x%i==0)and(y%i==0):
      HCF_=i
  return HCF_

print("the HCF  of the given numbers is", HCF(12,30))    


#*Find the factors of the numbers given by the user

number=int(input("Enter the number of which you want the factors of"))
number_in_list=[]
for i in range(1,number+1):
  if number%i==0:
    number_in_list.append(i)
print("The factors of the number ",number,"are ",number_in_list)



#*Taking two inputs from the user in a single line
a, b = map(int, input("Enter two numbers separated by a space: ").split())
print(a,b)

#*if you want to write by separating with comma
x, y = map(int, input("Enter two numbers separated by a comma: ").split(','))





