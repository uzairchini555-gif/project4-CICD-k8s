from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
	return {"Production Rolling Update Test"}
@app.get("/health")
def health():
	return {"status": "ok"}
