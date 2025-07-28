from base import BaseWebflowEndpoint
class WebflowToken(BaseWebflowEndpoint):
    

    def get_authorized_user_info(self):
        """
        Retrieves information about the authorized user who owns the API token.
        Required Scope: authorized_user:read
        Response contains user ID, email, first name, and last name.
        https://developers.webflow.com/data/reference/token/authorized-by
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint="token/authorized_by",
            headers=headers
        )
    
    def get_authorization_info(self):
        """
        Retrieves metadata about the current authorization token.
        Includes scopes, rate limit, grant type, and associated application info.
        Endpoint: GET /v2/token/introspect
        https://developers.webflow.com/data/reference/token/introspect
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint="token/introspect",
            headers=headers
        )
