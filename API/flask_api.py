from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

book_list = [
    {
        "id": 0,
        "author":"Luciano Ramalho",
        "title":"Fluent Python"
    },
    {
        "id": 1,
        "author":"Kenneth Reitz und Tanya Schlusser",
        "title":"The Hitchhiker's Guide to Python: Best Practices for Development"
    }
]

class Book(Resource):
    def get(self, id):
        for book in book_list:
            if(book["id"] == id):
                return book, 200
        return "Book not found", 404

    def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("title")
      params = parser.parse_args()
      for book in book_list:
          if(id == book["id"]):
              return f"Book with id {id} already exists", 400
      book = {
          "id": int(id),
          "author": params["author"],
          "title": params["title"]
      }
      book_list.append(book)
      return book, 201

    def delete(self, id):
      global book_list
      book_list = [book for book in book_list if book["id"] != id]
      return f"Book with id {id} is deleted.", 200

    def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("title")
      params = parser.parse_args()
      for book in book_list:
          if(id == book["id"]):
              book["author"] = params["author"]
              book["title"] = params["title"]
              return book, 200
      
      book = {
          "id": id,
          "author": params["author"],
          "title": params["title"]
      }
      
      book_list.append(book)
      return book, 201

api.add_resource(Book, '/books/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)