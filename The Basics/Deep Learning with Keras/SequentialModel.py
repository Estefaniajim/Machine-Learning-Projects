from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten

model = Sequential() # ontainer of the neural network
layer1 = Dense(5, input_dim=4) #fully-connected layer in the neural network
model.add(layer1)
layer2 = Dense(3, activation='relu')
model.add(layer2)
# Initializing a Sequential model with two Dense layers.
layer1 = Dense(5, input_dim=4)
layer2 = Dense(3, activation='relu')
model = Sequential([layer1, layer2])