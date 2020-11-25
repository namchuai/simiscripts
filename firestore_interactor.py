import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreInteractor:
    def __init__(self, cred):
        self.cred = cred
        self.app = firebase_admin.initialize_app(cred)
        self.store = firestore.client()
    
    def add_data(self, collection_name, obj):
        collection_ref = self.store.collection(collection_name)
        collection_ref.add(obj.to_dict())

