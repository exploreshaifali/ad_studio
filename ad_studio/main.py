from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello world!"}


@app.post("/feed/")
def process_feed(template_id: int, file: UploadFile = File(...)):
	# fetch template
	data = file.file.read().strip()
	# update template
	# generate image
	pass