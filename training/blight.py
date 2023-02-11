
import streamlit as st
import tensorflow as tf

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('blight.sav')
    return model

model = load_model()
st.write(
    """
    #Plant Disease Classification
    """
)

file = st.file_uploader("Upload a file", type=['jpg','png'])

import cv2
from PIL import Image, ImageOps

import numpy as np

def import_and_predict(image_data,model):
    size = (180,180)
    image = ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img = np.asarray()
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)

    return prediction

if file is None:
    st.text("Please upload an image file")

else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image,model)
    class_names = ["Early_Blight","Late_Blight","Healthy"]
    string = "This disease is most likely "+class_names[np.argmax(prediction)]
    st.success(string)


