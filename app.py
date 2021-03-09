from flask import Flask # request (was used in section 4)
from flask_restful import Api # Resource, reqparse (was used in section 4)
from flask_jwt import JWT # jwt_required (was used in section 4)

from db import db
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQL Alchemy track modification is better than the flask
app.secret_key = 'jake'
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

db.init_app(app)

if __name__ == '__main__':
  app.run(port=5000, debug=True)

# What was in section 4
# items = []

# class Item(Resource):
#   parser = reqparse.RequestParser()
#   parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")

#   @jwt_required()
#   def get(self, name):
#     item = next(filter(lambda x: x['name'] == name, items), None)
#     return {'item': item}, 200 if item else 404

#   def post(self, name):
#     if next(filter(lambda x: x['name'] == name, items), None) is not None:
#       return {'message': "An item with name '{}' already exists.".format(name)}, 400

#     data = Item.parser.parse_args()

#     item = {
#       'name': name,
#       'price': data['price']
#     }
#     items.append(item)
#     return item, 200

#   def put(self, name):
#     data = Item.parser.parse_args()

#     item = next(filter(lambda x: x['name'] == name, items), None)
#     if item is None:
#       item = {'name': name, 'price': data['price']}
#       items.append(item)
#     else:
#       item.update(data) # updates entire object
#     return item

#   def delete(self, name):
#     global items
#     items = list(filter(lambda x: x['name'] != name, items))
#     return {'message': 'Item deleted'}

# class ItemList(Resource):
#   def get(self):
#     return {'items': items}

