import requests

from .constants import AD_STUDIO_SERVICE, IMAGE_SERVICE


def generate_image(template):
	image_service_route = AD_STUDIO_SERVICE+IMAGE_SERVICE
	try:
		requests.post(image_service_route)
	except requests.exceptions.ConnectionError:
		return