#!/usr/bin/python
import tensorflow as tf

# creates nodes in a graph
# "Construction phase"
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)
print(result)

# defines our session and launches graph
sess = tf.Session()

# runs result
print(sess.run(result))

# close the session
sess.close()

# Utilize python's with statement
with tf.Session() as sess:
	output = sess.run(result)
	print(output)

# tf on Multiple Devices and even multiple distributed machines
print("Multiple Devices")
with tf.Session() as sess:
	with tf.device("/gpu:1"):
		matrix1 = tf.constant([[3., 3.]])
		matrix2 = tf.constant([[2.],[2.]])
		product = tf.matmul(matrix1, matrix2)

print product
#	op = sess.run(product)
#	print(op)



