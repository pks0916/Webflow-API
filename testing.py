# from main import Webflow
# from settings import WEBFLOW_API_TOKEN
# from main import Webflow
# import json
# import random
# import time

# # Initialize the Webflow client
# webflow_client = Webflow(token=WEBFLOW_API_TOKEN)
# """ Works"""
# print(">>> Testing: get_authorized_user_info")
# authorized_user = webflow_client.tokens.get_authorized_user_info()
# print("Authorized User Info:", authorized_user)


# """Access to this endpoint requires a bearer token from a Data Client App. doesnt work """
# # print(">>> Testing: get_authorization_info")
# # auth_info = webflow_client.tokens.get_authorization_info()
# # print("Authorization Info:", auth_info)




# """ all of sites beside the last one publish site works"""
# print(">>> Testing: list_sites")
# sites_response = webflow_client.sites.list_sites()
# print("📄 Sites Response:", json.dumps(sites_response, indent=2))


# sites_response = webflow_client.sites.list_sites()
# site_list = sites_response.get("sites", [])
# site_id=sites_response["sites"][0]["id"]

# if not site_list:
#     print("❌ No sites available to test get_site.")
# else:
#     site_id = site_list[0]["id"]
#     print(f"✅ Using site_id: {site_id}")

#     print(">>> Testing: get_site")
#     site_details = webflow_client.sites.get_site(site_id)
#     print("🔍 Site Details:", json.dumps(site_details, indent=2))


# sites_response = webflow_client.sites.list_sites()
# site_list = sites_response.get("sites", [])

# if not site_list:
#     print("❌ No sites available to test get_custom_domains.")
# else:
#     site_id = site_list[0]["id"]
#     print(f"✅ Using site_id: {site_id}")

#     print(">>> Testing: get_custom_domains")
#     domains = webflow_client.sites.get_custom_domains(site_id)
#     print("🌐 Custom Domains:", json.dumps(domains, indent=2))

# """ punlish site doesnt work 403 """
# # sites_response = webflow_client.sites.list_sites()
# # site_list = sites_response.get("sites", [])

# # if not site_list:
# #     print("❌ No sites available to test publish_site.")
# # else:
# #     site_id = site_list[0]["id"]
# #     print(f"✅ Using site_id: {site_id}")

# #     print(">>> Testing: publish_site (Webflow subdomain only)")
# #     response = webflow_client.sites.publish_site(
# #         site_id=site_id,
# #         publish_to_webflow_subdomain=True
# #     )
# #     print("🚀 Publish Response:", json.dumps(response, indent=2))






# """ all of Forms works """
# print("\n>>> Testing: list_forms")
# site_id = site_id  # Replace with actual site ID
# forms_list = webflow_client.forms.list_forms(site_id=site_id)
# print("📄 Forms List:", json.dumps(forms_list, indent=2))

# print(">>> Testing: get_form_schema")
# form_schema = webflow_client.forms.get_form_schema("6881293d0d3feffe91a6f070")
# print("📋 Form Schema:", json.dumps(form_schema, indent=2))


# print(">>> Testing: list_form_submissions")
# submissions = webflow_client.forms.list_form_submissions("6881293d0d3feffe91a6f070", limit=5)
# print("📨 Submissions:", json.dumps(submissions, indent=2))


# print(">>> Testing: list_form_submissions")
# submissions = webflow_client.forms.list_form_submissions("6881293d0d3feffe91a6f070", limit=5)
# print("📨 Submissions:", json.dumps(submissions, indent=2))

# # Extract first submission ID
# if submissions and "submissions" in submissions and submissions["submissions"]:
#     submission_id = submissions["submissions"][0]["_id"]
#     print("✔️ Using submission_id:", submission_id)

#     # Get submission
#     print(">>> Testing: get_form_submission")
#     submission = webflow_client.forms.get_form_submission(submission_id)
#     print("📄 Single Submission:", json.dumps(submission, indent=2))

#     # Modify submission
#     print(">>> Testing: modify_form_submission")
#     response = webflow_client.forms.modify_form_submission(
#         form_submission_id=submission_id,
#         formSubmissionData={"hiddenFieldName": "newValue"}  # Replace key with actual hidden field name
#     )
#     print("✏️ Modified Submission:", json.dumps(response, indent=2))

#     # Delete submission
#     print(">>> Testing: delete_form_submission")
#     delete_result = webflow_client.forms.delete_form_submission(submission_id)
#     print("🗑️ Delete Result:", json.dumps(delete_result, indent=2))

# else:
#     print("⚠️ No submissions found — skipping get, modify, and delete tests.")




# """ALL User.py doesnt work 403 error"""
# # # ✅ Test: list_users
# # print(">>> Testing: list_users")
# # users = webflow_client.users.list_users(site_id=site_id)
# # print("👥 Users List:", json.dumps(users, indent=2))


# # print(">>> Testing: list_access_groups")
# # access_groups = webflow_client.users.list_access_groups(site_id=site_id)
# # print("🔐 Access Groups:", json.dumps(access_groups, indent=2))


# # user_id = "replace_with_real_user_id"

# # # ✅ Test: get_user
# # print(">>> Testing: get_user")
# # user = webflow_client.users.get_user(site_id=site_id, user_id=user_id)
# # print("📄 Single User:", json.dumps(user, indent=2))

# # # ✅ Test: update_user (example: mark email as verified)
# # print(">>> Testing: update_user")
# # update_response = webflow_client.users.update_user(
# #     site_id=site_id,
# #     user_id=user_id,
# #     isEmailVerified=True
# # )
# # print("✏️ Updated User:", json.dumps(update_response, indent=2))


# # # ✅ Test: create_and_invite_user
# # print(">>> Testing: create_and_invite_user")
# # invite_response = webflow_client.users.create_and_invite_user(
# #     site_id=site_id,
# #     email="testuser@example.com",
# #     status="invited"  # optional
# # )
# # print("✉️ Invite User Response:", json.dumps(invite_response, indent=2))






# """Works"""
# print(">>> Testing: create_webhook")
# create_webhook=webflow_client.webhooks.create_webhook(site_id=site_id,
#                                                       triggerType='form_submission',
#                                                       url='www.workplayapp.com',
#                                                       id=None,
#                                                       workspaceId=None,
#                                                       siteId=None,
#                                                       filter=None,
#                                                       lastTriggered=None,
#                                                       createdOn=None
#                                                       )
# print("Create Webhook:", json.dumps(create_webhook, indent=2))

# """Works"""
# print(">>> Testing: list_webhooks")
# list_webhooks = webflow_client.webhooks.list_webhooks(site_id=site_id)
# print("List Webhook:", json.dumps(list_webhooks, indent=2))

# webhook_id = list_webhooks["webhooks"][0]["id"]

# """Works"""
# print(">>> Testing: get_webhook")
# get_webhook=webflow_client.webhooks.get_webhook(webhook_id=webhook_id)
# print("Get Webhook:", json.dumps(get_webhook, indent=2))

# """Works"""
# print(">>> Testing: remove_webhook")
# remove_webhook=webflow_client.webhooks.remove_webhook(webhook_id=webhook_id)
# print("Remove Webhook:", json.dumps(remove_webhook, indent=2))










