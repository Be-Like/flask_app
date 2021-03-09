# import sqlite3 # Section 5 query code below
from db import db

class UserModel(db.Model):
  __tablename__ = 'users'

  # Always have to add the column names
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(80)) # 80 Characters maximum
  password = db.Column(db.String(80)) # 80 Characters maximum

  def __init__(self, username, password):
    # These properties must match the database columns if they are going to be stored in the db
    self.username = username
    self.password = password

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_username(cls, username): # username mapping
    return cls.query.filter_by(username = username).first()
    # Section 5 query code below
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()

    # query = "SELECT * FROM users WHERE username=?"
    # result = cursor.execute(query, (username,))
    # row = result.fetchone()
    # if row:
    #   # user = cls(row[0], row[1], row[2]) # row[0] = id, row[1] = username, row[2] = password
    #   user = cls(*row)
    # else:
    #   user = None

    # connection.close()
    # return user

  @classmethod
  def find_by_id(cls, _id): # userid mapping
    return cls.query.filter_by(id = _id).first()

    # Section 5 query code below
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()

    # query = "SELECT * FROM users WHERE id=?"
    # result = cursor.execute(query, (_id,))
    # row = result.fetchone()
    # if row:
    #   # user = cls(row[0], row[1], row[2]) # row[0] = id, row[2] = username, row[2] = password
    #   user = cls(*row)
    # else:
    #   user = None

    # connection.close()
    # return user
