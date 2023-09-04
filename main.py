from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()

# Allow requests from the React application (adjust origins as needed)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(question_router.router)


# uvicorn main:app --reload
