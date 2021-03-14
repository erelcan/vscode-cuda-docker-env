import tensorflow as tf

print(tf.__version__)

a = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.print(a)

tf.test.gpu_device_name()
print(tf.config.experimental.list_physical_devices('GPU'))