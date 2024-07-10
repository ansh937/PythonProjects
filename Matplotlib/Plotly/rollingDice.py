from random import randint
'''In this project, we will analyze the results of rolling dice. When you roll
one regular, six-sided die, you have an equal chance of rolling any of the
numbers from 1 through 6. However, when you use two dice, you are more
likely to roll certain numbers than others. We will try to determine which
numbers are most likely to occur by generating a dataset that represents
rolling dice. Then we will plot the results of a large number of rolls to deter-
mine which results are more likely than others.
This work helps model games involving dice, but the core ideas also apply
to games that involve chance of any kind, such as card games. It also relates to
many real-world situations where randomness plays a significant factor.'''

class Die:
  
  def __init__(self,num_sides=6) -> None: #hy ako num_sides=class attribute vayo 
    """Assume a six-sided die."""
    self.num_sides=num_sides#Hya ko self.num_sides vanako object attribute vayo 
  
  def roll(self):
      #return a random value between 1 and number of sides
      return randint(1,self.num_sides)
    
    