import tensorflow as tf

# Placeholder for the model's input data
def init_inputs(input_size):
  inputs = tf.placeholder(tf.float32,shape=(None,input_size), name="inputs")
  return inputs

# Placeholders for the labels
def init_labels(output_size):
  labels = tf.placeholder(tf.int32, shape=(None, output_size), name="labels")
  return labels