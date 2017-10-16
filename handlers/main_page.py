from handlers.blog_base import BlogHandler

class MainPage(BlogHandler):
  def get(self):
      self.redirect('/blog')