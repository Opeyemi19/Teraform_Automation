from fastapi import FastAPI

from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World Opeyemi19"}

@app.get("/blog")
async def blog():
    return {
        "Voiture": "Hello BMW",
        "Velo": "Hello VTT"
        }

handler = Mangum(app=app)