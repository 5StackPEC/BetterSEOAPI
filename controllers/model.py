from fastapi import UploadFile
import os
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import tempfile


class Model:
    def __init__(self):
        self.image_path = f"{os.getcwd()}/uploads/default.png"
        self.model = self.get_saved_model()

    def get_saved_model(self, model_path=f"{os.getcwd()}/model/BetterSEOModel.h5"):
        return tf.keras.models.load_model(model_path)

    def save_image(self):
        self.image_path = f"{os.getcwd()}/uploads/{self.image.filename}"
        with open(self.image_path, "wb") as f:
            try:
                f.write(self.image.file.read())
                print(f"Image saved at {self.image_path}")
            except Exception as e:
                print(f"Failed while saving file: {self.image_path}")

    def remove_image(self):
        try:
            os.remove(self.image_path)
            print(f"Image removed ({self.image_path})")
        except Exception as e:
            print(f"Failed while removing file: {self.image_path}")

    async def get_preprocess_image(self, img_file_raw: UploadFile):

        try:
            contents = await img_file_raw.read()
            nparr = np.frombuffer(contents, np.uint8)

            processed_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            new_dims = (224, 224)
            processed_image = cv2.resize(
                processed_image, new_dims, interpolation=cv2.INTER_AREA
            )
            processed_image = processed_image / 255.0
            processed_image = np.expand_dims(processed_image, axis=0)
            # Preview the image in a window
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return processed_image
        except Exception as e:
            print(e)

    def predict(self, input_image):
        try:
            prediction: np.ndarray = self.model.predict(input_image)
            score = prediction.item()
            return score
        except Exception as e:
            print("Error while predicting!")
