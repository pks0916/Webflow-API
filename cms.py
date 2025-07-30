from base import BaseWebflowEndpoint
class WebflowCMS(BaseWebflowEndpoint):
    # def list_collections(self, site_id, limit=None, offset=None):
    #     """
    #     Returns a list of CMS Collections configured on the given Webflow site.
    #     Supports optional pagination with `limit` and `offset`.
    #
    #     https://developers.webflow.com/data/reference/cms/collections/list
    #     """
    #
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "site_id") and value is not None
    #     }
    #
    #     return self.connector.get(
    #         endpoint=f"sites/{site_id}/collections",
    #         query_params=query_params
    #     )
    #
    # def get_collection_details(self, collection_id):
    #     """
    #     Returns the full details of a CMS Collection using its collection ID.
    #
    #     https://developers.webflow.com/data/reference/cms/collections/get
    #     """
    #     return self.connector.get(
    #         endpoint=f"collections/{collection_id}"
    #     )
    #
    #
    # def create_collection(self,
    #                   site_id,
    #                   displayName,
    #                   singularName,
    #                   slug=None,
    #                   fields=None):
    #     """
    #     Creates a new CMS Collection on the given Webflow site.
    #
    #     https://developers.webflow.com/data/reference/cms/collections/create
    #     """
    #
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "site_id") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #
    #     return self.connector.post(
    #         endpoint=f"sites/{site_id}/collections",
    #         json=payload,
    #         headers=headers
    #     )
    #
    # def delete_collection(self, collection_id):
    #     """
    #     Deletes a CMS Collection by its ID.
    #
    #     https://developers.webflow.com/data/reference/cms/collections/delete
    #     """
    #
    #     return self.connector.delete(
    #         endpoint=f"collections/{collection_id}"
    #     )
    #
    #
    # def create_collection_field(self,
    #                         collection_id,
    #                         type,
    #                         displayName,
    #                         isRequired=False,
    #                         helpText=None,
    #                         id=None,
    #                         isEditable=True):
    #     """
    #     Creates a field inside a Webflow CMS Collection.
    #
    #     https://developers.webflow.com/data/reference/cms/collection-fields/create
    #     """
    #
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #
    #     return self.connector.post(
    #         endpoint=f"collections/{collection_id}/fields",
    #         json=payload,
    #         headers=headers
    #     )
    #
    # def update_collection_field(self,
    #                         collection_id,
    #                         field_id,
    #                         isRequired=None,
    #                         displayName=None,
    #                         helpText=None):
    #     """
    #     Updates an existing custom field in a CMS Collection.
    #
    #     https://developers.webflow.com/data/reference/cms/collection-fields/update
    #     """
    #
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "field_id") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #
    #     return self.connector.patch(
    #         endpoint=f"collections/{collection_id}/fields/{field_id}",
    #         json=payload,
    #         headers=headers
    #     )
    #
    # def delete_collection_field(self, collection_id, field_id):
    #     """
    #     Deletes a custom field from a CMS Collection.
    #
    #     https://developers.webflow.com/data/reference/cms/collection-fields/delete
    #     """
    #     return self.connector.delete(
    #         endpoint=f"collections/{collection_id}/fields/{field_id}"
    #     )

    """The individual methods followed by the combined method underneath
    Not tested"""
    # def list_collection_items(self, collection_id,
    #                           cmsLocaleId=None,
    #                           offset=None,
    #                           limit=None,
    #                           name=None,
    #                           slug=None,
    #                           lastPublished=None,
    #                           sortBy=None,
    #                           sortOrder=None):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     return self.connector.get(
    #         endpoint=f"/collections/{collection_id}/items",
    #         query_params=query_params
    #     )
    #
    # def list_live_collection_items(self, collection_id,
    #                                cmsLocaleId=None,
    #                                offset=None,
    #                                limit=None,
    #                                name=None,
    #                                slug=None,
    #                                lastPublished=None,
    #                                sortBy=None,
    #                                sortOrder=None):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     return self.connector.get(
    #         endpoint=f"/collections/{collection_id}/items/live",
    #         query_params=query_params
    #     )
    """The combined method"""
    # def list_collection_items(self,
    #                           collection_id,
    #                           live: bool = False,
    #                           cmsLocaleId=None,
    #                           offset=None,
    #                           limit=None,
    #                           name=None,
    #                           slug=None,
    #                           lastPublished=None,
    #                           sortBy=None,
    #                           sortOrder=None):
    #     """
    #     Fetch items from a Collection. By default hits the draft endpoint;
    #     set live=True to hit the /live endpoint.
    #
    #     :param collection_id:  ID of the CMS collection
    #     :param live:           False → /items, True → /items/live
    #     :param cmsLocaleId:    optional locale
    #     :param offset:         optional paging offset
    #     :param limit:          optional page size
    #     :param name:           optional filter by name
    #     :param slug:           optional filter by slug
    #     :param lastPublished:  optional filter timestamp
    #     :param sortBy:         optional sort field
    #     :param sortOrder:      optional sort direction
    #     """
    #     # collect only the non‐None params
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "live") and value is not None
    #     }
    #
    #     # choose the right endpoint
    #     suffix = "/live" if live else ""
    #     endpoint = f"/collections/{collection_id}/items{suffix}"
    #
    #     return self.connector.get(
    #         endpoint=endpoint,
    #         query_params=query_params
    #     )

    """The individual methods followed by the combined method underneath
    Not tested"""
    # def get_collection_item(self, collection_id, item_id,
    #                         cmsLocaleId=None):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "item_id") and value is not None
    #     }
    #     return self.connector.get(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}",
    #         query_params=query_params
    #     )
    #
    # def get_live_collection_item(self, collection_id, item_id,
    #                              cmsLocaleId=None):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "item_id") and value is not None
    #     }
    #     return self.connector.get(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}/live",
    #     )
    """The combined method"""
    # def get_collection_item(self,
    #                         collection_id,
    #                         item_id,
    #                         cmsLocaleId=None,
    #                         live: bool = False):
    #     """
    #     Fetch a single CMS item, either draft or live.
    #
    #     :param collection_id:  ID of the collection
    #     :param item_id:        ID of the item
    #     :param cmsLocaleId:    optional locale
    #     :param live:           False → /items/{item_id}, True → /items/{item_id}/live
    #     """
    #     # 1) Build query‐params (only cmsLocaleId in this case)
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "item_id", "live") and v is not None
    #     }
    #
    #     # 2) Choose suffix based on live flag
    #     suffix = "/live" if live else ""
    #     endpoint = f"/collections/{collection_id}/items/{item_id}{suffix}"
    #
    #     # 3) Fire the request
    #     return self.connector.get(
    #         endpoint=endpoint,
    #         query_params=query_params
    #     )

    # def create_collection_items(self, collection_id, skipInvalidFiles=None ):
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #
    # def create_live_collection_items(self, collection_id,
    #                                  skipInvalidFiles=None,):
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }


    """Nothing to combine with
    Not tested"""
    # def create_localized_collection_items(self, collection_id,fieldData,
    #                                       skipInvalidFiles=None,
    #                                       cmsLocaleIds=None,
    #                                       isArchived=None,
    #                                       isDraft=None):
    #     headers= {"Content-Type": "application/json"}
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "fieldData",) and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id",) and value is not None
    #     }
    #     return self.connector.post(
    #         endpoint=f"/collections/{collection_id}/items/bulk",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )

    """The individual methods followed by the combined method underneath
       Not tested"""
    # def update_single_collection_item(self, collection_id, item_id,
    #                                   skipInvalidFiles=None,
    #                                   cmsLocaleId=None,
    #                                   isArchived=None,
    #                                   isDraft=None,
    #                                   fieldData=None):
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id",) and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )
    # def update_single_live_collection_item(self, collection_id, item_id,
    #                                        skipInvalidFiles=None,
    #                                        cmsLocaleId=None,
    #                                        isArchived=None,
    #                                        isDraft=None,
    #                                        fieldData=None):
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id",) and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}/live",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )
    """The combined method"""
    # def update_single_collection_item(self,
    #                                   collection_id,
    #                                   item_id,
    #                                   skipInvalidFiles=None,
    #                                   cmsLocaleId=None,
    #                                   isArchived=None,
    #                                   isDraft=None,
    #                                   fieldData=None,
    #                                   live=False):
    #     # collect everything but self & collection_id
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     # same for the JSON body
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #
    #     # choose suffix based on live flag
    #     suffix = "/live" if live else ""
    #
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}{suffix}",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )

    """The individual methods followed by the combined method underneath
           Not tested"""
    # def update_collection_items(self, collection_id,
    #                             skipInvalidFiles=None,
    #                             items=None):
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id","skipInvalidFiles") and v is not None
    #     }
    #     # same for the JSON body
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "skipInvalidFiles") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )
    #
    # def update_live_collection_items(self, collection_id,
    #                                  skipInvalidFiles=None,
    #                                  items=None):
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "skipInvalidFiles") and v is not None
    #     }
    #     # same for the JSON body
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "skipInvalidFiles") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items/live",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )
    """The combined method"""
    # def update_collection_items(self,
    #                             collection_id,
    #                             skipInvalidFiles=None,
    #                             items=None,
    #                             live=False):
    #     # build query_params from everything except self, collection_id, skipInvalidFiles, live
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "skipInvalidFiles", "live") and v is not None
    #     }
    #     # build payload from everything except self, collection_id, skipInvalidFiles, live
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "skipInvalidFiles", "live") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #
    #     # choose live vs draft endpoint
    #     suffix = "/live" if live else ""
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items{suffix}",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )

    """The individual methods followed by the combined method underneath
               Not tested"""
    # def delete_single_collection_item(self, collection_id, item_id,
    #                                   cmsLocaleId=None):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self","collection_id","item_id") and value is not None
    #     }
    #     return self.connector.delete(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}",
    #         query_params=query_params
    #     )
    #
    # def unpublish_single_live_collection_item(self, collection_id, item_id,
    #                                   cmsLocaleId=None):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "item_id") and value is not None
    #     }
    #     return self.connector.delete(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}/live",
    #         query_params=query_params
    #     )
    """The combined method"""
    # def delete_single_collection_item(self,
    #                                   collection_id,
    #                                   item_id,
    #                                   cmsLocaleId=None,
    #                                   live=False):
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "item_id", "live") and value is not None
    #     }
    #     suffix = "/live" if live else ""
    #     return self.connector.delete(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}{suffix}",
    #         query_params=query_params
    #     )

    """The individual methods followed by the combined method underneath
                   Not tested"""
    # def delete_collection_items(self, collection_id, items):
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.delete(
    #         endpoint=f"/collections/{collection_id}/items",
    #         json=payload,
    #         headers=headers
    #     )
    # def unpublish_live_collection_items(self, collection_id, items):
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.delete(
    #         endpoint=f"/collections/{collection_id}/items/live",
    #     )
    """The combined method"""
    # def delete_collection_items(self,
    #                             collection_id,
    #                             items,
    #                             live=False):
    #     """
    #     Delete (or unpublish) multiple items in a collection.
    #
    #     :param collection_id: ID of the CMS collection
    #     :param items:         list of item‐dicts, each must include “id” (and optionally cmsLocaleId)
    #     :param live:          False → delete draft items; True → unpublish live items
    #     """
    #     # Build the JSON payload from locals (excluding self, collection_id & live flag)
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "live") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #
    #     # Pick the right endpoint suffix
    #     suffix = "/live" if live else ""
    #     endpoint = f"/collections/{collection_id}/items{suffix}"
    #
    #     return self.connector.delete(
    #         endpoint=endpoint,
    #         json=payload,
    #         headers=headers
    #     )
    #
    """Nothing to combine with
        Not tested"""
    # def publish_collection_items(self, collection_id,
    #                              Item_IDs,
    #                              Item_IDs_with_locales):
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.post(
    #         endpoint=f"/collections/{collection_id}/items/publish",
    #         json=payload,
    #         headers=headers
    #     )



















    

    

