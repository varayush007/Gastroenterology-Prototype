# Medical Condition Diagnosis App

This is a Streamlit application that allows users to enter their symptoms and receive a diagnosis, triage recommendations, and diagnostic methods for potential medical conditions based on the provided symptoms.

## Requirements

- Python 3.7 or later
- Streamlit
- LangChain
- Chroma
- OpenAI API key (for embeddings and language model)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/medical-condition-diagnosis.git

2. Navigate to the project directory:
   
   ```bash
   cd medical-condition-diagnosis

3. Create a virtual environment and activate it:

   ```bash
    python -m venv env
    source env/bin/activate # On Windows, use `env\Scripts\activate`
   
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   
5. Create a .env file in the project root directory and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your_openai_api_key

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run main.py
2. In the web interface, enter your symptoms (comma-separated) in the input field.
3. Click the "Diagnose" button.
4. The app will display the potential medical conditions, triage recommendations, and diagnostic methods based on the provided symptoms.
