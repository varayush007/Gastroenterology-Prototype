# Importing neccessary libraires
import streamlit as st
from langchain_community.vectorstores import Chroma
from medical_documents import docs
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from metadata_info import metadata_field_info
from langchain.retrievers.self_query.base import SelfQueryRetriever
from dotenv import load_dotenv

load_dotenv()


# Creating the vectorstore database
vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())


# Defining document content description
document_content_description = "Brief summary of a medical condition"

# Retriever to retrieve the relevant info from doc
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
    # Check if symptoms are in the known list
    all_known_symptoms = set([sym.lower() for doc in docs for sym in doc.metadata['symptoms'].split(', ')])
    input_symptoms = set(sym.strip().lower() for sym in symptoms.split(','))

    if not input_symptoms.issubset(all_known_symptoms):
        st.write("I do not have any knowledge regarding these symptoms. Please consult a doctor.")
    else:
        # Retrieve conditions based on symptoms
        answer = retriever.invoke(
            f"I have the following symptoms: {symptoms}. What could be the condition, triage, and diagnosis?")

        if not answer:
            st.write("No matching conditions found in the document.")
        else:
            conditions = []
            triages = []
            diagno = []

            # Displaying conditions, triage, and diagnosis
            for res in answer:
                condition = res.metadata.get("condition")
                conditions.append(condition)
                triage = res.metadata.get("triage")
                triages.append(triage)
                diagnosis = res.metadata.get("diagnosis")
                diagno.append(diagnosis)

            unique_conditions = set(conditions)
            unique_triages = set(triages)
            unique_diagnoses = set(diagno)

            for condition, triage, diagnosis in zip(unique_conditions, unique_triages, unique_diagnoses):
                st.write(f"Condition: {condition}")
                st.write(f"Triage: {triage}")
                st.write(f"Diagnosis: {diagnosis}")


