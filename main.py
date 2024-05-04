import streamlit as st
from langchain_community.vectorstores import Chroma
from medical_documents import docs
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from metadata_info import metadata_field_info
from langchain.retrievers.self_query.base import SelfQueryRetriever
from dotenv import load_dotenv

load_dotenv()


# Creating vectorstore database using Chroma
vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())


# Defining document content description
document_content_description = "Brief summary of a medical condition"

# Creating retriever to retrieve the relevant answers
llm = ChatOpenAI(temperature=0)
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectorstore,
    document_content_description,
    metadata_field_info,
)

# Streamlit app
st.title("Gestroentrology Medical Condition Diagnosis")
symptoms = st.text_input("Enter your symptoms (comma-separated):")

if st.button("Diagnose"):
    # Retrieve conditions based on symptoms
    answer = retriever.invoke(f"I have the following symptoms: {symptoms}. What could be the condition, triage, and diagnosis?")

    conditions = []
    triages = []
    diagno = []

    # Display conditions, triage, and diagnosis
    for i in range(len(answer)):
        condition = answer[i].metadata.get("condition")
        conditions.append(condition)
        triage = answer[i].metadata.get("triage")
        triages.append(triage)
        diagnosis = answer[i].metadata.get("diagnosis")
        diagno.append(diagnosis)

    unique_conditions = set(conditions)
    unique_triages = set(triages)
    unique_diagnoses = set(diagno)

    for condition, triage, diagnosis in zip(unique_conditions, unique_triages, unique_diagnoses):
        st.write(f"Condition: {condition}")
        st.write(f"Triage: {triage}")
        st.write(f"Diagnosis: {diagnosis}")


