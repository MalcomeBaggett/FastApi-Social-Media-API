from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "First Post", "content": "This is the first post", "id": 1},
    {"title": "Second Post", "content": "This is the second post", "id": 2},
]


def find_post(post_id):
    for post in my_posts:
        if post["id"] == post_id:
            return post
    return None


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_post(new_post: Post):

    # if you ever need to convert a pydantic model to a dictionary, you can use the .dict() method
    post_dict = new_post.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": f"{post_dict} is created successfully"}


# title str, content str


@app.get("/posts/{post_id}")
def get_posts(post_id: int):
    post = find_post(post_id)
    if post:
        return {"data": post}
    return {"data": "Post not found"}
