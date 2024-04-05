from fastapi import FastAPI, staticfiles, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse



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
    # file.write()
    # return {"filename": file.filename}
    try:
        with open("static/comics/images/uploaded/" + file.filename, "wb") as buffer:
            buffer.write(await file.read())
        return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Failed to upload file: {e}"})
