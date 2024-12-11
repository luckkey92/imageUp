import streamlit as st
from PIL import Image
import io

def upscale_image(image):
    """
    Upscale the image to 2x its original size.
    """
    width, height = image.size
    return image.resize((width * 2, height * 2), Image.Resampling.LANCZOS)

st.title("Image Upscaler App")
st.write("Upload an image to upscale it to 2x its original size.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    st.write("Original Image:")
    st.image(image, caption="Original Image", use_column_width=True)

    # Upscale the image
    upscaled_image = upscale_image(image)
    st.write("Upscaled Image:")
    st.image(upscaled_image, caption="Upscaled Image", use_column_width=True)

    # Provide download option
    buf = io.BytesIO()
    upscaled_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download Upscaled Image",
        data=byte_im,
        file_name="upscaled_image.png",
        mime="image/png",
    )
