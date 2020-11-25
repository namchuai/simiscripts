import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from firestore_interactor import FirestoreInteractor
from model.product import Product
from excel_interactor import ExcelInteractor
from firebase_storage_interactor import FirebaseStorageInteractor

my_vars = {}

with open(".env") as env:
  for line in env:
    name, var = line.partition("=")[::2]
    my_vars[name.strip()] = var

if (len(my_vars) == 0):
  print(".env file is not exists or not well-formated! Exiting..")
  exit()

print(my_vars)

# cred = credentials.Certificate("./ServiceAccountKey.json")
# firebase_admin.initialize_app(cred)
# # my_firestore = FirestoreInteractor(cred)
# # my_excel = ExcelInteractor('./sample_data/sample_product_list.xlsx')
# # productList = my_excel.test()

# my_storage.upload_file('./sample_data/sample_product_list.xlsx', 'test/test', None)


# for product in productList:
#   print(u'Creating product {}'.format(product.n))
#   my_firestore.add_data(u'products', product)

# my_firestore.delete_collection(u'products', 100)

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