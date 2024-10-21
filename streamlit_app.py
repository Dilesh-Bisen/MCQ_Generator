import os
import json
import pandas as pd
import traceback
import PyPDF2
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_mistralai import ChatMistralAI
from langchain_community.callbacks.manager import get_openai_callback  
from src.generate_mcqs.mcqs_generator import combine_chain
from src.generate_mcqs.logger import logging
from src.generate_mcqs.utils import read_file, get_table_data  

load_dotenv()

st.set_page_config(
    page_title="MCQ Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_response_json():
    try:
        with open(
            "response.json", "r"
        ) as file:
            return json.load(file)
    except Exception as e:
        st.error("Error loading the response.json file.")
        logging.error(f"Error loading the response.json file: {e}")
        return None

response_json = load_response_json()  

with st.form("user_input"):

    uploaded_file = st.file_uploader("Upload a PDF or text file", type=["pdf", "txt"])

    mcq_count = st.number_input("Number of MCQs", min_value=0, step=1)

    subject = st.text_input("Subject")

    tone_options = ["", "Simple", "Moderate", "Complex"]  
    tone = st.selectbox("Complexity Level of Questions", options=tone_options)

    submit_button = st.form_submit_button("Generate MCQs")

    if submit_button:
        if uploaded_file is None:
            st.warning("Please upload a file.", icon="⚠️")
        if mcq_count <= 0:
            st.warning("Please enter a number for the number of MCQs.", icon="⚠️")
        if not subject:
            st.warning("Please provide the subject.", icon="⚠️")
        if tone == "":
            st.warning("Please select a complexity level.", icon="⚠️")

        if uploaded_file is not None and subject:
            with st.spinner("Loading..."):
                try:
                    text = read_file(uploaded_file) 
                    st.info("File read successfully.")

                    with get_openai_callback() as cb:  
                        try:
                            response = combine_chain.invoke({
                                "text": text,
                                "number": mcq_count,
                                "subject": subject,
                                "tone": tone,
                                "response_json": json.dumps(response_json),
                            })
                        except Exception as e:
                            print(f"Error during combine_chain execution")
                            st.error(f"Error during combine_chain execution: {e}")
                            logging.error(f"Error during combine_chain execution: {traceback.format_exc()}")
                            response = None

                except Exception as e:
                    traceback.print_exception(type(e), e, e.__traceback__)
                    st.error("Error reading the file or processing the input.")
                else:
                    if response is not None:
                        print(f"Total Tokens: {cb.total_tokens}")
                        print(f"Prompt Tokens: {cb.prompt_tokens}")
                        print(f"Completion Tokens: {cb.completion_tokens}")
                        print(f"Total Cost: {cb.total_cost}")

                        if isinstance(response, dict):
                            quiz = response.get("quiz", None)
                            if quiz is not None:
                                table_data = get_table_data(quiz)
                                if table_data is not None and isinstance(table_data, list): 
                                    if len(table_data) > 0 and isinstance(table_data[0], dict): 
                                        df = pd.DataFrame(table_data)  
                                        df.index = df.index + 1
                                        st.table(df)
                                        st.text_area(label="Review", value=response["review"])
                                    else:
                                        st.error("Unexpected data format for quiz data.")
                                else:
                                    st.error("Error in table data.")
                        else:
                            st.write(response)
