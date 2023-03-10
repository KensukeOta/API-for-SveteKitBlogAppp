from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import users, posts

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://sveltekit-blogapp-kensuke.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
