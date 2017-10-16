from google.appengine.ext import db
from modules import *
from models.user import User

class Post(db.Model):
    user_id = db.IntegerProperty(required=True)
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        u = User.by_id(self.user_id)
        user_name = u.name
        return render_str("post.html", p = self, user_name = user_name)
