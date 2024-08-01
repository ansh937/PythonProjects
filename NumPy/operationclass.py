import numpy as np
import matplotlib.pyplot as plt
class IntArray:
  def __init__(self,int_array):#int array is the object
    if not isinstance(int_array,np.ndarray)or int_array.dtype !=int:#This checks if int_array is not an instance of the np.ndarray class.             int_array.dtype != int: This checks if the data type (dtype) of the elements in int_array is not an integer.
# isinstance() is a built-in Python function used to check if an object is an instance of a particular class or its subclasses. It returns a boolean value: True if the object is an instance of the specified class or its subclasses, False otherwise.


      raise ValueError("input must be NUMPY array or intigers")
    #*"instance of" often refers to a specific object created from a class. 
    self.int_array=int_array
    
  def display(self):  
    print(self.int_array)
    
  #compam=ny donot wanna count one by one employee so 
  def salary(self):
    array_shape=self.int_array.shape
    money_for_product=np.full(array_shape,7)#Return a new array of given shape and type, filled with fill_value.
    salaries=self.int_array*money_for_product
    
    print(f"people made {self.int_array} products and this is their salaryes {salaries}")
    
  def show_data(self):
    x=np.arange(len(self.int_array))
    plt.plot(x,self.int_array,marker="o",markersize=5)#plt.plot: This function from the matplotlib.pyplot module is used to create a 2D line plot. and markersize helps to resize the marker
    plt.title("productivity of the employees",fontsize=20)
    plt.xlabel("Rank of the employees",fontsize=14)
    plt.ylabel("products/months",fontsize=14)
    plt.xticks(x)#This sets the ticks at positions [0, 1, 2, ..., 9] as the The plt.xticks(x) function in Matplotlib sets the locations and labels of the x-axis ticks based on the values in the array x
    plt.scatter(x,self.int_array,color=(0, 0.8, 0),s=50)#you can also costomize color and # Adjust the size of scatter points here
    plt.tick_params(labelsize=14)#The labelsize parameter specifically controls the font size of the tick labels.
    plt.grid()#The plt.grid() function in matplotlib is used to add grid lines to your plot
    plt.show()
    """x: This is the data for the x-axis. In your case, it is np.arange(len(self.int_array)), which creates an array of integers from 0 to the length of self.int_array minus one. This ensures that each element in self.int_array is plotted at its corresponding index.
    self.int_array: This is the data for the y-axis, representing the integer array stored in the IntArray class instance.
    marker="o": This argument specifies that each data point should be marked with a circle ("o") on the plot.
    """