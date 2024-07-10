from rollingDice import Die
import plotly.express as px
die=Die()

results=[]
for roll_num in range(1000):
  result=die.roll()
  results.append(result)
#print(results)
  
  #To analyze the rolls, we create the empty
# list frequencies to store the number of times each value is rolled. 
frequencies=[]
poss_results=range(1,die.num_sides+1)
for value in  poss_results:# We loop through the pos-sible values, count how many times each number appears in results
  frequency=results.count(value)#value vanako 1 bata 6 samma kati patak number aahuxa vanera rakheko 
  frequencies.append(frequency)
print(frequencies)  

# title = "Results of Rolling One D6 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.show()

fig=px.bar(x=poss_results,y=frequencies,title="Result of rolling one Dinc 1000 times",labels={'x':'result','y':'feequency of result'})
#px.scatter also can be used there are many ..px.pie
fig.show()

