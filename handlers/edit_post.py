from handlers.blog_base import *
from models.post import Post

class EditPost(BlogHandler):
    def get(self, post_id):
        if not self.user:
            self.redirect("/login")
        else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            if post and post.user_id == self.user.key().id():
                self.render('editpost.html', subject=post.subject, content=post.content, post_id=post_id)

            else:
                self.write("You are not permitted to edit the post")


    def post(self, post_id):
        if not self.user:
            self.redirect('/blog')
            return

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user_id:
            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)

                post.subject = subject
                post.content = content

                post.put()

                self.redirect('/blog/%s' % str(post.key().id()))
            else:
                error = "subject and content, please!"
                self.render("newpost.html", subject=subject,
                            content=content, error=error)

        else:
            self.write("You cannot edit this post becuase you are not the one who wrote this post.")
