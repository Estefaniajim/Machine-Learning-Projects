from sklearn.model_selection import train_test_split
import numpy as np

# The default size of the testing set is 25% of the original dataset

data = np.array([
    [10.2, 0.5],
    [8.7, 0.9],
    [9.3, 0.8],
    [10.1, 0.4],
    [9.5, 0.77],
    [9.1, 0.68],
    [7.7, 0.9],
    [8.3, 0.8]])
labels = np.array(
    [1.4, 1.2, 1.6, 1.5, 1.6, 1.3, 1.1, 1.2])

split_dataset = train_test_split(data, labels)
# [array([[ 9.5 ,  0.77],
#       [10.2 ,  0.5 ],
#       [ 8.3 ,  0.8 ],
#       [ 8.7 ,  0.9 ],
#       [ 7.7 ,  0.9 ],
#       [ 9.3 ,  0.8 ]]), array([[10.1 ,  0.4 ],
#       [ 9.1 ,  0.68]]), array([1.6, 1.4, 1.2, 1.2, 1.1, 1.6]), array([1.5, 1.3])]

train_data = split_dataset[0]
# array([[10.1 ,  0.4 ],
#       [ 8.3 ,  0.8 ],
#       [ 9.5 ,  0.77],
#       [ 9.3 ,  0.8 ],
#       [ 7.7 ,  0.9 ],
#       [10.2 ,  0.5 ]])

test_data = split_dataset[1]
# array([[8.7 , 0.9 ],
#       [9.1 , 0.68]])

train_labels = split_dataset[2]
# array([1.5, 1.2, 1.6, 1.6, 1.1, 1.4])

test_labels = split_dataset[3]
# array([1.2, 1.3])

# Manually specify the proportion of the original dataset that will go into the testing set

split_dataset = train_test_split(data, labels,
                                 test_size=0.375)
# [array([[ 7.7 ,  0.9 ],
#       [10.1 ,  0.4 ],
#       [ 9.1 ,  0.68],
#       [ 8.7 ,  0.9 ],
#       [ 8.3 ,  0.8 ]]), array([[ 9.3 ,  0.8 ],
#       [ 9.5 ,  0.77],
#       [10.2 ,  0.5 ]]), array([1.1, 1.5, 1.3, 1.2, 1.2]), array([1.6, 1.6, 1.4])]

train_data = split_dataset[0]
# array([[ 7.7 ,  0.9 ],
#       [10.1 ,  0.4 ],
#       [ 9.1 ,  0.68],
#       [ 8.7 ,  0.9 ],
#       [ 8.3 ,  0.8 ]])

test_data = split_dataset[1]
# array([[ 9.3 ,  0.8 ],
#       [ 9.5 ,  0.77],
#       [10.2 ,  0.5 ]])

train_labels = split_dataset[2]
# array([1.1, 1.5, 1.3, 1.2, 1.2])

test_labels = split_dataset[3]


# array([1.6, 1.6, 1.4])

# Example
# The function will split the input dataset into training and
# testing sets, and then group the data and labels based on type of set.
def dataset_splitter(data, labels, test_size=0.25):
    split_dataset = train_test_split(data, labels, test_size=test_size)
    train_set = (split_dataset[0], split_dataset[2])
    test_set = (split_dataset[1], split_dataset[3])
    return train_set, test_set
