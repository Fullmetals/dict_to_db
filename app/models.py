from app import db

class Vocabulary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    part_of_speech = db.Column(db.String(50), nullable=False)
    definition = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Vocabulary(word='{self.word}', part_of_speech='{self.part_of_speech}', definition='{self.definition}')>"