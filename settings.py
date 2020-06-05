## adapter.py
DEFAULT_TIMEOUT=5

## retries.py
RETRIES = 5
BACKOFF_FACTOR = 1
METHOD_WHITELIST = ["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"]
STATUS_FORCELIST = [413, 429, 500, 502, 503, 504]

## user_agents
BASE = "https://developers.whatismybrowser.com" 
SUB = "/useragents/explore/software_name/"
PAGE_NUM= "/1"
BROWSERS = ['opera', 'chrome', 'firefox', 'internet-explorer', 'safari']