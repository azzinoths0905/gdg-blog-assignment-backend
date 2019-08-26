from store.database import Store


class UserTable(Store):
    pass


class PostTable(Store):
    pass


class Blog(object):
    post_table = PostTable('sqlite')

    def query_post_by_user(self, username: str) -> list:
        return self.__meta2post(Blog.post_table[f'author={username}'])

    def query_all(self) -> list:
        return self.__meta2post(Blog.post_table["*"])

    @staticmethod
    def __meta2post(meta_posts: list) -> list:
        posts = []
        for meta_post in meta_posts:
            posts.append(Post(
                meta_post.id,
                meta_post.key,
                meta_post.title,
                meta_post.content,
                meta_post.author,
            ))
        return posts


class Post(object):
    def __init__(self, title: str, content: str, author: str = "", id: int = "", key: str = ""):
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.key = key


class User(object):
    user_table = UserTable('sqlite')
    post_table = PostTable('sqlite')

    def __init__(self, username: str, password: str, new_user: bool = False):
        self.username = username
        self.__password = password

        if new_user:
            self.__sign_up()

        if not self.__validate():
            raise PermissionError()

    def add_post(self, post: Post):
        User.post_table.add({
            'title': post.title,
            'content': post.content,
            'author': self.username,
        })

    def __sign_up(self):
        User.user_table[self.username] = self.__password

    def __validate(self) -> bool:
        return User.user_table[self.username] and User.user_table[self.username].value == self.__password


if __name__ == "__main__":
    admin = User('admin', 'admin', True)
    blog = Blog()
    admin.add_post(
        Post('这是另一篇入门教程', '1. docker 简介\n2. docker 架构\n3. docker 命令基础\n...'))
    posts = blog.query_post_by_user('admin')
    print(posts)
    print('.......')
    posts = blog.query_all()
    print(posts)
