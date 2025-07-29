

from base import BaseWebflowEndpoint
class WebflowWebhooks(BaseWebflowEndpoint):
    def list_webhooks(self, site_id):
        """
        List all App-created Webhooks registered for a given site
        Required scope: sites:read
        Endpoint: get/v2/sites/:site_id/webhooks
        https://developers.webflow.com/data/reference/webhooks/list
        """
        headers= {"Content-Type": "application/json"}
        return self.connector.get(
            endpoint= f'/sites/{site_id}/webhooks',
            headers=headers
        )

    def get_webhook(self, webhook_id):
        """
        returns a specific webhook instance
        Required scope: sites:read
        Endpoint: get/v2/webhooks/:webhook_id
        https://developers.webflow.com/data/reference/webhooks/get
        """
        headers= {"Content-Type": "application/json"}
        return self.connector.get(
            endpoint= f'/webhooks/{webhook_id}',
            headers=headers
        )

    def create_webhook(self, site_id,
                       triggerType,
                       url,
                       id=None,
                       workspaceId=None,
                       siteId=None,
                       filter=None,
                       lastTriggered=None,
                       createdOn=None
                       ):
        """
        Creates a new webhook. Limit of 75 registrations per triggerType, per site.
        Required scope: sites:write
        Endpoint: post/v2/sites/:site_id/webhooks
        https://developers.webflow.com/data/reference/webhooks/create
        """
        headers= {"Content-Type": "application/json"}
        payload = {key: value
                   for key, value in locals().items()
                   if key not in ("self", "site_id", "triggerType", "url") and value is not None and not hasattr(value, "__dict__")
                   }
        return self.connector.post(
            endpoint= f'/sites/{site_id}/webhooks',
            json=payload,
            headers=headers
        )

    def remove_webhook(self, webhook_id):
        """
        Removes a webhook
        Required scope: sites:read
        Endpoint: delete/v2/webhooks/:webhook_id
        https://developers.webflow.com/data/reference/webhooks/delete
        """
        return self.connector.delete(
            endpoint= f'/webhooks/{webhook_id}'
        )


