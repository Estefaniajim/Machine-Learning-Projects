from keras.models import Sequential
from keras.layers import Dense

# Configuring for training
model = Sequential()
layer1 = Dense(5, activation='relu', input_dim=4)
model.add(layer1)
layer2 = Dense(1, activation='sigmoid')
model.add(layer2)
model.compile('adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
