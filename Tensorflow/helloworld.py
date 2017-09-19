# Python 3
# Tensorflow Test model fit
import numpy as np
import tensorflow as tf

# Parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)

# IO
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
linear_model = W * x + b

# Model fit SSE
loss = tf.reduce_sum(tf.square(linear_model - y))

# Optimize
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# Training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train, {x:x_train, y:y_train})

# Evaluate
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
print("W: %s b: %s loss: %s" %(curr_W, curr_b, curr_loss))
