from base import BaseWebflowEndpoint
class WebflowSites(BaseWebflowEndpoint):
    

    def list_sites(self):
        """
        Retrieves a list of all sites the current API token can access.
        Required Scope: sites:read
        Endpoint: GET /v2/sites
        https://developers.webflow.com/data/reference/sites/list
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint="sites",
            headers=headers
        )


    def get_site(self, site_id):
        """
        Retrieves detailed information about a specific site by its ID.
        Required Scope: sites:read
        https://developers.webflow.com/data/reference/sites/get
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint=f"sites/{site_id}",
            headers=headers
        )
    def get_custom_domains(self, site_id):
        """
        Retrieves all custom domains associated with a specific site.
        Required Scope: sites:read
        Endpoint: GET /v2/sites/:site_id/custom_domains
        https://developers.webflow.com/data/reference/sites/get-custom-domain
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint=f"sites/{site_id}/custom_domains",
            headers=headers
        )
    
    def publish_site(self, site_id, custom_domains=None, publish_to_webflow_subdomain=False):
        """
        Publishes the specified site to selected custom domains and/or the Webflow subdomain.
        Rate limit: 1 publish per minute
        Required Scope: sites:write
        Endpoint: POST /v2/sites/:site_id/publish
        https://developers.webflow.com/data/reference/sites/publish
        """

        payload = {
            "publishToWebflowSubdomain": publish_to_webflow_subdomain
        }

        if custom_domains:
            payload["customDomains"] = custom_domains

        headers = {"Content-Type": "application/json"}

        return self.connector.post(
            endpoint=f"sites/{site_id}/publish",
            json=payload,
            headers=headers
        )

    

    


    

