import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from firebase_storage_interactor import FirebaseStorageInteractor
from firestore_interactor import FirestoreInteractor

class FirebaseEntrance:
  STORAGE_PATH_KEY = 'firebase_storage_root_path'
  FIREBASE_CONFIG_FILE_KEY = 'firebase_config_file'

  def __init__(self):
    self.firebase_keys = {}
    self.env = open('.env', 'r')

    for line in self.env:
      name, var = line.partition('=')[::2]
      self.firebase_keys[name.strip()] = var

    cred = credentials.Certificate("ServiceAccountKey.json")#self.firebase_keys[self.FIREBASE_CONFIG_FILE_KEY])
    self.firestore = FirestoreInteractor(cred)
    #self.storage = FirebaseStorageInteractor(self.firebase_keys[self.STORAGE_PATH_KEY])

  def push_to_firestore(self, firestore_path, map_data):
    self.firestore.add_data(firestore_path, map_data)

  def upload_file(self, local_file_path, server_path, mime_type):
    pass
    #self.storage.upload_file(local_file_path, server_path, mime_type)

  def delete_collection(self, collection):
    self.firestore.delete_collection(collection, 500)
