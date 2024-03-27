from flask import Blueprint, jsonify, request
from mongo_client import Client2Mongo

joueurs_bp = Blueprint('joueurs', __name__)

client = Client2Mongo()

@joueurs_bp.route('/', methods=['GET'])

def liste_joueurs():
    try:
        joueurs = client.db['joueur'].find()
        joueurs_dict = [{**joueur, '_id': str(joueur['_id'])} for joueur in joueurs]
        return jsonify(joueurs_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    

@joueurs_bp.route('/<string:id>', methods=['GET'])

def trouve_joueur(id):
    try:
        joueur_trouve = client.db['joueur'].find_one(id)
        if joueur_trouve:
            joueur_trouve['_id'] = str(joueur_trouve['_id'])
            return jsonify(joueur_trouve)
        else:
            return jsonify({'error': 'Joueur non trouvé'})
    except Exception as e:
        return jsonify({'error': str(e)})

@joueurs_bp.route('/ajouter_joueur', methods=['POST'])

def ajouter_nouveau_joueur():
    try:
        joueur = request.json
        resultat = client.db['joueur'].insert_one(joueur)
        if resultat.inserted_id:
            return jsonify({"id_insertion": str(resultat.inserted_id)})
        else:
            return jsonify({"message": "Erreur lors de l'insertion"})
    except Exception as e:
        return jsonify({'error': str(e)})

@joueurs_bp.route('/<string:id>', methods=['DELETE'])

def supprimer_joueur(id):
    try:
        resultat = client.db['joueur'].find_one_and_delete({'_id': id})
        if resultat:
            return jsonify({"message": "Joueur supprimé avec succès"})
        else:
            return jsonify({'error': 'Joueur non trouvé'})
    except Exception as e:
        return jsonify({'error': str(e)})

@joueurs_bp.route('/<string:id>', methods=['PUT'])
def modifier_joueur(id):
    try:
        joueur_modifie = request.json
        resultat = client.db['joueur'].update_one({'_id': id}, {'$set': joueur_modifie})
        if resultat.modified_count:
            return jsonify({"message": "Joueur modifié avec succès"})
        else:
            return jsonify({"message": "Erreur lors de la modification du joueur"})
    except Exception as e:
        return jsonify({'error': str(e)})
