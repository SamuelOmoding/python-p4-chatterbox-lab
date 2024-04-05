from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize SQLAlchemy
db = SQLAlchemy()

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'  # Use double underscores for __tablename__

    # Define the columns for the Message model
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Optional: Define a method to serialize your model to a dictionary
    # This can be useful for JSON serialization in Flask routes
    def to_dict(self):
        return {
            "id": self.id,
            "body": self.body,
            "username": self.username,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
