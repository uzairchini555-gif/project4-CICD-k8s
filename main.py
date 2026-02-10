from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
	return {"message": "CD pipeline Testing again"}
@app.route("/health")
def health():
	return "ok", 200
