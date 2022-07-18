# mongodb+srv://awlesss:<password>@cluster0.xetnm.mongodb.net/?retryWrites=true&w=majority
import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://awlesss:GlebDasha01@cluster0.xetnm.mongodb.net/?retryWrites=true&w=majority')
db = cluster["hoopWithMe"]
collection = db['users']
post = {'_id': 3, 'name': 'gleb', 'score': 0}
#collection.insert_one(post)
collection.delete_one({'_id': 2})
results = collection.find({'name': 'gleb'})
for res in results:
    print(res)