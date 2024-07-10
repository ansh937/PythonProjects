'''we will create a RandomWalk class, which will make ran-
dom decisions about which direction the walk should take. The class needs
three attributes: one variable to track the number of points in the walk, and
two lists to store the x- and y-coordinates of each point in the walk.
Well only need two methods for the RandomWalk class: the __init__()
method and fill_walk(), which will calculate the points in the walk. Lets
start with the __init__() method:'''

from random import choice

class RandomWalk:
  # """A class to generate random walks."""
  
    def __init__(self,num_points=5000) -> None:
      self.num_points=num_points
      
      # All walks start at (0, 0).
      self.x_values=[0]
      self.y_values=[0]
    

    
    
#     '''To make random decisions, we will store possible moves in a list and use
# the choice() function (from the random module) to decide which move to
# make each time a step is taken . We set the default number of points in
# a walk to 5000, which is large enough to generate some interesting patterns
# but small enough to generate walks quickly . Then we make two lists to
# hold the x- and y-values, and we start each walk at the point (0, 0) .'''

# '''Well use the fill_walk() method to determine the full sequence of points
# in the walk. Add this method to random_walk.py:'''



# '''We first set up a loop that runs until the walk is filled with the correct
# number of points . The main part of fill_walk() tells Python how to simu-
# late four random decisions: Will the walk go right or left? How far will it go
# in that direction? Will it go up or down? How far will it go in that direction?
# We use choice([1, -1]) to choose a value for x_direction, which returns
# either 1 for movement to the right or −1 for movement to the left . Next,
# choice([0, 1, 2, 3, 4]) randomly selects a distance to move in that direc-
# tion. We assign this value to x_distance. The inclusion of a 0 allows for the
# possibility of steps that have movement along only one axis.
# We determine the length of each step in the x- and y-directions by mul-
# tiplying the direction of movement by the distance chosen . A positive
# result for x_step means move to the right, a negative result means move
# to the left, and 0 means move vertically. A positive result for y_step means
# move up, negative means move down, and 0 means move horizontally. If the
# values of both x_step and y_step are 0, the walk doesn’t go anywhere; when
# this happens, we continue the loop .
# To get the next x-value for the walk, we add the value in x_step to the
# last value stored in x_values and do the same for the y-values. When we
# have the new point’s coordinates, we append them to x_values and y_values.'''
    def fill_walk(self): 
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
        # Decide which direction to go, and how far to go.
          x_direction = choice([1, -1])#We use choice([1, -1]) to choose a value for x_direction, which returns
# either 1 for movement to the right or −1 for movement to the left 

          x_distance = choice([0, 1, 2, 3, 4])# Next,
# choice([0, 1, 2, 3, 4]) randomly selects a distance to move in that direc-
# tion. We assign this value to x_distance. 
          x_step = x_direction * x_distance# We determine the length of each step in the x- and y-directions by mul-
# tiplying the direction of movement by the distance chosen 
          y_direction = choice([1, -1])
          y_distance = choice([0, 1, 2, 3, 4])
          y_step = y_direction * y_distance
          # Reject moves that go nowhere.
          if x_step == 0 and y_step == 0:
            continue
        
          # Calculate the new position.
          #To get the next x-value for the walk, we add the value in x_step to the
# last value stored in x_values and do the same for the y-values.
          x = self.x_values[-1] + x_step
          y = self.y_values[-1] + y_step
          self.x_values.append(x)
          self.y_values.append(y)

