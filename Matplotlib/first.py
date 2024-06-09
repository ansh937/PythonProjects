import matplotlib.pyplot as  plt

squares=[1,4,9,16,25]
fig, ax = plt.subplots()#*This line creates a figure (fig) and a set of subplots (ax). The plt.subplots() function returns a tuple containing a figure and axes object(s).The function can generate one or more plot
ax.plot(squares)#*This line plots the data in the squares list on the ax (axes) object. 
#An Axes object that is the area where data is plotted.
plt.show()#*This line displays the figure with the plot. 

#*fig: A Figure object that serves as the top-level container for all plot elements.
#*ax: An Axes object that is the area where data is plotted.

