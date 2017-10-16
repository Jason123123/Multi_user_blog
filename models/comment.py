rom google.appengine.ext import db
from modules import *

class Comment(db.Model):
    user_id = db.IntegerProperty(required=True)
    content = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add = True)