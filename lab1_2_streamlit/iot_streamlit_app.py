import streamlit as st
from PIL import Image
# Trags this! LED m0 ph0ng
if "led_on" not in st.session_state:
    st.session_state.led_on = False
# XU ly sy kiện nút truộc khi render
col1, col2 = st.columns(2)
with col1:
    if st.button("BẤT LED"):

       st.session_state.led_on = True
with col2:
    if st.button("TÁT LED"):
        st.session_state.led_on = False

# Sau khi cặp nhật trạng thái + render ảnh
st.title("Điều khiển LED mô phỏng bằng Streamlit")

if st.session_state.led_on:
    image_file = "images/led_on.png"
else:
    image_file = "images/led_off.png"

image = Image.open(image_file)
st.image(image, caption="LED is ON"
    if st.session_state.led_on
        else "LED is OFF", width=200)