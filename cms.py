from base import BaseWebflowEndpoint
class WebflowCMS(BaseWebflowEndpoint):
    def list_collections(self, site_id, limit=None, offset=None):
        """
        Returns a list of CMS Collections configured on the given Webflow site.
        Supports optional pagination with `limit` and `offset`.

        https://developers.webflow.com/data/reference/cms/collections/list
        """

        query_params = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        return self.connector.get(
            endpoint=f"sites/{site_id}/collections",
            query_params=query_params
        )
    
    def get_collection_details(self, collection_id):
        """
        Returns the full details of a CMS Collection using its collection ID.

        https://developers.webflow.com/data/reference/cms/collections/get
        """
        return self.connector.get(
            endpoint=f"collections/{collection_id}"
        )
    

    def create_collection(self,
                      site_id,
                      displayName,
                      singularName,
                      slug=None,
                      fields=None):
        """
        Creates a new CMS Collection on the given Webflow site.

        https://developers.webflow.com/data/reference/cms/collections/create
        """

        payload = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        headers = {"Content-Type": "application/json"}

        return self.connector.post(
            endpoint=f"sites/{site_id}/collections",
            json=payload,
            headers=headers
        )
    
    def delete_collection(self, collection_id):
        """
        Deletes a CMS Collection by its ID.

        https://developers.webflow.com/data/reference/cms/collections/delete
        """

        return self.connector.delete(
            endpoint=f"collections/{collection_id}"
        )
    

    def create_collection_field(self,
                            collection_id,
                            type,
                            displayName,
                            isRequired=False,
                            helpText=None,
                            id=None,
                            isEditable=True):
        """
        Creates a field inside a Webflow CMS Collection.

        https://developers.webflow.com/data/reference/cms/collection-fields/create
        """

        payload = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "collection_id") and value is not None
        }

        headers = {"Content-Type": "application/json"}

        return self.connector.post(
            endpoint=f"collections/{collection_id}/fields",
            json=payload,
            headers=headers
        )
    
    def update_collection_field(self,
                            collection_id,
                            field_id,
                            isRequired=None,
                            displayName=None,
                            helpText=None):
        """
        Updates an existing custom field in a CMS Collection.

        https://developers.webflow.com/data/reference/cms/collection-fields/update
        """

        payload = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "collection_id", "field_id") and value is not None
        }

        headers = {"Content-Type": "application/json"}

        return self.connector.patch(
            endpoint=f"collections/{collection_id}/fields/{field_id}",
            json=payload,
            headers=headers
        )
    
    def delete_collection_field(self, collection_id, field_id):
        """
        Deletes a custom field from a CMS Collection.

        https://developers.webflow.com/data/reference/cms/collection-fields/delete
        """
        return self.connector.delete(
            endpoint=f"collections/{collection_id}/fields/{field_id}"
        )
    











    

    

