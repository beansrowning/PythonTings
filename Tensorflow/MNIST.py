#! Python 3.6
# softmax MNIST Classifier

# Load MNIST
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)

# Import tensorflow
import tensorflow as tf
sess = tf.InteractiveSession()

# Placeholders for images to be analyzed
x = tf.placeholder(tf.float32, shape = [None, 784])
y_ = tf.placeholder(tf.float32, shape = [None, 10])

# Weight and bias variables
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

sess.run(tf.global_variables_initializer())

# Multiply vectorized images by weight matrix and add bias
y = tf.matmul(x, W) + b

# Calculate loss value to minimize with softmax
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = y))

# Optimize via gradient descent
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

for _ in range(1000):
    # Load 100 examples to train
    batch = mnist.train.next_batch(100)
    # Run gradient descent, minimizing for cross entropy
    train_step.run(feed_dict = {x: batch[0], y_: batch[1]})

# How did we do?
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# Cast boolean to FP
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Report
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
