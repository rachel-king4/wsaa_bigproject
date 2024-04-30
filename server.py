# flask server that links to the Player DAO
# author: Rachel King

from flask import Flask, request, jsonify, abort
from playerDAO import playerDAO

app = Flask(__name__, static_url_path='', static_folder='.')

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
        if not request.json:
                abort(400)
        
        # other checking 
        player = {
                "name": request.json['name'],
                "age": request.json['age'],
                "nationality": request.json['nationality'],
                "club": request.json['club'],
        }
        
        return jsonify(playerDAO.create(player))

# update
# curl -X PUT -d "{\"name\":\"Roy Keane\", \"age\":25, \"nationality\":\"Irish\"}" http://XXX.X.X.X:XXXX/players/1

@app.route('/players/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        player = {}

        if "name" in jsonstring:
                player["name"] = jsonstring["name"]
        if "age" in jsonstring:
                player["age"] = jsonstring["age"]
        if "nationality" in jsonstring:
                player["nationality"] = jsonstring["nationality"]
        if "club" in jsonstring:
                player["club"] = jsonstring["club"]
        
        return jsonify(playerDAO.update(id, player))

# Delete
# curl -X DELETE  http://XXX.X.X.X:XXXX/players/1

@app.route('/players/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(playerDAO.delete(id))


# getall clubs
# curl http://XXX.X.X.X:XXXX/players

@app.route('/clubs', methods=['GET'])
def getallclubs():
        return jsonify(playerDAO.getAllClubs())

#create club
#curl -X POST -d "{\"name\":\"Roy Keane\", \"age\":25, \"nationality\":\"Irish\"}" http://XXX.X.X.X:XXXX/clubs
@app.route('/clubs', methods=['POST'])
def createclub():
        if not request.json:
                abort(400)
        
        # other checking 
        club = {
                "name": request.json['name'],
                "number_of_trophies_won": request.json['number_of_trophies_won'],
                "country": request.json['country'],
        }
        
        return jsonify(playerDAO.createClub(club))

# find club by id
# curl http://XXX.X.X.X:XXXX/clubs/1

@app.route('/clubs/<int:id>', methods=['GET'])
def findClubbyid(id):
        return jsonify(playerDAO.findClubByID(id))

# Delete club
# curl -X DELETE  http://XXX.X.X.X:XXXX/clubs/1

@app.route('/clubs/<int:id>', methods=['DELETE'])
def deleteclub(id):
        return jsonify(playerDAO.deleteClub(id))


if __name__ == "__main__":
    app.run(debug = True)