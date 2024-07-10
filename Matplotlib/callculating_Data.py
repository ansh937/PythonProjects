import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values]
plt.style.use("seaborn-v0_8-darkgrid")
fig,ax=plt.subplots()

ax.scatter(x_values,y_values,s=10)

ax.plot(x_values,y_values,linewidth=1)
ax.set_title("Square Data",fontsize=24)
ax.set_xlabel("value",fontsize=18)
ax.set_ylabel("number values",fontsize=18)
ax.tick_params(labelsize=14)


#*Using the colormap 


ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# ax.scatter(x_values,y_values,cmap=plt.cm.Reds,s=10)

ax.axis([0, 1100, 0, 1_100_000])#*The axis() method requires four values: the mini-
#*mum and maximum values for the x-axis and the y-axis.
ax.ticklabel_format(style='plain')#*there are also other styles..

# plt.show()
plt.savefig('squareBox.png', bbox_inches='tight')



