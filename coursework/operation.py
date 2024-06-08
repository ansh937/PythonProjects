from coursework.read import *
def input_validate(data, name):
    all_kitta = []
    i = 0
    rented = False 
    while i < len(data) and not rented: 
        while True:
            choice = input("Do you want to purchase multiple lands? (yes/no): ").lower()
            if choice == "yes":
                kitta = input("Enter the kitna number for purchase (enter 'done' to finish): ").strip()
                while kitta.lower() != "done":
                    found = False
                    for j in range(len(data)):
                        if kitta == data[j][0].strip():
                            print(data[j][5])
                            print("Kitna number is available.")
                            if data[j][5].strip() == "Available":
                                all_kitta.append(kitta)
                                print("Kitna number", kitta, "is available for purchase.")
                                data[j][5] = "Not Available"
                                found = True
                                break
                            else:
                                print("Kitna number", kitta, "is already purchased.")
                                found = True
                                break
                    if not found:
                        print("Kitna number", kitta, "is not available in our records.")
                    kitta = input("Enter the kitna number for purchase (enter 'done' to finish): ").strip()
                generate_purchased_invoice(all_kitta, name)  # Pass name to generate_purchased_invoice
                save_data(data)
                rented = True  # Set rented flag to True after renting
                break
            elif choice == "no":
                while True:
                    kitta = input("Enter the kitna number for purchase (enter 'done' to finish or 'quit' to exit): ").strip()
                    if kitta.lower() == "done":
                        generate_purchased_invoice(all_kitta, name)  # Pass name to generate_purchased_invoice
                        # return all_kitta
                    else:
                        found = False
                        for j in range(len(data)):
                            if kitta == data[j][0].strip():
                                print(data[j][5])
                                print("Kitna number is available.")
                                if data[j][5].strip() == "Available":
                                    all_kitta.append(kitta)
                                    data[j][5] = "Not Available"
                                    print("Kitna number", kitta, "is available for purchase.")
                                else:
                                    print("Kitna number", kitta, "is already purchased.")
                                found = True
                                break
                        if not found:
                            print("Kitna number", kitta, "is not available in our records.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        i += 1
    else:
        if not rented:
            print("Kitna number is not available in our records.")
    return all_kitta




def generate_purchased_invoice(all_kitta,name): # ["101","102"]
    # print(all_kitta)
    name = input("what is your name: ")
    contact = input("contact: ")
    datas = readData()
    for data in datas:
        data.append(name)
        data.append(contact)
    print(datas)
    return all_kitta 


def save_data(datas):
#   print(datas)
    file= open("datas.txt","w")
    to_save=""
    for data in datas:
        to_save+=",".join(data)+ "\n"
#   print(to_save)
    file.write(to_save)
    file.close()
#   print("wrote")