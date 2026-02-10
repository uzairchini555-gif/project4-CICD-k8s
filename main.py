from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
	return {"message": "CD pipeline Testing again"}
@app.get("/health")
def health():
	return {"status": "ok"}
