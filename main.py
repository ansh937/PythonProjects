from read import *
from operation import *
def mainFile():
  run=True
  while run:
    print("""
          ------------------------------------------------
          |   How would you like to move forward?         |
          ------------------------------------------------
          | Enter 1: To Display Available Lands           |
          -------------------------------------------------
          | Enter 2: To Rent the  Available Land          |
          -------------------------------------------------
          | Enter 3: To return Rented  Land               |
          -------------------------------------------------
          | Enter 4: To Exit from the program             |
          -------------------------------------------------
          
          """)
    
    # try:
    option=int(input("\nEnter an option to continue: "))
      
    if option == 1:
        print("Displaying Available Lands")
        display_data()
    elif option == 2:
      rentLand()
    elif option == 3:
        returnLand()
        
    elif option == 4:
        print("We appreciate your visit!")
    run=False
          
    # except:
    #   print("<------------------!!!!!!!Error Occoured please try again!!!!------------------------>")


def display_data():
    data = readData()
    
    print(f"""
|------------------------------------------Techno Property Nepal-------------------------------------------|
|----------------------------------------------Lands fro rent----------------------------------------------|
|----------------------------------------------------------------------------------------------------------|
|SN \t    | Kitta No\t    |      Location |Direction \t    |Anna \t    | Price(Rs)     | Availability |
|----------------------------------------------------------------------------------------------------------|""")
    
    for i in range(len(data)):
        element = data[i]
        print("| ", end='')
        print(str(i+1).ljust(10), element[0].ljust(15), element[1].ljust(15), element[2].ljust(15), element[3].ljust(15), element[4].ljust(15), element[5], sep="|")
        print("-----------------------------------------------------------------------------------------------------------|")

    choice = input("do you want to go to mein menu or exit (y/n)").lower()
    if choice == "yes":
      mainFile()
    elif choice == "no":
      exit()
    else:
      print(print("invalid coice"))
  
  
  
def rentLand():
    data = readData()
    all_kitta = input_validate(data)  
    generate_purchased_invoice(all_kitta)  # Pass all_kitta to generate_purchased_invoice

def returnLand():
  print("returning")
  

mainFile()  