from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
 

class Client2Mongo:
    
    def __init__(self, host='localhost', port=27017, db_name='Ping_Pong', username='TODO', password=None):
        try:
            if username and password:
                uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}"
                self.client = MongoClient(uri)
            else:
                self.client = MongoClient(host, port)
            self.db = self.client[db_name]
        except ConnectionFailure as e:
            print("Erreur de connexion à la base de données MongoDB:", e)

    def close(self):
        if self.client:
            self.client.close()
            print("Déconnexion de MongoDB")
    """
    def trouver_tous_documents(self, collection_name):
        collection = self.db[collection_name]
        documents = collection.find()
        for doc in documents:
            print(doc)

    def trouver_un_document(self, collection_name, query):
        collection = self.db[collection_name]
        document = collection.find_one(query)
        print(document)
    """   

