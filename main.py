import uvicorn

from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)


@app.get("/")
def home():
    return [{"id": "0", "name": "HP"}, {"id": "1", "name": "DELL"}]


@app.post("/print_file")
async def print_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
