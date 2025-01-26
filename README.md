# **Java House Recruitment Portal**

Welcome to the Java House Recruitment Portal! This application is designed to streamline the recruitment process by collecting applicant information, analyzing CVs, and generating compatibility reports using advanced AI.

---

## **Features**

### 1. **User-Friendly Recruitment Form**
- Collects applicant details, including:
  - Name, age, gender.
  - Role of interest.
  - Outreach information (e.g., how they heard about the role).
  - Expected salary and a brief self-description.

### 2. **CV Upload and Summarization**
- Allows applicants to upload their CV in **PDF format**.
- Extracts and summarizes the CV content for efficient analysis.

### 3. **AI-Powered Compatibility Reports**
- Integrates with **OpenAI GPT** to analyze:
  - Applicant data (e.g., skills, experience).
  - Summarized CV content.
- Generates a detailed compatibility summary highlighting:
  - Applicant strengths.
  - Potential weaknesses.
  - Suitability for the applied role.

### 4. **Enhanced Error Handling**
- Warns users about missing or invalid inputs (e.g., no CV uploaded).
- Guides users through submission errors to ensure smooth application processing.

---

## **Technology Stack**

### **Frontend**:
- [Streamlit](https://streamlit.io/): Used to build a dynamic and interactive user interface.

### **Backend**:
- [OpenAI GPT](https://platform.openai.com/docs/): For analyzing applicant data and generating compatibility summaries.

### **Utilities**:
- [PyPDF2](https://pypi.org/project/PyPDF2/): For extracting text from PDF CVs.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For securely managing API keys via environment variables.

---

## **Installation and Setup**

### **Prerequisites**
1. Python 3.8 or later.
2. A valid OpenAI API key.

### **Steps to Run Locally**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

6. Open your browser and navigate to the displayed URL (usually `http://localhost:8501`).

---

## **Usage**

1. **Fill Out the Form**:
   - Enter your personal information, select the desired role, and upload your CV.
2. **Submit the Form**:
   - Once submitted, the app generates a **Compatibility Summary Report**.
3. **Review the Report**:
   - The report includes insights into your suitability for the role, based on the provided information and CV.

---

## **Development Workflow**

### **Branching Strategy**
- All new features are implemented in separate branches.
- Changes are merged into the main branch via pull requests.

### **Contributing**
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add: Description of your feature"
   git push origin feature/your-feature-name
   ```
4. Create a pull request.

---

## **Acknowledgments**
- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework.
- [OpenAI](https://platform.openai.com/) for their cutting-edge AI capabilities.
- The recruitment team at Java House for inspiring this project.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

**Feel free to contribute to the project and make the recruitment process smarter and more efficient!**
```