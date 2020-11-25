import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from firestore_interactor import FirestoreInteractor
from model.product import Product
from excel_interactor import ExcelInteractor

cred = credentials.Certificate("./ServiceAccountKey.json")

my_firestore = FirestoreInteractor(cred)
my_excel = ExcelInteractor('./sample_data/sample_product_list.xlsx')
productList = my_excel.test()

print(productList[0].__dict__)

# myfsinteractor.add_data(u'products', dummy_product)

#.add_data(dummy_product)
# app = firebase_admin.initialize_app(cred)

# store = firestore.client()
# product_ref = store.collection(u'products')

# try:
#     docs = product_ref.get()
#     for doc in docs:
#         print(u'Doc Data: {}'.format(doc.to_dict()))
# except google.cloud.exceptions.NotFound:
#     print(u'Missing Data')