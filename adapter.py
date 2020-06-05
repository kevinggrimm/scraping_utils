import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import settings
from retries import SessionRetries

class TimeoutHTTPAdapter(HTTPAdapter):
	'''

	'''
	def __init__(self, *args, **kwargs):
		'''

		'''
		self.timeout = settings.DEFAULT_TIMEOUT
		if "timeout" in kwargs:
			self.timeout = kwargs.get("timeout")
			del kwargs["timeout"]
		super().__init__(*args, **kwargs)
		self.max_retries = SessionRetries().max_retries

	def send(self, request, **kwargs):
		'''
		
		'''
		timeout = kwargs.get("timeout")
		if timeout is None:
			kwargs["timeout"] = self.timeout
		return super().send(request, **kwargs)


# http = requests.Session()
# adapter = TimeoutHTTPAdapter()
# print(dir(adapter.max_retries))
# print()
# print('Backoff factor: ', adapter.max_retries.backoff_factor)
# print('Method whitelist: ', adapter.max_retries.method_whitelist)