from fastapi import FastAPI
from DoItList.Users.router import router as users_router
app = FastAPI(title='ToDo App')


app.include_router(users_router)
