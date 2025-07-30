from main import Webflow
from settings import WEBFLOW_API_TOKEN
from main import Webflow
import json
import random
import time

# Initialize the Webflow client
webflow_client = Webflow(token=WEBFLOW_API_TOKEN)
"""Works"""
# print(">>> Testing: get_authorized_user_info")
# authorized_user = webflow_client.tokens.get_authorized_user_info()
# print("Authorized User Info:", authorized_user)

"""Error 500. An Internal error occurred"""
# print(">>> Testing: get_authorization_info")
# auth_info = webflow_client.tokens.get_authorization_info()
# print("Authorization Info:", auth_info)


"""Works"""
print(">>> Testing: list_sites")
sites_response = webflow_client.sites.list_sites()
print("📄 Sites Response:", json.dumps(sites_response, indent=2))

site_id = sites_response["sites"][0]["id"]

# sites_response = webflow_client.sites.list_sites()
# site_list = sites_response.get("sites", [])
#
# if not site_list:
#     print("❌ No sites available to test get_site.")
# else:
#     site_id = site_list[0]["id"]
#     print(f"✅ Using site_id: {site_id}")

print(">>> Testing: get_site")
site_details = webflow_client.sites.get_site(site_id=site_id)
print("🔍 Site Details:", json.dumps(site_details, indent=2))

#
# sites_response = webflow_client.sites.list_sites()
# site_list = sites_response.get("sites", [])
#
# if not site_list:
#     print("❌ No sites available to test get_custom_domains.")
# else:
#     site_id = site_list[0]["id"]
#     print(f"✅ Using site_id: {site_id}")
#
#     print(">>> Testing: get_custom_domains")
#     domains = webflow_client.sites.get_custom_domains(site_id)
#     print("🌐 Custom Domains:", json.dumps(domains, indent=2))
#
#
#
# # sites_response = webflow_client.sites.list_sites()
# # site_list = sites_response.get("sites", [])
#
# # if not site_list:
# #     print("❌ No sites available to test publish_site.")
# # else:
# #     site_id = site_list[0]["id"]
# #     print(f"✅ Using site_id: {site_id}")
#
#     # print(">>> Testing: publish_site (Webflow subdomain only)")
#     # response = webflow_client.sites.publish_site(
#     #     site_id=site_id,
#     #     publish_to_webflow_subdomain=True
#     # )
#     # print("🚀 Publish Response:", json.dumps(response, indent=2))
#
# site_ID = "67337e69cfb40d801615041f"
#
#
# print("\n>>> Testing: list_forms")
# site_id = site_ID  # Replace with actual site ID
# forms_list = webflow_client.forms.list_forms(site_id=site_id)
# print("📄 Forms List:", json.dumps(forms_list, indent=2))
#
# print(">>> Testing: get_form_schema")
# form_schema = webflow_client.forms.get_form_schema("6881293d0d3feffe91a6f070")
# print("📋 Form Schema:", json.dumps(form_schema, indent=2))
#
#
# print(">>> Testing: list_form_submissions")
# submissions = webflow_client.forms.list_form_submissions("6881293d0d3feffe91a6f070", limit=5)
# print("📨 Submissions:", json.dumps(submissions, indent=2))
#

"""Works"""
print(">>> Testing: create_webhook")
create_webhook=webflow_client.webhooks.create_webhook(site_id=site_id,
                                                      url='www.workplayapp.com',
                                                      triggerType='form_submission',
                                                      id=None,
                                                      workspaceId=None,
                                                      siteId=None,
                                                      filter=None,
                                                      lastTriggered=None,
                                                      createdOn=None
                                                      )
print("Create Webhook:", json.dumps(create_webhook, indent=2))

"""Works"""
print(">>> Testing: list_webhooks")
list_webhooks = webflow_client.webhooks.list_webhooks(site_id=site_id)
print("List Webhook:", json.dumps(list_webhooks, indent=2))
webhook_id = list_webhooks["webhooks"][0]["id"]

"""Works"""
print(">>> Testing: get_webhook")
get_webhook=webflow_client.webhooks.get_webhook(webhook_id=webhook_id)
print("Get Webhook:", json.dumps(get_webhook, indent=2))

"""Work"""
print(">>> Testing: remove_webhook")
remove_webhook=webflow_client.webhooks.remove_webhook(webhook_id=webhook_id)
print("Remove Webhook:", json.dumps(remove_webhook, indent=2))
