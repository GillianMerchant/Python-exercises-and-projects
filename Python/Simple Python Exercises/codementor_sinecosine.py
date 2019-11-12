import numpy as np
import matplotlib.pyplot as plt
#An exercise from codementor
# This generates a sin v cosin curve using numpy and matplotlib libraries.
# The x axis must go from -360 to 360

# The numpy methods sin() and cosin() take radians and not degrees as arguments.
# In order to make the x axis show as degrees whilst the values come from radians it was necessary to convert to rads in the sin() and cosin() function


"""
import numpy
import matplotlib
generate the values of -360-360
convert to radians and calculate the sin and cosin of each value
plot them on a line graph
x axis shows degrees not radians

"""
#build set of variables for x with arange(start, stop, step)
x = np.arange(-360, 360, 10)

#convert x to radians to use in the sin and cos conversion functions
y = np.sin(np.radians(x))
z = np.cos(np.radians(x))

# now create and display the chart
# you can do the y and z plotting in one step but easier to set labels when  you do it in two stages. 
# plt.plot(x,y,x,z)
plt.plot(x,y, label = "sine")
plt.plot(x,z, label = "cosine")
plt.title("Gill's attempt at a sine / cosine curve")
plt.ylabel("value of sine and cosine")
plt.legend()
plt.show()

