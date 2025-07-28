from base import BaseWebflowEndpoint
class WebflowUsers:
    def list_users(self, site_id, offset=None, limit=None, sort=None):
        """
        Retrieves users of a given Webflow site.
        Supports pagination and sorting.
        https://developers.webflow.com/data/reference/users/users/list
        
        """

        query_params = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        return self.connector.get(
            endpoint=f"sites/{site_id}/users",
            query_params=query_params
        )