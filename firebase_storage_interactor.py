from firebase_admin import storage

class FirebaseStorageInteractor:
  def __init__(self, path):
    self.bucket = storage.bucket(path)

  def upload_file(self, path_to_local_file, path_to_storage, type):
    file_blob = self.bucket.blob(path_to_storage)
    file_blob.upload_from_filename(path_to_local_file, type)

