#0 to 9 are decimal numbers(base 10)
#Bianary numbers-The binary system is used in computers and digital systems. It is based on 2 and uses only the digits 0 and 1.
#Octal (Base 8)-The octal system is based on 8 and uses the digits 0-7. It was used historically in computing.
# HexaDecimal(Base 16)-The hexadecimal system is based on 16 and uses the digits 0-9 and the letters A-F (where A=10, B=11, C=12, D=13, E=14, F=15). It is often used in computing because it is more compact than binary and octal.

decimal=int(input("Enter the number"))
print("The conversion of decimal number in ",decimal,"is")
print(bin(decimal),"in bianary")
print(oct(decimal),"in octal")
print(hex(decimal),"in hexa decimal")


#*video no 24