# flask server that links to the Player DAO
# author: Rachel King

from flask import Flask, request, jsonify, abort
from playerDAO import playerDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# getall
# curl http://XXX.X.X.X:XXXX/players

@app.route('/players', methods=['GET'])
def getall():
        return jsonify(playerDAO.getAll())

# find by id
# curl http://XXX.X.X.X:XXXX/players/1

@app.route('/players/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(playerDAO.findByID(id))

#create
#curl -X POST -d "{\"name\":\"Roy Keane\", \"age\":25, \"nationality\":\"Irish\"}" http://XXX.X.X.X:XXXX/players
@app.route('/players', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        player = {}

        if "name" not in jsonstring:
                abort(403)
        player["name"] = jsonstring["name"]
        if "age" not in jsonstring:
                abort(403)
        player["age"] = jsonstring["age"]
        if "nationality" not in jsonstring:
                abort(403)
        player["nationality"] = jsonstring["nationality"]
        
        return jsonify(playerDAO.create(player))

# update
# curl -X PUT -d "{\"name\":\"Roy Keane\", \"age\":25, \"nationality\":\"Irish\"}" http://XXX.X.X.X:XXXX/players/1

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        book = {}

        if "title" in jsonstring:
                book["title"] = jsonstring["title"]
        if "author" in jsonstring:
                book["author"] = jsonstring["author"]
        if "price" in jsonstring:
                book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.update(id, book))

# Delete
# curl -X DELETE  http://XXX.X.X.X:XXXX/players/1

@app.route('/players/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(playerDAO.delete(id))


if __name__ == "__main__":
    app.run(debug = True)