import matplotlib.pyplot as plt

x_values=range(1,6)
y_values=[x**3 for x in x_values]

plt.style.use("seaborn-v0_8-darkgrid")
fig,ax=plt.subplots()
ax.plot(x_values,y_values,linewidth=3)
ax.set_title("cubic numbers",fontsize=18)
ax.set_xlabel("values")
ax.set_ylabel("cubic points")
ax.scatter(x_values,y_values,color="red",s=100)
plt.show()