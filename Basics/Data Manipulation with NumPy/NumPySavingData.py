import numpy as np

# Saving
arr = np.array([1, 2, 3])  # Saves to 'arr.npy'
np.save('arr.npy', arr)  # Also saves to 'arr.npy'
np.save('arr', arr)  # overwrite the previous file

# Loading
arr = np.array([1, 2, 3])
np.save('arr.npy', arr)
load_arr = np.load('arr.npy')  # [1, 2, 3]

# Examples
# The function will save some randomly generated 2-D points in a file.
def save_points(save_file):
  points = np.random.uniform(
    low=-2.5, high=2.5, size=(100,2))
  np.save(save_file,points)