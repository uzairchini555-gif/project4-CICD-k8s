from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
	return {"message": "Hello from Kubernetes Project 3 - Updated again"}
