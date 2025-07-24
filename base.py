import json
import logging
import requests
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

class BaseWebflowEndpoint:
    def __init__(self, connector):
        self.connector = connector

class WebflowConnector:
    def __init__(self, token, timeout=30):
        self.token = token
        self.timeout = timeout

    def get_url(self, endpoint, query_params=None):
        base_url = "https://api.webflow.com/v2"
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        url = f"{base_url}{endpoint}"
        if query_params:
            url = f"{url}{self.get_url_query_params(query_params)}"
        return url

    def get_url_query_params(self, params):
        if not isinstance(params, dict):
            return ""
        return f"?{urlencode(params)}"

    def _get_default_headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def __getattr__(self, method_name):
        def method_handler(endpoint, json=None, **kwargs):
            upper_method = method_name.upper()
            valid_methods = ("GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS")
            if upper_method not in valid_methods:
                raise ValueError(f"Invalid HTTP method: {method_name}")

            headers = self._get_default_headers()
            if "headers" in kwargs:
                headers.update(kwargs.pop("headers"))

            if upper_method in ("POST", "PUT", "PATCH") and json:
                kwargs["json"] = json

            if "timeout" not in kwargs:
                kwargs["timeout"] = self.timeout

            query_params = kwargs.pop("query_params", None)
            url = self.get_url(endpoint, query_params)
            return self._api_call(upper_method, url, headers=headers, **kwargs)
        return method_handler

    def _api_call(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, **kwargs)
            return WebflowValidator(response).validate()
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

class WebflowValidator:
    def __init__(self, response):
        self.response = response

    def validate(self):
        if not self.response.ok:
            logger.error(f"Error {self.response.status_code}: {self.response.text}")
            self.response.raise_for_status()
        try:
            return self.response.json()
        except json.JSONDecodeError:
            if self.response.ok:
                return {"status": "success", "text": self.response.text}
            raise
