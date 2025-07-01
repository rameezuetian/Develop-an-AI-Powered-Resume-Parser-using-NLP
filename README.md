# 🤖 AI-Powered Resume Parser using NLP

This project is a resume parser built with Python and NLP that extracts structured information like name, email, phone number, skills, and work experience from unstructured resumes (PDF, DOCX, or TXT). It uses SpaCy for Named Entity Recognition (NER), regex for pattern matching, and Streamlit for an interactive web interface.

---

## 🚀 Features

- ✅ Supports **PDF, DOCX, TXT** resume formats
- ✅ Extracts:
  - Name
  - Email
  - Phone number
  - Skills (from a predefined list)
  - Job Title, Company, and Duration
- ✅ Outputs structured JSON
- ✅ Download parsed data
- ✅ Interactive **Streamlit App**

---

## 🧠 Technologies Used

- Python
- SpaCy (NER)
- Regex
- PDFMiner / python-docx
- Streamlit (Web UI)

---

## 📂 Folder Structure

```
resume\_parser/
├── app.py                        # Streamlit app entry point
├── output\_json/                 # Parsed JSON output files
├── resumes/                     # Input resumes
├── resume\_parser\_core/          # Core logic
│   ├── extract\_text.py          # File text extractor
│   ├── extract\_entities.py      # Name, email, phone, skills
│   └── extract\_experience.py    # Experience parsing logic
└── evaluation/                  # Accuracy evaluation scripts

```

---

## 💻 Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/resume-parser-nlp.git
cd resume-parser-nlp
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

4. **Upload your resume** and get structured results in JSON.

---

## 📊 Sample JSON Output

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1-234-567-8901",
  "skills": ["Python", "Machine Learning", "AWS"],
  "experience": [
    {
      "title": "Data Scientist",
      "company": "TechCorp",
      "years": 2
    }
  ]
}
```

---

## 📈 Learning Outcomes

This project helped us apply real-world NLP to unstructured document parsing. We gained hands-on experience with SpaCy, regular expressions, JSON structuring, and frontend integration using Streamlit—making it a great end-to-end practical application.

---

## 📌 Future Improvements

* Train a custom SpaCy NER model for higher accuracy
* Handle multiple resumes at once
* Integrate resume preview and profile matching

---

## 🤝 Contributing

Feel free to fork this repo, create issues, or submit pull requests. Contributions are welcome!

---

## 📜 License

MIT License. See `LICENSE` for more details.

```
