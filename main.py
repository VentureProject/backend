from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

received_modal_data = {}

@app.post("/")
async def receive_modal_data(modal_data: dict):
    global received_modal_data
    received_modal_data = modal_data
    return {"message": "Data received successfully"}

@app.get('/photoReview')
async def get_photo_review():
    global received_modal_data
    received_modal_data['isPhotoReviewed'] = False
    received_modal_data['whyRejected'] = "전신이 나오도록 촬영해주세요"
    return received_modal_data

# uvicorn main:app --reload

# uvicorn main:app --reload
