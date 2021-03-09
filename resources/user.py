import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
  parser.add_argument('password', type=str, required=True, help='This field cannot be blank')

  def post(self):
    data = UserRegister.parser.parse_args()

    if UserModel.find_by_username(data['username']):
      return {'message': 'A user with that username already exists.'}, 400

    user = UserModel(**data)
    user.save_to_db()

    # Section 5 query code below
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()

    # query = "INSERT INTO users VALUES (NULL, ?, ?)"
    # cursor.execute(query, (data['username'], data['password']))

    # connection.commit()
    # connection.close()

    return {'message': 'User created successfully.'}, 201

# section 5 code moved in section 6
# class User:
#   def __init__(self, _id, username, password):
#     self.id = _id
#     self.username = username
#     self.password = password

#   @classmethod
#   def find_by_username(cls, username): # username mapping
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()

#     query = "SELECT * FROM users WHERE username=?"
#     result = cursor.execute(query, (username,))
#     row = result.fetchone()
#     if row:
#       # user = cls(row[0], row[1], row[2]) # row[0] = id, row[2] = username, row[2] = password
#       user = cls(*row)
#     else:
#       user = None

#     connection.close()
#     return user

#   @classmethod
#   def find_by_id(cls, _id): # userid mapping
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()

#     query = "SELECT * FROM users WHERE id=?"
#     result = cursor.execute(query, (_id,))
#     row = result.fetchone()
#     if row:
#       # user = cls(row[0], row[1], row[2]) # row[0] = id, row[2] = username, row[2] = password
#       user = cls(*row)
#     else:
#       user = None

#     connection.close()
#     return user
