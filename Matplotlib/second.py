import matplotlib.pyplot as f
# import seaborn as sns



# import seaborn as sns
# data=[2,5,105,600,800]
# fig,ax=f.subplots()
# ax.plot(data,linewidth=2)
# ax.set_title("Numbers")
# ax.set_xlabel("values")
# ax.set_ylabel("Numbers value")
# ax.tick_params(labelsize=16)
# f.show()


# #*we use the style here 
# f.style.use('seaborn-v0_8-darkgrid')#*This the faous one with grid 
# f.style.use('seaborn-v0_8-paper')
# f.style.use('seaborn-v0_8-notebook')
f.style.use('seaborn-v0_8-darkgrid')

#*Now in the figure in the x-coordinate the 25 was shown in the square of the 4 let us give the x-coordinate(input numbers as the y coordinate is the squares)
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]



fig, ax = f.subplots()#*This line creates a figure (fig) and a set of subplots (ax). The plt.subplots() function returns a tuple containing a figure and axes object(s).The function can generate one or more plot
ax.plot(input_values,squares,linewidth=3)#*This line plots the data in the squares list on the ax (axes) object. 
#An Axes object that is the area where data is plotted.
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("value",fontsize=18)
ax.set_ylabel("Square of value",fontsize=18)
ax.tick_params(labelsize=14)
f.show()#*This line displays the figure with the plot. 

#*fig: A Figure object that serves as the top-level container for all plot elements.
#*ax: An Axes object that is the area where data is plotted.
