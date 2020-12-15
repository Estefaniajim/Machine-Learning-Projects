import tensorflow as tf

probs = tf.nn.sigmoid(logits)
rounded_probs = tf.round(probs)  # Round the probabilities to 0.0 or 1.0
predictions = tf.cast(rounded_probs, tf.int32)  # Match the type of the labels placeholder
is_correct = tf.equal(predictions, labels)  # Returns a tensor that has True at each position where our prediction
# matches the label and False elsewhere
is_correct_float = tf.cast(is_correct, tf.float32)  # Converts True to 1.0 and False to 0.0
accuracy = tf.reduce_mean(is_correct_float)  # Accuracy of our predictions