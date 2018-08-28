""" Models and database functions for Hangman game project. """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

######################################################################
# Model definitionsgc

class User(db.Model):
    """User of Hangman game website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<User: name={} => email={}>".format(self.name, self.email)

class Score(db.Model):
    """Game details on Hangman game website."""
    
    __tablename__ = "scores"

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    #Tie together Score and User here. Use pk for User which is user_id.
    # user = db.relationship("User",
    #                             backref=db.backref("user", order_by=user_id))

    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<Score: score={} => for user_id{}".format(self.score, self.user_id)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hangman'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

# def example_data():
#     """Create some sample data.""" 


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."

