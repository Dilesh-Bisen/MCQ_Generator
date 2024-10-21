import os
import json
import pandas as pd
import traceback
import PyPDF2
from src.generate_mcqs.logger import logging


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text

        except Exception as e:
            raise Exception("Error reading the PDF file")

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception("Unsupported file format. Only PDF and text files are allowed.")


def get_table_data(quiz_str):
    try:
        quiz_str = quiz_str.replace('```', '').strip()  # Removing any Markdown artifacts.
        quiz_str = quiz_str.lstrip("json\n").strip()  # Cleaning up the string.
        
        # Check if quiz_str is empty or None
        if not quiz_str:
            raise ValueError("The quiz string is empty or not in a valid format.")
        
        # Attempt to load quiz_str as JSON
        quiz_dict = json.loads(quiz_str)
        
        # Check if the required structure exists
        if "quizzes" not in quiz_dict:
            raise ValueError("The JSON structure is not correct. 'quizzes' key is missing.")
        
        quiz_data = []
        for value in quiz_dict["quizzes"]:
            mcq = value.get("question", "No question found")
            options = " | ".join(value.get("options", []))
            correct = value.get("correct_answer", "No correct answer found")

            quiz_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_data
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error: {e}")
        st.error(f"Error decoding JSON: {e}. Please check the input format.")
        return False
    except Exception as e:
        logging.error(f"Error processing table data: {e}")
        st.error(f"Error processing quiz data: {e}")
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
