#!/usr/bin/python3

import os
import re
import random
import requests
import time

from bs4 import BeautifulSoup as bs
from itertools import cycle
#from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry
#from requests_toolbelt import sessions
#from requests_toolbelt.utils import dump

import settings

class UserAgent():

	def __init__(self):
		self.base = settings.BASE
		self.sub = settings.SUB
		self.page = settings.PAGE
		self.browsers = settings.BROWSERS

	def get_random_url(self):
		self.browser = random.choice(self.browsers)
		self.url = "".join([self.base, self.sub, self.browser, self.page])

	def get_soup_object(self):
		r = requests.get(self.url)
		soup = bs(r.content, "html.parser")
		self.soup = soup

	def get_page_count(self):
		pagination = self.soup.find("div", id="pagination")
		pages = [link.get_text() for link in pagination.find_all("a")]
		pages = [re.sub(r'[^0-9]', "", page) for page in pages]
		self.pages = pages

	def get_user_agents(self):
		results = self.soup.find("table", class_="table").tbody.find_all("tr")
		user_agents = set()
		for page in self.pages:
			for result in results:
				rows = result.find_all("td")
				if not rows[3].get_text().lower().startswith("comp"):
					continue
				user_agent = rows[0].get_text()
				user_agents.add(user_agent)
			self.page = page 
			self.url = "".join([self.base, self.sub, self.browser, self.page])
			soup = self.get_soup_object()
		self.user_agents = user_agents

	def get_random_user_agent(self):
		user_agent_pool = cycle(self.user_agents)
		self.user_agent_pool = user_agent_pool

	def get_next_user_agent(self):
		user_agent = next(self.user_agent_pool)
		return user_agent

# a = UserAgent(settings.BASE, settings.SUB, settings.PAGE, settings.BROWSERS)
# a.get_random_url()
# a.get_soup_object()
# a.get_page_count()
# a.get_user_agents()
# a.get_random_user_agent()
# user_agent = a.get_next_user_agent()
# print(user_agent)