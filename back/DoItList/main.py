from fastapi import FastAPI
from DoItList.Users.router import router as users_router

app = FastAPI(title='ToDo App')
from fastapi.middleware.cors import CORSMiddleware

app.include_router(users_router)

origins = ['http://localhost:3000',
           'http://localhost',
           'http://localhost:8080']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
