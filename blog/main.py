from fastapi import FastAPI

from blog.database import create_db_and_tables
from blog.routers import blog_router, user_router

app = FastAPI()

app.include_router(blog_router)
app.include_router(user_router)

@app.on_event("startup")
def on_startup():
  create_db_and_tables()