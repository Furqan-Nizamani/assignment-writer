import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import textwrap

st.set_page_config(page_title='Handwriting creator')

st.title('Handwriting Creator (Offline)')

text = st.text_area('Enter your Assignment text here:')

if st.button('Convert to Handwriting'):
    font_path = "C:/Users/Furqan Ahmed/Desktop/python-50 projects/handwriter/Caveat/Caveat-VariableFont_wght.ttf"
    font_size = 24
    image_width = 800
    margin = 50
    line_height = 40

    lines = textwrap.wrap(text, width=60)

    image_height = margin * 2 + line_height * len(lines)

    img = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    y = margin
    for line in lines:
        draw.text((margin, y), line, font=font, fill="black")
        y += line_height

    st.image(img, caption='Your handwritten text')

    pdf_bytes = io.BytesIO()
    img.save(pdf_bytes, format='PDF')
    pdf_bytes.seek(0)

    st.download_button(
        label='Download as PDF',
        data=pdf_bytes,
        file_name='handwriting.pdf',
        mime='application/pdf'
    )
