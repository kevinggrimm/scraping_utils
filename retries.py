import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import settings

class SessionRetries(Retry):
	'''

	'''
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.retries = settings.RETRIES
		self.backoff_factor = settings.BACKOFF_FACTOR
		self.method_whitelist = settings.METHOD_WHITELIST
		self.status_forcelist = settings.STATUS_FORCELIST
		self.max_retries = Retry(
				total=self.retries,
				connect=self.retries,
				read=self.retries,
				method_whitelist=self.method_whitelist,
				status_forcelist=self.status_forcelist,
				backoff_factor=self.backoff_factor
			)
# http = requests.Session()
# retries = SessionRetries()
# adapter TimeOutHTTPAdapter(timeout)