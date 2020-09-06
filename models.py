from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_completed = db.Column(db.DateTime)

    def __repr__(self):
      return '<Task %r>' % self.id