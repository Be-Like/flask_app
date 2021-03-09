from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")
  parser.add_argument('store_id', type=int, required=True, help="Every item needs a store id.")

  @jwt_required()
  def get(self, name):
    item = ItemModel.find_by_name(name)
    if item:
      return item.json()
    return {'message': 'Item not found'}, 404

  def post(self, name):
    if ItemModel.find_by_name(name):
      return {'message': "An item with name '{}' already exists.".format(name)}, 400

    data = Item.parser.parse_args()
    item = ItemModel(name, data['price'], data['store_id'])

    try:
      item.save_to_db()
    except:
      return {'message': 'An error occurred inserting the item'}, 500

    return item.json(), 201

  def put(self, name):
    data = Item.parser.parse_args()

    item = ItemModel.find_by_name(name)
    # updated_item = ItemModel(name, data['price']) # Section 5 query code below

    if item is None:
      item = ItemModel(name, data['price'], data['store_id'])
      # try:
      #   updated_item.insert()
      # except:
      #   return {'message': 'An error occurred inserting the item'}, 500
    else:
      item.price = data['price']
      item.store_id = data['store_id']
      # try:
      #   # ItemModel.update(updated_item) # updates entire object (section 5)
      #   updated_item.update()
      # except:
      #   return {'message': 'An error occurred inserting the item'}, 500
    item.save_to_db()
    return item.json()

  def delete(self, name):
    item = ItemModel.find_by_name(name)
    if item:
      item.delete_from_db()

    return {'message': 'Item deleted'}
    # Section 5 query code below
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()

    # query = "DELETE FROM items WHERE name=?"
    # cursor.execute(query, (name,))

    # connection.commit()
    # connection.close()



class ItemList(Resource):
  def get(self):
    return {'items': [item.json() for item in ItemModel.query.all()]}
    # or
    # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

    # Section 5 query code below
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()

    # query = "SELECT * FROM items"
    # result = cursor.execute(query)
    # items = result.fetchall()

    # connection.commit()
    # connection.close()
    # return {'items': items}
