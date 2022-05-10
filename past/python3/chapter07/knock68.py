import sys, pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.artist_db
co = db.artist

for data in co.find({'tags.value': 'dance'}, {'name': 1, '_id':0}).sort('rating.value', pymongo.DESCENDING).limit(10):
    print(data['name'])
