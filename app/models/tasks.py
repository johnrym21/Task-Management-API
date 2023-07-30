from app import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Integer)
    due_date = db.Column(db.Date)
    category = db.Column(db.Text)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'priority': self.priority,
            'due_date': str(self.due_date),
            'category': self.category
        }
