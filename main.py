from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def index():
  return {
    'data': 'Hello, World!',
  }

@app.get('/blog')
def showBlogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
  if published:
    return {
      'data': f'{limit} published blogs'
    }
  else :
    return {
      'data': f'{limit} blogs'
    }

@app.get('/blog/unpublished')
def unpublishedBlogs():
  return {
    'data': 'Unpublished blogs'
  }

@app.get("/blog/{id}")
def showBlog(id: int):
  return {
    'data': id
  }

@app.get("/blog/{id}/comments")
def showBlogComments(id: int, limit:int = 10):
  return {
    'data': f'Comments for blog {id}'
  }

class Blog(BaseModel):
  title: str
  body: str
  published: Optional[bool] = None

@app.post('/blog')
def createBlog(request: Blog):
  return {
    'data': f'Blog created with title: {request.title}',
  }

# Uncomment the following line to run the app on a specific host and port. Or to run it with the command 'python main.py'
# if __name__ == "__main__":
#   uvicorn.run(app, host="127.0.0.1", port=9000)