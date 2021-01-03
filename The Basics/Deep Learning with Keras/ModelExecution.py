from keras.models import Sequential
from keras.layers import Dense

# Training
model = Sequential()
layer1 = Dense(200, activation='relu', input_dim=4)
model.add(layer1)
layer2 = Dense(200, activation='relu')
model.add(layer2)
layer3 = Dense(3, activation='softmax')
model.add(layer3)
model.compile('adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# predefined multiclass dataset
train_output = model.fit(data, labels,
                         batch_size=20, epochs=5)
print(train_output.history)
# 'loss': [1.0050578951835631, 0.7327303171157837, 0.561303706963857, 0.4560817003250122, 0.41256120602289836],
# 'acc': [0.5199999968210857, 0.6800000111262003, 0.7200000007947286, 0.7399999936421712, 0.9599999904632568]}

# Evaluation
# predefined eval dataset
print(model.evaluate(eval_data, eval_labels))
#  32/100 [========>.....................] - ETA: 0s
# 100/100 [==============================] - 0s 791us/step
# [0.33016082882881165, 0.87]

# Predictions
# 3 new data observations
print('{}'.format(repr(model.predict(new_data))))
# array([[9.7247946e-01, 2.5739742e-02, 1.7807921e-03],
#        [6.6281867e-04, 1.3427845e-01, 8.6505878e-01],
#        [2.8883541e-02, 7.6322287e-01, 2.0789358e-01]], dtype=float32)