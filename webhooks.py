

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
                   if key not in ("self", "site_id") and value is not None and not hasattr(value, "__dict__")
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
    

    def form_submission(self,
                             
                             name=None,
                             siteId=None,
                             data=None,
                             schema=None,
                             submittedAt=None,
                             id=None,
                             formId=None,
                             formElementId=None):
        """
        Simulates a Webflow 'form_submission' webhook by POSTing mock data to a target webhook URL.
        https://developers.webflow.com/data/reference/webhooks/events/form-submission
        All fields are optional based on Webflow documentation.
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "form_submission",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )
    
    def site_publish(self,
                          
                          siteId=None,
                          publishedOn=None,
                          domains=None,
                          publishedBy=None):
        """
        Simulates a Webflow 'site_publish' webhook by POSTing mock data to a target webhook URL.
        https://developers.webflow.com/data/reference/webhooks/events/site-publish
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "site_publish",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )
    

    def simulate_collection_item_created(self,
                                     
                                     id,
                                     workspaceId,
                                     siteId,
                                     collectionId,
                                     fieldData,
                                     cmsLocaleId=None,
                                     lastPublished=None,
                                     lastUpdated=None,
                                     createdOn=None,
                                     isArchived=None,
                                     isDraft=None):
        """
        Simulates a Webflow 'collection_item_created' webhook by POSTing mock data to a target webhook URL.

        
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "collection_item_created",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )

    
    def collection_item_updated(self,
                                     
                                     id,
                                     workspaceId,
                                     siteId,
                                     collectionId,
                                     fieldData,
                                     cmsLocaleId=None,
                                     lastPublished=None,
                                     lastUpdated=None,
                                     createdOn=None,
                                     isArchived=None,
                                     isDraft=None):
        """
        Simulates a Webflow 'collection_item_changed' webhook by POSTing mock data to a target webhook URL.

        https://developers.webflow.com/data/reference/webhooks/events/collection-item-changed
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "collection_item_changed",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )
    

    def collection_item_deleted(self,
                                     
                                     id=None,
                                     siteId=None,
                                     workspaceId=None,
                                     collectionId=None,
                                     cmsLocaleId=None,
                                     lastPublished=None,
                                     lastUpdated=None,
                                     createdOn=None,
                                     isArchived=None,
                                     isDraft=None,
                                     fieldData=None):
        """
        Simulates a Webflow 'collection_item_deleted' webhook by POSTing mock data to a target webhook URL.
        https://developers.webflow.com/data/reference/webhooks/events/collection-item-deleted
        All fields are optional based on Webflow documentation.
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "collection_item_deleted",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )
    def new_user_added(self,
                                
                                id=None,
                                isEmailVerified=None,
                                lastUpdated=None,
                                invitedOn=None,
                                createdOn=None,
                                lastLogin=None,
                                status=None,
                                accessGroups=None,
                                data=None):
        """
        Simulates a Webflow 'user_account_added' webhook by POSTing mock data to a target webhook URL.

        https://developers.webflow.com/data/reference/webhooks/events/user-account-added
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "user_account_added",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )
    
    
    def account_updated(self,
                                  
                                  id=None,
                                  isEmailVerified=None,
                                  lastUpdated=None,
                                  invitedOn=None,
                                  createdOn=None,
                                  lastLogin=None,
                                  status=None,
                                  accessGroups=None,
                                  data=None):
        """
        Simulates a Webflow 'user_account_updated' webhook by POSTing mock data to a target webhook URL.

        https://developers.webflow.com/data/reference/webhooks/events/user-account-updated
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "user_account_updated",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )
    def account_deleted(self,
                                  
                                  id=None,
                                  isEmailVerified=None,
                                  lastUpdated=None,
                                  invitedOn=None,
                                  createdOn=None,
                                  lastLogin=None,
                                  status=None,
                                  accessGroups=None,
                                  data=None):
        """
        Simulates a Webflow 'user_account_deleted' webhook by POSTing mock data to a target webhook URL.

        https://developers.webflow.com/data/reference/webhooks/events/user-account-deleted
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "triggerType": "user_account_deleted",
            "payload": {
                key: value
                for key, value in locals().items()
                if key not in ("self", "webhook_url") and value is not None and not hasattr(value, "__dict__")
            }
        }
        return self.connector.post(
            
            json=payload,
            headers=headers,
            external=True
        )

    



    






    
    