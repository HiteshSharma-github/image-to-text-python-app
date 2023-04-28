import easyocr as ocr
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# Title
st.title("Netspire OCR")

# Subtitle
st.markdown("## Extract Text from Images")

st.markdown("")

# Image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

@st.cache
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader

reader = load_model()  # Load model

if image is not None:

    input_image = Image.open(image)  # Read image

    # Perform image processing
    input_image = input_image.convert('L')  # Convert to grayscale
    input_image = ImageEnhance.Contrast(input_image).enhance(2)  # Increase contrast
    input_image = input_image.filter(ImageFilter.MedianFilter())  # Apply median filter
    input_image = input_image.filter(ImageFilter.SHARPEN)  # Sharpen image
    input_image = input_image.convert('RGB')  # Convert back to RGB

    st.image(input_image)  # Display image

    with st.spinner("🤖 AI is at Work! "):
        result = reader.readtext(np.array(input_image))

        result_text = []  # Empty list for results

        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.balloons()
else:
    st.write("Upload an Image")
    
url = "https://netspires.netlify.app"
st.write("🔙 [Go Back](%s)" % url)
st.caption("Made with ❤️ by Hitesh SHarma")
