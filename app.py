import streamlit as st
import os
from metadata import extract_metadata
from analysis import analyze_frame

st.title("🎬 Footage Analyzer")

uploaded_file = st.file_uploader("Upload your footage", type=["mp4", "mov", "avi"])

if uploaded_file:
    # Temporary save the uploaded file
    temp_file = "temp_uploaded_video.mp4"
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract metadata and analyze footage
    metadata = extract_metadata(temp_file)
    analysis = analyze_frame(temp_file)

    # Remove temp file immediately after use
    os.remove(temp_file)

    # Display results
    st.subheader("📌 Metadata")
    st.json(metadata)

    st.subheader("📷 Footage Analysis")
    st.json(analysis)
