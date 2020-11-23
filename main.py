import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
product_ref = store.collection(u'products')

try:
    docs = product_ref.get()
    for doc in docs:
        print(u'Doc Data: {}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing Data')