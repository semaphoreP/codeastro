## This code is broken. Don't treat it as model code for your work ##

import numpy as np
import matplotlib.pylab as plt

# make a random image
np.random.seed(99999)

# for each row, we will draw numbers from increasinly large pools of random numbers
new_image = []

dim1 = 150
dim2 = 75

for i in range(dim1):
    # draw random integers between 0 and 10*(i+1), no repeats!
    this_row = []
    for j in range(dim2):
        new_number = np.random.randint(0, 10*(i+1))
        if new_number not in this_row:
            this_row.append(new_number)

    # add this row to the image we are creating
    new_image.append(this_row)


# now let's check we did that right. Test that each value only occurs once in the array
for i in range(dim1):
    for j in range(dim2):
        value = new_image[dim1, dim2]
        all_matches = np.where(new_image == value)[0]
        assert np.size(all_matches) == 1


plt.figure()
plt.imshow(new_image, cmap="RdBu")
plt.gca().invert_yaxis()
plt.show()