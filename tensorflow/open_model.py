import tensorflow as tf


def open_model():
    # Recreate the exact same model, including its weights and the optimizer
    new_model = tf.keras.models.load_model('s3://druid-index-eu-west-1/mlflow/4/09c9ce210fec472eb635ee22ea360387/artifacts/model')

    # Show the model architecture
    print(new_model.summary())

if __name__ == '__main__':
    open_model()
