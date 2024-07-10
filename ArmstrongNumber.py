# #armstrong number are those whose sum of squares or cubes according to the length of the number is equal to the number
# lower=int(input("Enyter the lower digit number"))
# upper=int(input("Enter the upper digit number"))
# for number in range(lower,upper+1):
#   length=len(str(number))
#   sum=0
#   temp=number# This is done so that we can manipulate temp without altering the original number.
#   while temp>0:
#     digit=temp%10#*last value(obtain garna) ko cube likalna(turn by turn cube garna)This line extracts the last digit of temp by taking the remainder when temp is divided by 10. This is done using the modulus operator %
#     sum+=digit**length
#     temp //=10#flow division(last ko cube nikali sakiyo so last ko number lai eliminate garna ko lagi(if 407 last ko 7 hati sako so aaba flow division ma 40.7 point agadi ko linxa 40))
#   if number==sum:
#       print(number)






lower=int(input("enter a number to be the upper digigt for the armstrong number"))
upper=int(input("enter a number for the upper digit of the armstrong number"))
for number in range(lower,upper+1):
  sum=0
  length=len(str(number))
  temp=number
  while temp>0:
    digit=temp%10
    sum+=digit**length
    temp //=10
  if number==sum:
      print(number)  