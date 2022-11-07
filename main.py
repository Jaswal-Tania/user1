from user import User
from post import Post

user_one = User("nn@nn.com", "Tania Jaswal", "password", "student")
user_one.get_user_info()

user_two = User("nn@nn.com", "Emily P", "password2", "CEO")
user_two.get_user_info()

new_post = Post("Hello!", user_two.name)
new_post.get_post_info()