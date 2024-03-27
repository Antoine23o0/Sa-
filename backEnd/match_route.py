from flask import Blueprint, jsonify, request
from mongo_client import Client2Mongo

matchs_bp = Blueprint('matchs', __name__)
client = Client2Mongo()
db_match = client.db['match']

@matchs_bp.route('/', methods=['GET'])
def liste_matchs():
    matchs = db_match.find()
    matchs_dict = [{**match, '_id': str(match['_id'])} for match in matchs]
    return jsonify(matchs_dict)

@matchs_bp.route('/<string:id>', methods=['GET'])
def trouve_match(id):
    match_trouve = db_match.find_one(id)
    if match_trouve:
        return jsonify(match_trouve)
    else:
        return jsonify({'error': 'Match non trouvé'})

@matchs_bp.route('/ajouter_match', methods=['POST'])
def ajouter_nouveau_match():
    match = request.json
    resultat = db_match.insert_one(match)

    if resultat.inserted_id:
        return jsonify({"id_insertion": str(resultat.inserted_id)})
    else:
        return jsonify({"message": "Erreur lors de l'insertion"})

@matchs_bp.route('/<string:id>', methods=['DELETE'])
def supprimer_match(id):
    match_trouve = db_match.find_one_and_delete({'_id': id})
    if match_trouve:
        return jsonify({"message": "Match supprimé avec succès"})
    else:
        return jsonify({'error': 'Match non trouvé'})

@matchs_bp.route('/<string:id>', methods=['PUT'])
def modifier_match(id):
    match_modifie = request.json
    resultat = db_match.update_one({'_id': id}, {'$set': match_modifie})
    
    if resultat.modified_count:
        return jsonify({"message": "Match modifié avec succès"})
    else:
        return jsonify({"message": "Erreur lors de la modification du match"})
