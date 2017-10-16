from handlers.blog_base import *
from models.post import Post
import time

class DeletePost(BlogHandler):
    def get(self, post_id):
        if not self.user:
            self.redirect("/login")
        else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            if post and post.user_id == self.user.key().id():

                post.delete()
                time.sleep(0.1) ##add this line when runing on local machine to get front page refreshed
                self.redirect('/')

            else:
                self.write("You are not permitted to delete the post")