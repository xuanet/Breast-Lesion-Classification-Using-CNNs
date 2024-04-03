import tensorflow as tf
print(tf.config.list_physical_devices())
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# tf.debugging.set_log_device_placement(True)


# from tensorflow.python.client import device_lib 
# print(device_lib.list_local_devices())