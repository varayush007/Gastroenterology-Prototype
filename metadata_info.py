from langchain.chains.query_constructor.base import AttributeInfo

metadata_field_info = [
    AttributeInfo(
        name="condition",
        description="Name of the medical condition",
        type="string",
    ),
    AttributeInfo(
        name="symptoms",
        description="Common symptoms associated with the condition",
        type="string",
    ),
    AttributeInfo(
        name="triage",
        description="Triage recommendations for the condition",
        type="string",
    ),
    AttributeInfo(
        name="diagnosis",
        description="Methods used for diagnosing the condition",
        type="string",
    ),
]
