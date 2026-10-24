def get_target_config():
    model_name=input("Enter model name to be tested :")
    API_Endpoint=input("Enter API Endpoint or URL of LLM / Rag : ")
    API_key=input("API Key (optional):")
    Tools_to_test=input("Enter tool name to test during session : ")
    session_id=input("Session/Auth Token (optional):")

    target_data={
    "model_name":model_name,
    "api_endpoint":API_Endpoint,
    "api_key":API_key,
    "tools_to_test":Tools_to_test,
    "session_id":session_id
    }
    return target_data

#get_target_config()

