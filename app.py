# app.py

import streamlit as st
import json
import os
from resume_parser.extract_text import extract_text
from resume_parser.extract_entities import extract_entities
from resume_parser.extract_expereince import extract_experience


st.set_page_config(page_title="AI Resume Parser", layout="centered")

st.title("📄 AI-Powered Resume Parser")
st.write("Upload a resume (PDF, DOCX, TXT) and get structured information using NLP.")

uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_path = os.path.join("resumes", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Extracting text..."):
        raw_text = extract_text(file_path)

    with st.spinner("Parsing entities..."):
        parsed_data = extract_entities(raw_text)
        parsed_data["experience"] = extract_experience(raw_text)

    st.subheader("📊 Extracted Information")
    st.json(parsed_data)

    # Save to file
    output_path = os.path.join("output_json", uploaded_file.name.split('.')[0] + ".json")
    with open(output_path, "w") as out_file:
        json.dump(parsed_data, out_file, indent=4)

    st.success("✅ Resume parsed successfully!")
    with open(output_path, "rb") as f:
        st.download_button("⬇️ Download JSON", f, file_name=os.path.basename(output_path))

