import requests

class BaseApiObject(object):
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session if session else requests.Session()

    def _request(self, path, max_cache_age=-1):
        r = self.session.get(f"{self.base_url}/{path}")
        if r.status_code == 200:
            return r.text
        else:
            raise RequestError(r)
