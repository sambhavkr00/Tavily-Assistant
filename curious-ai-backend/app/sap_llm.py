from langchain_community.llms.sap_ai_core import SAPAICore
from app.credentials import get_credential

def get_sap_llm():
    """
    Creates and configures an instance of the SAP AI Core LLM.

    Returns:
        An instance of the SAP AI Core LLM.
    """
    llm = SAPAICore(
        url=get_credential("AICORE_URL"),
        client_id=get_credential("AICORE_CLIENT_ID"),
        client_secret=get_credential("AICORE_CLIENT_SECRET"),
        auth_url=get_credential("AICORE_AUTH_URL"),
        resource_group=get_credential("AICORE_RESOURCE_GROUP"),
        deployment_id=get_credential("AICORE_DEPLOYMENT_ID"),
    )
    return llm
