import numpy as np 
from operationclass import IntArray
# def file_haldeling():
#     lines = []
#     with open("/Users/macm2/Desktop/pythoon/NumPy/company.txt", "r") as file:
#         for line in file:
#             values = line.strip().split(",")
#             # Filter out empty strings
#             int_values = [int(valu) for valu in values if valu]
#             # Skip empty lines
#             if int_values:
#                 lines.append(int_values)
    
#     data_frame = np.array([np.array(row) for row in lines], dtype="object")
#     return data_frame

# def main():
#     data_frame = file_haldeling()
#     print(data_frame)

# main()

#which company makee minimum and the maximum
def productivity_of_company(order, data_frame):
    # this is without the numpy function sum()
    """
    num_of_products = 0
    for element in data_frame[order]:
        num_of_products += element

    return num_of_products
    """
    return np.sum(data_frame[order])

def max_productivity(data_frame):
    i = 0
    best_company = i + 1
    num_of_products = 0

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result > num_of_products:
            num_of_products = result
            best_company = i + 1

    print(f"The best company is the {best_company}. company with {num_of_products} products made")

def min_productivity(data_frame):
    i = 0
    worst_company = i + 1
    num_of_products = productivity_of_company(0, data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result <= num_of_products:
            num_of_products = result
            worst_company = i + 1

    print(f"The best company is the {worst_company}. company with {num_of_products} products made")

def mean_products(data_frame):
    for i in range(len(data_frame)):
        average = np.mean(data_frame[i])
        print(f"On average, one human from {i}. company produced {average} products")

    """
    for element in np.nditer(my_2d_array):
        print(element)

    for row in my_2d_array:
        for element in row:
            print(element)
    """

    sum = 0
    num_elements = 0

    for row in data_frame:
        for element in row:
            num_elements += 1

    for row in range(len(data_frame)):
        row_sum = np.sum(data_frame[row])
        sum += row_sum

    total_mean = sum / num_elements

    print(f"Mean of the entire monopoly is {total_mean} per employee")
    




def file_handling():
    lines = []
    with open("/Users/macm2/Desktop/pythoon/NumPy/company.txt", "r") as file:
        for line in file:
            values = line.strip().split(",")
            # Filter out empty strings and ensure all values are integers
            int_values = []
            for valu in values:
                if valu.strip():  # Check if the string is not empty
                    try:
                        int_values.append(int(valu))
                    except ValueError:
                        print(f"Warning: Non-integer value '{valu}' encountered and skipped.")
            if int_values:#list empty means False in the python 
                lines.append(int_values)
                
    data_frame = np.array([np.array(row) for row in lines], dtype='object')
    return data_frame
    # data_frame = np.array([np.array(row) for row in lines], dtype="object")#for row in lines: np.array()
    # return data_frame
    
def main():
    data_frame = file_handling()
    print(data_frame)
    
    # Ensure that we are passing a NumPy array with integer dtype
    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()
    max_productivity(data_frame)
    min_productivity(data_frame)
    mean_products(data_frame)
    
if __name__ == "__main__":
    main()

"""The condition if int_values: checks if the list int_values is not empty. In Python, an empty list is considered False in a boolean context, while a non-empty list is considered True. Here's a breakdown of how this works:
int_values = []
int_values is initialized as an empty list.
If int_values is not empty, the condition evaluates to True, and the list is appended to lines.
If int_values is empty, the condition evaluates to False, and the list is not appended to lines.
"""

