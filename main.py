from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.get("/posts")
def get_posts():
    return [
        {"id": 1, "title": "First Post", "content": "This is the first post"},
        {"id": 2, "title": "Second Post", "content": "This is the second post"},
    ]