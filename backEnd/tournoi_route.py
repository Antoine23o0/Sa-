from flask import Blueprint, jsonify, request
from mongo_client import Client2Mongo

tournois_bp = Blueprint('tournois', __name__)
client = Client2Mongo()
db_tournoi = client.db['tournoi']

@tournois_bp.route('/', methods=['GET'])
def liste_tournois():
    tournois = db_tournoi.find()
    tournois_dict = [{**tournoi, '_id': str(tournoi['_id'])} for tournoi in tournois]
    return jsonify(tournois_dict)

@tournois_bp.route('/<string:id>', methods=['GET'])
def trouve_tournoi(id):
    tournoi_trouve = db_tournoi.find_one(id)
    if tournoi_trouve:
        return jsonify(tournoi_trouve)
    else:
        return jsonify({'error': 'Tournoi non trouvé'})

@tournois_bp.route('/ajouter_tournoi', methods=['POST'])
def ajouter_nouveau_tournoi():
    tournoi = request.json
    resultat = db_tournoi.insert_one(tournoi)

    if resultat.inserted_id:
        return jsonify({"id_insertion": str(resultat.inserted_id)})
    else:
        return jsonify({"message": "Erreur lors de l'insertion"})


@tournois_bp.route('/<string:id>', methods=['DELETE'])
def supprimer_tournoi(id):
    resultat = db_tournoi.delete_one({'_id': id})
    if resultat.deleted_count:
        return jsonify({"message": "Tournoi supprimé avec succès"})
    else:
        return jsonify({'error': 'Tournoi non trouvé'})


@tournois_bp.route('/<string:id>', methods=['PUT'])
def modifier_tournoi(id):
    tournoi_modifie = request.json
    resultat = db_tournoi.update_one({'_id': id}, {'$set': tournoi_modifie})
    
    if resultat.modified_count:
        return jsonify({"message": "Tournoi modifié avec succès"})
    else:
        return jsonify({"message": "Erreur lors de la modification du tournoi"})
