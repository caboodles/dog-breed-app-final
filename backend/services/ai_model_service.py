import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.applications.resnet_v2 import preprocess_input
from PIL import Image
from sklearn.preprocessing import LabelEncoder
import pandas as pd

print(tf.__version__)

num_breeds = 60

# LabelEncoder 로드
df_labels = pd.read_csv('./backend/services/labels.csv')
encoder = LabelEncoder()
encoder.fit(df_labels["breed"].values)
print(df_labels["breed"].values)

# 모델 로드
model = load_model('model.h5')

def predict_breed(image_path):
    # 이미지 로드 및 전처리
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img_array = np.array(img).astype(np.float32)
    img_array = preprocess_input(np.expand_dims(img_array, axis=0))

    # 예측
    pred_label = model.predict(img_array)
    pred_label = np.argmax(pred_label, axis=1)
    pred_breed = encoder.inverse_transform(pred_label)

    # 예측 결과 리턴
    return pred_breed[0]
