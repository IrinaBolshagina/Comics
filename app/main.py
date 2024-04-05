from fastapi import FastAPI, staticfiles, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware




class TripOptions(BaseModel):
    current_session: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow requests from specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.mount("/upload", staticfiles.StaticFiles(directory="static", html=True), name="static")
app.mount("/comics", staticfiles.StaticFiles(directory="static/comics", html=True), name="comics")

@app.post("/test")
async def read_root(trip_options: TripOptions):
    print("text")
    return {"current_session": trip_options.current_session}

@app.post("/images")
async def images(file: UploadFile):
    return {"filename": file.filename}