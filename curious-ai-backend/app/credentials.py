
import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_credential(credential_name: str) -> str:
    """
    Retrieves a credential from VCAP_SERVICES environment variable if available,
    otherwise falls back to getting it from a local .env file.

    Args:
        credential_name: The name of the credential to retrieve (e.g., "GOOGLE_API_KEY").

    Returns:
        The credential value.

    Raises:
        ValueError: If the credential is not found.
    """
    vcap_services = os.getenv("VCAP_SERVICES")
    
    if vcap_services:
        try:
            services = json.loads(vcap_services)
            # Look for credentials in user-provided services
            if "user-provided" in services:
                for service in services["user-provided"]:
                    if "credentials" in service and credential_name in service["credentials"]:
                        return service["credentials"][credential_name]
        except json.JSONDecodeError:
            # Handle cases where VCAP_SERVICES is not a valid JSON
            pass

    credential = os.getenv(credential_name)
    if not credential:
        raise ValueError(f"{credential_name} not found in VCAP_SERVICES or .env file.")
    
    return credential
