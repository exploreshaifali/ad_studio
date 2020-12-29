import requests

from .constants import AD_STUDIO_SERVICE, TEMPLATE_SERVICE_WITH_ID


DEFAULT_TEMPLATE = {
					"objects": [
						{
							"type": "image",
							"width": 350,
							"height": 300,
							"x": 300,
							"y": 300,
							"url": "https://tinyurl.com/o5rkr73"
						},
						{
							"type": "textbox",
							"width": 300,
							"height": 100,
							"x": 400,
							"y": 300,
							"text": "Now at $50"
						}
					],
					"width": 600,
					"height": 600,
					}

def fetch_template(template_id):
	template_service_route = AD_STUDIO_SERVICE+TEMPLATE_SERVICE_WITH_ID+str(template_id)
	try:
		template_data = requests.get(template_service_route)
	except requests.exceptions.ConnectionError:
		return DEFAULT_TEMPLATE
	return template_data


def update_tempalte(template, feed_data):
	# update image url
	row = feed_data.split(",")
	template['objects'][0]['url'] = row[-1]
	#update price
	if row[1] != "":
		template['objects'][1]['text'] = "Now at $"+str(row[1])
	else:
		template['objects'].pop()
	print(template)
	return template