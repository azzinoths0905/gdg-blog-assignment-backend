from blog import Blog


def all():
    posts = Blog().query_all()
    return [
        {
            'id': post.id,
            'key': post.key,
            'title': post.title,
            'author': post.author,
            'content': post.content
        } for post in posts
    ]
