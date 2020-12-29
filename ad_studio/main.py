import copy

from fastapi import FastAPI, File, UploadFile

from .images import generate_image
from .templates import fetch_template, update_tempalte

app = FastAPI()


@app.get("/")
def index():
	return {"message": "Hello world!"}


@app.post("/feed/",  status_code=201)
def process_feed(template_id: int, file: UploadFile = File(...)):
	# fetch template
	template = fetch_template(template_id)
	data = file.file.read().strip().decode("utf-8")
	rows = data.split("\n")
	for row in rows[1:]:
		# update template
		updated_template = update_tempalte(copy.deepcopy(template), row)
		# generate image
		image = generate_image(updated_template)
	return {"message": "Images Generated"}
