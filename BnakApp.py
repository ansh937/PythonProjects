
def show_Balance(balance):
  print(f"your balalce in NMB bank is {balance:.2f} ")

def deposit():
  amount=float(input("Enter the amount you want to deposit"))
  if amount<0:
    print("Enter amount greater than zero")
  else:
    return amount
  

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))
    
    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount < 0:
        print("Amount should be more than zero.")
        return 0
    else:
        return amount


def main():
    balance=0
    print("Welcome to MNB Bank Pokhara 🏦")
    while True:
      try:
          user_input = int(input("""\nEnter:
              1. to show Balance
              2. to Deposit cash
              3. to withdraw cash
              4. to exit the program\n
          """).strip())  # .strip() removes any leading/trailing whitespace
          if user_input == 1:
              show_Balance(balance)
          elif user_input == 2:
              balance+=deposit()
          elif user_input == 3:
              balance-=withdraw(balance)# withdraw la withdrawn amout return garxa 
          elif user_input == 4:
            break
          else:
              print("Please provide a valid input.")
      except :
          print("Invalid input, please type 1, 2, 3, or 4 to use the bank system.")
          
          
if __name__=="__main__":        
  main()
#In Python, functions need to be defined before they are called. Therefore, after defining all necessary functions, calling user_info at the end ensures that the code inside user_info executes when the script is run.