import os
import json
import pandas as pd
import traceback
import PyPDF2

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.callbacks.manager import get_openai_callback
from langchain_mistralai import ChatMistralAI

from src.generate_mcqs.utils import read_file, get_table_data
from src.generate_mcqs.logger import logging

load_dotenv()

my_key = os.getenv("MISTRAL_API_KEY")

if my_key is None:
    raise ValueError("MISTRAL_API_KEY is not set.")

print("Loaded MISTRAL_API_KEY:", my_key) 

llm = ChatMistralAI(
    api_key=my_key,
    model="mistral-large-latest",
    temperature=0.5,
    max_retries=2,
)

TEMPLATE1 = """
You are tasked with creating {number} multiple-choice questions for an educational quiz. 
The topic of each question should be based on {text}. 
The subject is {subject}, and the tone of the questions should be {tone}. 
Ensure that each question effectively tests the user's knowledge, is clear, concise, and does not repeat the answer or options. 
For each question, provide {number} options, only one of which is correct. 
Return all questions and options in the following 
### RESPONSE_JSON 
{response_json}
"""

prompt1 = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE1,
)

chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="quiz", verbose=True)

TEMPLATE2 = """
You are tasked with evaluating the quiz based on the subject: {subject}. 
Please review the quiz questions and options provided in the {quiz}. 
Ensure that the questions effectively assess the knowledge of the respondents, are clear and concise, and that the options are distinct from each other. 
Provide feedback on the clarity of the questions and the appropriateness of the options given. 
Make suggestions for any improvements needed for better evaluation.
"""

prompt2 = PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE2)

chain2 = LLMChain(prompt=prompt2, llm=llm, output_key="review", verbose=True)

combine_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True,
)
