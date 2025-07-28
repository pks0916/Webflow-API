from main import Webflow
from settings import WEBFLOW_API_TOKEN

# Initialize the Webflow client
webflow_client = Webflow(token=WEBFLOW_API_TOKEN)

print(">>> Testing: get_authorized_user_info")
authorized_user = webflow_client.tokens.get_authorized_user_info()
print("Authorized User Info:", authorized_user)

print(">>> Testing: get_authorization_info")
auth_info = webflow_client.tokens.get_authorization_info()
print("Authorization Info:", auth_info)
