import matplotlib.pyplot as f

f.style.use('seaborn-v0_8-darkgrid')

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

fig,ax=f.subplots()
ax.scatter(2,4,s=200,color='green')#* dort li bigger size dini 2 ko char only one point

#*If you want a series of point in scatter the use 
ax.scatter(input_values,squares,color=(0, 0.8, 0),s=100)#you can also costomize color




ax.plot(input_values,squares,linewidth=3)
ax.set_title("Square Data",fontsize=24)
ax.set_xlabel("value",fontsize=18)
ax.set_ylabel("number values",fontsize=18)
ax.tick_params(labelsize=14)
f.show()