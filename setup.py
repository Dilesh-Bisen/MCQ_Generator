from setuptools import setup, find_packages

setup(
    name="MCQ_Generator",
    version="0.1.0",
    author="Dilesh Bisen",
    author_email="1dileshbisen@gmail.com",
    description="Multiple Choice Questions (MCQs) Generator using GenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dilesh-Bisen/MCQ_Generator.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
)

