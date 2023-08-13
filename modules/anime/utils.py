import json
from datetime import datetime
from collections import defaultdict

from django import template
from django.utils import timezone
import requests

register = template.Library()

class GetSchedule:
	def __init__(self):
				# anilist API backend URL
		self.url = "https://graphql.anilist.co"

		# GraphQL Query for anime schedule
		self.gql = """query (
				$weekStart: Int,
				$weekEnd: Int,
				$page: Int,
		){
			Page(page: $page) {
				pageInfo {
						hasNextPage
						total
				}
				airingSchedules(
						airingAt_greater: $weekStart
						airingAt_lesser: $weekEnd
				) {
					id
					episode
					airingAt
					timeUntilAiring
					media { title { userPreferred } }
					media { status }
				}
			}
		}"""

	def arrange_template(self, data):
		''' Convert JSON data from iter_schedule to Python dictionary format. '''
		template = []

		for airing in data[::1]:
			datetime_object = datetime.fromtimestamp(airing.get("airingAt", 0))
			template.append({
				"name": airing.get("media", {}).get("title", {}).get("userPreferred"),
				"episode": airing.get('episode', 0), 
				"date": format(datetime_object, "%b. %d, %A"), 
				"time": format(datetime_object, "%X"),
			})

		return template

	def iter_schedule(self, unix_time: int):
		''' Getting anime schedule via Anilist using their GraphQL API. '''
		page = 1
		data = {} # Empty dict for storing temp data

		query = self.gql
		week_start = unix_time	# current date
		week_end = unix_time + 24 * 7 * 60 * 60 # date for 7 days from today

		# Getting JSON data from Anilis GraphQL API
		while data.get("pageInfo", {}).get("hasNextPage", True): # Loop until there is no more anime schedule on the API return
			schedule_data = requests.post(
				self.url,
				json = {
					"query": query,
					"variables": {
						"weekStart": week_start,
						"weekEnd": week_end,
						"page": page
					}
				}
			)

			data = schedule_data.json().get("data", {}).get("Page", {})
			page += 1

			yield from data.get("airingSchedules", [])

	def get_schedule_data(self, unix_time: int):
		return self.arrange_template(list(self.iter_schedule(unix_time)))

def anime_schedule():
	unix_time = int(timezone.now().timestamp())
	schedule = GetSchedule()
	schedule_data = schedule.get_schedule_data(unix_time)
	print(schedule_data)
	return schedule_data