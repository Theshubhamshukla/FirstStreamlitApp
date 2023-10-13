import streamlit as st
from PIL import Image
import pandas as pd


st.title('File Uploading')


# 1. image
st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload Image', type = ['png', 'jpeg', 'jpg'])
if img_file is not None:
    #st.write(type(img_file))  getting error for now

    file_details = {'file_name' : img_file.name,
                    'file_type' : img_file.type,
                    'file_size' : img_file.size
                    }
    st.write(file_details)

    st.image(Image.open(img_file))

# 2. Audio
st.subheader('1. Uploading an Audio')
audio_file = st.file_uploader('Upload Audio', type = ['mp3', 'wav'])
if audio_file is not None:
    #st.write(type(img_file))  getting error for now

    file_details = {'file_name' : audio_file.name,
                    'file_type' : audio_file.type,
                    'file_size' : audio_file.size
                    }
    st.write(file_details)
    st.audio(audio_file)


# 3. Video
st.subheader('1. Uploading an video')
video_file = st.file_uploader('Upload video', type = ['mp4',   'mov'])
if video_file is not None:
    #st.write(type(img_file))  getting error for now

    file_details = {'file_name' : video_file.name,
                    'file_type' : video_file.type,
                    'file_size' : video_file.size
                    }
    st.write(file_details)
    st.video(video_file)


# 4. CSV
