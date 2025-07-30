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

    # def list_collection_items(
    #         self,
    #         collection_id,
    #         cmsLocaleId=None,
    #         offset=None,
    #         limit=None,
    #         name=None,
    #         slug=None,
    #         lastPublished=None,
    #         sortBy=None,
    #         sortOrder=None,
    #         live: bool = False
    # ):
    #     """
    #     List staged or live collection items.
    #
    #     :param collection_id: ID of the collection
    #     :param cmsLocaleId:   optional locale override
    #     :param offset:        result offset
    #     :param limit:         max number of items to return
    #     :param name:          filter by name
    #     :param slug:          filter by slug
    #     :param lastPublished: filter by lastPublished timestamp
    #     :param sortBy:        field to sort by
    #     :param sortOrder:     'asc' or 'desc'
    #     :param live:          if True, list live items; otherwise list staged items
    #     """
    #     # build query params, include only non-None args
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "live") and value is not None
    #     }
    #
    #     # choose endpoint path
    #     path = "items/live" if live else "items"
    #     endpoint = f"/collections/{collection_id}/{path}"
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
    #         query_params=query_params
    #     )
    """The combined method
    not tested"""

    # def get_collection_item(
    #         self,
    #         collection_id,
    #         item_id,
    #         cmsLocaleId=None,
    #         live: bool = False
    # ):
    #     """
    #     Retrieve a staged collection item or its live version.
    #
    #     :param collection_id: ID of the collection
    #     :param item_id:       ID of the item
    #     :param cmsLocaleId:   optional locale override
    #     :param live:          if True, fetch the live item; otherwise fetch the staged item
    #     """
    #     # build query params (omit None and internal args)
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "item_id", "live") and value is not None
    #     }
    #
    #     # choose endpoint based on `live` flag
    #     endpoint = f"/collections/{collection_id}/items/{item_id}"
    #     if live:
    #         endpoint += "/live"
    #
    #     return self.connector.get(
    #         endpoint=endpoint,
    #         query_params=query_params
    #     )
    """
    The individual methods followed by the combined method underneath
    Not tested
    """
    # def create_collection_items(
    #         self,
    #         collection_id,
    #         items,
    #         skipInvalidFiles: bool = True,
    #         cmsLocaleId: str = None
    # ):
    #     """
    #     Create one or more items in a collection (across multiple locales if needed).
    #
    #     :param collection_id:    ID of the collection (objectId)
    #     :param items:            A dict representing a single item, or a list of dicts for multiple items.
    #     :param skipInvalidFiles: If True (default), invalid files are skipped; if False, the request will fail on invalid files.
    #     :param cmsLocaleId:      Optional locale override (e.g. "en-US").
    #     """
    #     # Build query parameters
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "items") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #
    #     return self.connector.post(
    #         endpoint=f"/collections/{collection_id}/items",
    #         json=items,
    #         headers=headers,
    #         query_params=query_params
    #     )
    #
    # def create_live_collection_items(
    #         self,
    #         collection_id,
    #         items,
    #         skipInvalidFiles: bool = True,
    #         cmsLocaleId: str = None
    # ):
    #     """
    #     Create one or more items in a collection and immediately publish them live.
    #
    #     :param collection_id:    ID of the collection (objectId)
    #     :param items:            A dict for a single item, or a list of dicts for multiple items.
    #     :param skipInvalidFiles: If True (default), invalid files are skipped; if False, the request fails on invalid files.
    #     :param cmsLocaleId:      Optional locale override (e.g. "en-US").
    #     """
    #     # Build query parameters (omit None and internal names)
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "items") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #
    #     return self.connector.post(
    #         endpoint=f"/collections/{collection_id}/items/live",
    #         json=items,
    #         headers=headers,
    #         query_params=query_params
    #     )

    """
    The combined method
    not tested
    """

    # def create_collection_items(
    #         self,
    #         collection_id,
    #         items,
    #         skipInvalidFiles: bool = True,
    #         cmsLocaleId: str = None,
    #         live: bool = False
    # ):
    #     """
    #     Create one or more items in a collection, either staged or live.
    #
    #     :param collection_id:    ID of the collection (objectId)
    #     :param items:            A dict for a single item, or a list of dicts for multiple items.
    #     :param skipInvalidFiles: If True (default), invalid files are skipped; if False, the request fails on invalid files.
    #     :param cmsLocaleId:      Optional locale override (e.g. "en-US").
    #     :param live:             If True, items are published immediately (live); if False, items are staged.
    #     """
    #     # build query parameters (omit internal args and None values)
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "items", "live") and value is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #     path = "items/live" if live else "items"
    #
    #     return self.connector.post(
    #         endpoint=f"/collections/{collection_id}/{path}",
    #         json=items,
    #         headers=headers,
    #         query_params=query_params
    #     )


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
    #         if k not in ("self", "collection_id", "fieldData") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
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
    #         if k not in ("self", "collection_id", "item_id") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id","item_id") and value is not None
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
    #         if k not in ("self", "collection_id", "item_id") and v is not None
    #     }
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id","item_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items/{item_id}/live",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )

    """The combined method
    Not tested"""

    # def update_single_collection_item(
    #         self,
    #         collection_id,
    #         item_id,
    #         skipInvalidFiles=None,
    #         cmsLocaleId=None,
    #         isArchived=None,
    #         isDraft=None,
    #         fieldData=None,
    #         live: bool = False
    # ):
    #     """
    #     Update a staged item or its live version.
    #
    #     :param collection_id:     ID of the collection
    #     :param item_id:           ID of the item
    #     :param skipInvalidFiles:  whether to skip invalid files
    #     :param cmsLocaleId:       optional locale override
    #     :param isArchived:        mark item archived
    #     :param isDraft:           mark item as draft
    #     :param fieldData:         dict of field updates
    #     :param live:              if True, patch the live item; otherwise patch staged
    #     """
    #     # build query parameters
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "item_id", "live") and v is not None
    #     }
    #
    #     # build JSON payload
    #     payload = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "item_id", "live") and v is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #     endpoint = f"/collections/{collection_id}/items/{item_id}"
    #     if live:
    #         endpoint += "/live"
    #
    #     return self.connector.patch(
    #         endpoint=endpoint,
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
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     # same for the JSON body
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
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
    #         if k not in ("self", "collection_id") and v is not None
    #     }
    #     # same for the JSON body
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/items/live",
    #         json=payload,
    #         headers=headers,
    #         query_params=query_params
    #     )

    """The combined method
    not tested"""

    # def update_collection_items(
    #         self,
    #         collection_id,
    #         skipInvalidFiles=None,
    #         items=None,
    #         live: bool = False
    # ):
    #     """
    #     Update staged collection items or live collection items in bulk.
    #
    #     :param collection_id:      ID of the collection
    #     :param skipInvalidFiles:   whether to skip invalid files
    #     :param items:              list of item dicts to update
    #     :param live:               if True, target the live endpoint; otherwise the staged endpoint
    #     """
    #     # build query params (only include args that aren’t None)
    #     query_params = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "live") and v is not None
    #     }
    #
    #     # build JSON payload (same filtering)
    #     payload = {
    #         k: v
    #         for k, v in locals().items()
    #         if k not in ("self", "collection_id", "live") and v is not None
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #     path = "items/live" if live else "items"
    #
    #     return self.connector.patch(
    #         endpoint=f"/collections/{collection_id}/{path}",
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
    #         query_params=query_params)

    """The combined method
    not tested"""

    # def delete_single_collection_item(
    #         self,
    #         collection_id,
    #         item_id,
    #         cmsLocaleId=None,
    #         live: bool = False
    # ):
    #     """
    #     Delete a staged collection item or unpublish a live item.
    #
    #     :param collection_id: ID of the collection
    #     :param item_id:    ID of the item
    #     :param cmsLocaleId: optional locale override
    #     :param live:       if True, unpublish the live item; if False, delete the staged item
    #     """
    #     # build query params (only include cmsLocaleId if given)
    #     query_params = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id", "item_id", "live") and value is not None
    #     }
    #
    #     # choose endpoint path based on `live` flag
    #     endpoint = f"/collections/{collection_id}/items/{item_id}"
    #     if live:
    #         endpoint += "/live"
    #
    #     return self.connector.delete(
    #         endpoint=endpoint,
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
    #         headers=headers)
    # def unpublish_live_collection_items(self, collection_id, items):
    #      payload = {
    #          key: value
    #          for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #      }
    #      headers = {"Content-Type": "application/json"}
    #      return self.connector.delete(
    #          endpoint=f"/collections/{collection_id}/items/live",
    #          json=payload,
    #          headers=headers)

    """The combined method
    not tested"""

    # def delete_collection_items(self, collection_id, items, live=False):
    #     """
    #     Delete or unpublish items in a collection.
    #
    #     :param collection_id: ID of the collection
    #     :param items: list of item IDs to delete/unpublish
    #     :param live: if True, unpublish live items; if False, delete staged items
    #     """
    #     payload = {
    #         key: value
    #         for key, value in locals().items()
    #         if key not in ("self", "collection_id") and value is not None
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     path = "items/live" if live else "items"
    #
    #     return self.connector.delete(
    #         endpoint=f"/collections/{collection_id}/{path}",
    #         json=payload,
    #         headers=headers
    #     )

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
    #         headers=headers)



















    

    

