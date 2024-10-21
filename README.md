# 📝 MCQ Generator : https://mcqgenerator-dilesh.streamlit.app/


Welcome to the MCQ Generator! This web-based application helps you generate multiple choice questions (MCQs) from uploaded PDFs, text files, or manually provided text. Built using Streamlit and Python, the app allows users to specify the number of MCQs, subject, and complexity level to generate tailored questions.

## <b>Features</b>
- **File Upload**: Upload a PDF or text file to generate questions from the content.
- **Manual Text Input**: Provide your own text directly within the app.
- **MCQ Generation**: Specify the number of MCQs to generate.
- **Subject Specification**: Choose the subject for the generated questions.
- **Complexity Levels**: Select from Simple, Moderate, or Complex question types.
- **Real-time Output**: View the generated MCQs in a table format with an easy-to-read structure.
- **Error Handling**: Friendly notifications in case of errors or invalid inputs.

## <b>Technologies Used</b>
- **Python**: Backend logic for processing files and generating MCQs.
- **Streamlit**: Web application framework for building interactive user interfaces.
- **Langchain**: For managing prompts and model chaining.
- **Mistral AI**: Used for generating MCQs with natural language processing capabilities.
- **Pandas**: Data handling and displaying generated MCQs in a table format.
- **dotenv**: To manage environment variables securely.

## <b>Setup and Installation</b>
#### Prerequisites
- Python 3.10 or higher
- Virtual environment (recommended)
#### Installation Steps
<b>1. **Clone the Repository**:</b>
   ```bash
   git clone https://github.com/your-username/mcq-generator.git
   cd mcq-generator


<b>2. Create and Activate Virtual Environment:</b>
```bash
   python -m venv venv
   venv\Scripts\activate

<b>3. Install Required Packages:</b>
```bash
   pip install -r requirements.txt

<b>4. Set Up Environment Variables:</b> 
- Create a .env file in the root directory with your Mistral AI API key:
- MISTRAL_API_KEY=your-api-key-here
- Get your API key from Mistral AI.

<b>5. Run the Application:</b>
```bash
   streamlit run streamlit_app.py
This will start the Streamlit server and open the app in your web browser.

<b>Usage</b>
- Open the application in your browser.
- Upload a PDF or text file, or manually input text in the provided input box.
- Specify the number of MCQs, subject, and complexity level.
-Click "Generate MCQs" and view the generated questions in a table.
- Optionally, review the generated questions in the provided review section.

<b>Files and Directories</b>
- src/generate_mcqs/mcqs_generator.py: Core logic for generating MCQs.
- src/generate_mcqs/utils.py: Utility functions like reading files.
- src/generate_mcqs/logger.py: Logging module for error handling.
- streamlit_app.py: Main Streamlit application file.
- requirements.txt: List of Python dependencies.
- .env: Environment variables file (not included in the repository).

<b>Contributing</b>
Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

<b>Contact</b>
For any questions or feedback, feel free to reach out at Your Name via <a href="2dileshbisen@gmail.com">2dileshbisen@gmail.com</a>.
