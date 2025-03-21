import tensorflow as tf

# List all physical devices
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"Num GPUs Available: {len(gpus)}")
    for gpu in gpus:
        print("GPU Details:", gpu)
else:
    print("No GPU detected. TensorFlow is running on CPU.")
