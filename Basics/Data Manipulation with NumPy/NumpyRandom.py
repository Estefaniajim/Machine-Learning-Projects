import numpy as np

# Random integers
num1 = np.random.randint(5)  # 1
num2 = np.random.randint(5, high=6)  # [0, n) --> [0, 6) --> 5
random_arr = np.random.randint(-3, high=14,
                               size=(2, 2))  # [[ 9, -2], [-3, -1]]

# Utility functions
# A random seed (or seed state, or just seed) is a number
# (or vector) used to initialize a pseudorandom number generator.
np.random.seed(1)
np.random.randint(10)  # 5
random_arr2 = np.random.randint(3, high=100,
                                size=(2, 2))  # [[15, 75], [12, 78]]
np.random.seed(2)  # New seed
np.random.randint(10)  # 8
random_arr3 = np.random.randint(3, high=100,
                                size=(2, 2))  # [[18, 75], [25, 46]]
np.random.seed(1)  # Original seed
np.random.randint(10)  # 5
random_arr4 = np.random.randint(3, high=100,
                                size=(2, 2))  # [[15, 75], [12, 78]]
vec = np.array([1, 2, 3, 4, 5])
np.random.shuffle(vec)  # [5, 2, 4, 1, 3]
np.random.shuffle(vec)  # [2, 4, 5, 1, 3]
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
np.random.shuffle(matrix)  # [[4, 5, 6], [7, 8, 9], [1, 2, 3]]

# Distributions
# The continuous uniform distribution or rectangular distribution
# is a family of symmetric probability distributions
# Draw pseudo-random real numbers from a uniform distribution
np.random.uniform()  # [0.0, 1.0) --> 0.5165912060005503
np.random.uniform(low=-1.5, high=2.2)  # [-1.5, 2.2) --> -0.2714734800878733
np.random.uniform(size=3)  # [0.0, 1.0) --> [0.04950374, 0.2074792 , 0.50690197]
np.random.uniform(low=-3.4, high=5.9,
                  size=(2, 2))  # [3.4, 5.9) --> [[ 5.61823728, 3.05439943], [-2.25858195, -1.07944141]]
# A normal (or Gaussian or Gauss or Laplace–Gauss)
# distribution is a type of continuous probability
# distribution for a real-valued random variable.
np.random.normal()  # -0.25430341887781266
np.random.normal(loc=1.5, scale=3.5)  # 2.912483022156186
np.random.normal(loc=-2.4, scale=4.0,
                 size=(2, 2))  # [[-1.21742131, -0.00294223], [ 1.60328904, -0.03785279]]
# loc and scale keyword arguments represent the mean and standard deviation

# Custom sampling
colors = ['red', 'blue', 'green']
np.random.choice(colors)  # green
np.random.choice(colors, size=2)  # ['red', 'blue']
np.random.choice(colors, size=(2, 2),
                 p=[0.8, 0.19, 0.01])  # [['blue', 'red'], ['blue', 'red']]
# p keyword argument denotes the probabilities
# given to each element in the input distribution.
# Note that the list of probabilities for p must sum to 1.