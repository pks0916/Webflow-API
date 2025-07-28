from base import BaseWebflowEndpoint
class Webflowforms:
    def list_forms(self, site_id, limit=None, offset=None):
        """
        Returns a list of forms configured on the given Webflow site.
        Supports optional pagination with `limit` and `offset`.

        https://developers.webflow.com/data/reference/forms/forms/list
        """

        # Build query params just like your previous function format
        query_params = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        return self.connector.get(
            endpoint=f"sites/{site_id}/forms",
            query_params=query_params
        )
    
    def get_form_schema(self, form_id):
        """
        Retrieves the full schema and configuration of a specific form.
        Includes field definitions, redirect settings, and metadata.
        https://developers.webflow.com/data/reference/forms/forms/get
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint=f"forms/{form_id}",
            headers=headers
        )
    
    def list_form_submissions(self, form_id, limit=None, offset=None):
        """
        Retrieves a list of submissions for a given form.
        Supports pagination with optional `limit` and `offset` query parameters.

        https://developers.webflow.com/data/reference/forms/form-submissions/list-submissions
        
        """

        query_params = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "form_id") and value is not None
        }

        return self.connector.get(
            endpoint=f"forms/{form_id}/submissions",
            query_params=query_params
        )
    

    def get_form_submission(self, form_submission_id):
        """
        Retrieves a specific form submission by its ID.
        https://developers.webflow.com/data/reference/forms/form-submissions/get-submission
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.get(
            endpoint=f"form_submissions/{form_submission_id}",
            headers=headers
        )
    

    def list_site_form_submissions(self,
                                site_id,
                                element_id=None,
                                limit=None,
                                offset=None):
        """
        Returns a list of form submissions for a specific Webflow site.
        Optional filters include form element ID, limit, and pagination offset.

        https://developers.webflow.com/data/reference/forms/form-submissions/list-submissions-by-site
        """

        query_params = {
            key: value
            for key, value in locals().items()
            if key not in ("self", "site_id") and value is not None
        }

        return self.connector.get(
            endpoint=f"sites/{site_id}/form_submissions",
            query_params=query_params
        )
    
    def modify_form_submission(self,
                                form_submission_id,
                                formSubmissionData=None):
        """
        Updates hidden fields on a form submission.
        Only predefined hidden fields from the form schema can be modified.
        https://developers.webflow.com/data/reference/forms/form-submissions/update-submission
        """

        payload = {
            "formSubmissionData": formSubmissionData
        }

        # Remove keys where value is None
        payload = {k: v for k, v in payload.items() if v is not None}

        headers = {"Content-Type": "application/json"}

        return self.connector.patch(
            endpoint=f"form_submissions/{form_submission_id}",
            json=payload,
            headers=headers
        )
    

    def delete_form_submission(self, form_submission_id):
        """
        Deletes a specific form submission by its ID.

        https://developers.webflow.com/data/reference/forms/form-submissions/delete-submission
        """

        headers = {"Content-Type": "application/json"}

        return self.connector.delete(
            endpoint=f"form_submissions/{form_submission_id}",
            headers=headers
        )



    


    



    



    

    

    

    
