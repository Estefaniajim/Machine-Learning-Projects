import tensorflow as tf

labels_float = tf.cast(labels, tf.float32)
cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=labels_float, logits=logits)  # Calculate the
# sigmoid-based cross entropy
loss = tf.reduce_mean(cross_entropy)  # Overall mean of the cross entropy as loss
adam = tf.train.AdamOptimizer()  # Adam optimizer object
train_op = adam.minimize(loss)  # Training operation