import numpy as np
import tensorflow as tf
import cv2

class Classification:
    def __init__(self) -> None:
        self.efficient_net =  tf.keras.applications.efficientnet_v2.EfficientNetV2B0()
    
    def predict(self, image):
        image = np.asarray(image)
        image = cv2.resize(image, (224, 224))
        image =  tf.keras.applications.efficientnet_v2.preprocess_input(np.expand_dims(image, axis=0))
        prediction = self.efficient_net.predict(image)
        decode_prediction=tf.keras.applications.efficientnet_v2.decode_predictions(prediction)
        return decode_prediction[0][0][1]

if __name__ == "__main__":
    img = cv2.imread('cycle.jpg')
    clf = Classification()
    print(clf.predict(img))