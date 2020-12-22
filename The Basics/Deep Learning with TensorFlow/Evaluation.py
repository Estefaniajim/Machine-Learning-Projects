import tensorflow as tf

# Evaluation of the accuracy in the pretrained model on the test data and labels
# test_data, test_labels, inputs, labels, accuracy
# are all predefined in the backend
feed_dict = {inputs:test_data, labels:test_labels}
eval_acc = sess.run(accuracy, feed_dict=feed_dict)