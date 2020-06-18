"""
Warning: This code is broken. Don't treat it as model code for your work.

This code generates random pixel art. The values are all integers drawn from a
random uniform distribution. The range of the random distribution increases as 
we go up in the image. We also will log how many times each integer is hit.  

# Topics we'll cover:
# - setting up debugging configuration in VSCode
# - pdb
# - post mortem debugging
# - breakpoints/conditional breakpoints
# - stepping through lines
# - debug console
# - How to use this when developing for large packages. 
"""

import numpy as np
import matplotlib.pylab as plt

# make a random image
np.random.seed(99999)

# for each row, we will draw numbers from increasingly large pools of random numbers
new_image = []

dim1 = 25
dim2 = 7

for i in range(dim1):
    # draw random integers between 0 and 10*(i+1), no repeats!
    this_row = []
    for j in range(dim2):
        new_number = np.random.randint(0, 10*(i+1))
        if new_number not in this_row:
            this_row.append(new_number)

    # add this row to the image we are creating
    new_image.append(this_row)

# now let's check how many of each number we generated
counts = {} # dictionary of counts per value
for i in range(dim1):
    for j in range(dim2):
        value = new_image[dim1, dim2]
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 0

print(counts)

# plot the resulting image. 
plt.figure()
plt.imshow(new_image, cmap="RdBu")
plt.gca().invert_yaxis()
plt.title("Art")
plt.show()