from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
	return {"message": "Hello from Kubernetes Project4 CI pipelien and push"}
