from base import WebflowConnector
from sites import WebflowSites
from cms import WebflowCMS
from tokens import WebflowToken
from forms import WebflowForms
from users import WebflowUsers
from webhooks import WebflowWebhooks
from settings import *

class Webflow:
    def __init__(self, token=None, timeout=None):
        self.token = token or "385cb88c4b5e77b411f5ce2c170c04d04c17fd0b813dca95835f99d82faf49a1"
        self.timeout = timeout or 30

        self.connector = WebflowConnector(
            token=self.token,
            timeout=self.timeout
        )

    @property
    def sites(self):
        return WebflowSites(connector=self.connector)

    @property
    def cms(self):
        return WebflowCMS(connector=self.connector)

    @property
    def tokens(self):
        return WebflowToken(connector=self.connector)

    @property
    def forms(self):
        return WebflowForms(connector=self.connector)

    @property
    def users(self):
        return WebflowUsers(connector=self.connector)

    @property
    def webhooks(self):
        return WebflowWebhooks(connector=self.connector)
