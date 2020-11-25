import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreInteractor:
    def __init__(self, cred):
        self.cred = cred
        self.app = firebase_admin.initialize_app(cred)
        self.store = firestore.client()
    
    def add_data(self, collection_name, obj):
        collection_ref = self.store.collection(collection_name)
        collection_ref.add(obj.__dict__)

    def delete_collection(self, coll_name, batch_size):
      docs = self.store.collection(coll_name).limit(batch_size).stream()
      deleted = 0

      for doc in docs:
          print(f'Deleting doc {doc.id} => {doc.to_dict()}')
          doc.reference.delete()
          deleted = deleted + 1

      if deleted >= batch_size:
          return self.delete_collection(coll_name, batch_size)

