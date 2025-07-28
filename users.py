from base import BaseWebflowEndpoint
class WebflowUsers(BaseWebflowEndpoint):
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
    

    def get_user(self, site_id, user_id):
        """
        Retrieves detailed information about a specific user on a site.

        https://developers.webflow.com/data/reference/users/users/get
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint=f"sites/{site_id}/users/{user_id}",
            headers=headers
        )
    
    def delete_user(self, site_id, user_id):
        """
        Deletes a specific user from a Webflow site.

        https://developers.webflow.com/data/reference/users/users/delete
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.delete(
            endpoint=f"sites/{site_id}/users/{user_id}",
            headers=headers
        )
    
    def update_user(self,
                    site_id,
                    user_id,
                    isEmailVerified=None,
                    lastUpdated=None,
                    invitedOn=None,
                    createdOn=None,
                    lastLogin=None,
                    status=None,
                    accessGroups=None,
                    data=None):
        """
        Updates fields for a specific user on a Webflow site.
        Email and password cannot be updated using this endpoint.

        https://developers.webflow.com/data/reference/users/users/update
        """

        payload = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id", "user_id") and value is not None
        }

        headers = {"Content-Type": "application/json"}

        return self.connector.patch(
            endpoint=f"sites/{site_id}/users/{user_id}",
            json=payload,
            headers=headers
        )
    

    def create_and_invite_user(self,
                                site_id,
                                email,
                                accessGroups=None,
                                isEmailVerified=None,
                                lastUpdated=None,
                                invitedOn=None,
                                createdOn=None,
                                lastLogin=None,
                                status=None,
                                data=None,
                                id=None):
        """
        Creates and invites a new user to the site by sending them an email invitation.

        https://developers.webflow.com/data/reference/users/users/invite
        """

        payload = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        headers = {"Content-Type": "application/json"}

        return self.connector.post(
            endpoint=f"sites/{site_id}/users/invite",
            json=payload,
            headers=headers
        )
    

    def list_access_groups(self, site_id, offset=None, limit=None, sort=None):
        """
        Lists access groups configured for a given Webflow site.
        Used to assign users to roles/groups.
        https://developers.webflow.com/data/reference/users/access-groups/list
        
        """

        query_params = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        return self.connector.get(
            endpoint=f"sites/{site_id}/accessgroups",
            query_params=query_params
        )


    
    

    


    

