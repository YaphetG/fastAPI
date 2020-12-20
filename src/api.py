from src.dummyService import DummyService
from src.models import *
from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title='Some awesome api 🎉😒🐱‍👤'
)
dummy_svc = DummyService()



@app.get(
    '/all_users',
    response_model=List[User],
    description= 'Returns all users',
    summary='👩👨🧑'
)
def get_all_users():
    users = dummy_svc.get_all_users()
    return users


@app.get(
    '/all_items',
    description= 'Returns all items',
    response_model=List[Item],
    summary='🎂🍔🌭'
)
def get_all_items():
    return dummy_svc.get_all_items()


@app.get(
    '/all_posts',
    description='Returns all posts',
    response_model=List[Post],
    summary='🤳'
)
def get_all_items():
    return dummy_svc.get_all_posts()


@app.post(
    '/get_post_by_user',
    description='Returns a post by a single user',
    response_model=List[Post],
    summary='(👩 or 🧑) x 🤳'
)
def get_post_by_user(user: User):
    return dummy_svc.get_post_by_user(user)


if __name__ == '__main__':
    uvicorn.run(
        'src.api:app',
        port=9090,
        host='0.0.0.0',
        reload=True
    )




