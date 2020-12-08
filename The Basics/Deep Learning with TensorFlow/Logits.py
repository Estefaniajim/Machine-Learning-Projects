import tensorflow as tf

# A single layer perceptron, whose output is logits
def model_layers(inputs, output_size):
  logits = tf.layers.dense(inputs,output_size, name = "logits")
  return logits