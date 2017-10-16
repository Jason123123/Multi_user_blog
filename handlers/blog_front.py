from handlers.blog_base import BlogHandler
from models.post import Post

class BlogFront(BlogHandler):
    def get(self):
        posts = greetings = Post.all().order('-created')
        self.render('front.html', posts = posts)