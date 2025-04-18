import streamlit as st
import tempfile
import os
from metadata import extract_metadata
from analysis import analyze_frame

st.title("🎬 Footage Analyzer")

uploaded_file = st.file_uploader("Upload your footage", type=["mp4", "mov", "avi"])

if uploaded_file:
    # Correct handling of temp file with tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_filename = tmp_file.name

    try:
        metadata = extract_metadata(temp_filename)
        analysis = analyze_frame(temp_filename)

        st.subheader("📌 Metadata")
        st.json(metadata)

        st.subheader("📷 Footage Analysis")
        st.json(analysis)

    finally:
        os.remove(temp_filename)
