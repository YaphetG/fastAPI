from src.models import User, Item, Post
from typing import List


class DummyService:
    """
    Class that creates some dummy data
    """
    def __init__(self):
        self.users = self.create_users(5, 'base_')
        self.items = []
        self.posts = []
        for u in self.users:
            user_id = u.id
            item_prefix = f'{user_id}_item_'
            items = self.create_items(10, item_prefix)
            post_id = f'{user_id}_post'
            self.posts.append(
               self.create_post(u, items, post_id)
            )
            self.items += items

    def create_users(self, amount, id_prefix: str = ''):
        generate_id = lambda i: f'{id_prefix}{i}'
        users = [
            User(**k) for k in [
                {'name': f'user{generate_id(i)}',
                 'email': f'user{generate_id(i)}@mail.com',
                 'id': generate_id(i)} for i in range(0, amount)
            ]
        ]
        return users

    def create_items(self, amount, id_prefix: str = ''):
        generate_id = lambda i: f'{id_prefix}{i}'
        ids = [generate_id(i) for i in range(0, amount)]
        items = [
            Item(**k) for k in [
                {
                    'id': i,
                    'name': f'item{i}',
                    'description': f'some details on item {i}',
                    'price': 0.0,
                    'tax': 0.0,
                    'tags': ['tag1', 'tag2']
                } for i in ids
            ]
        ]
        return items

    def create_post(self, user: User, items: List[Item], id):
        return Post(**{
            'id': id,
            'ownedBy': user,
            'items': items
        })

    def get_post_by_user(self, user: User):
        return list(filter(lambda post: post.ownedBy == user, self.posts))

    def get_all_users(self):
        return self.users

    def get_all_posts(self):
        return self.posts

    def get_all_items(self):
        return self.items


if __name__ == '__main__':
    dummysvc = DummyService()
    users = dummysvc.create_users(10)
    print(users)