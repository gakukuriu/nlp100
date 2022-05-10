# インタラクティブシェルを利用する場合: db.artist.find({name: 'Queen'})

import sys, pymongo

query = sys.argv[1]
client = pymongo.MongoClient('localhost', 27017)
db = client.artist_db
co = db.artist

for data in co.find({'name': query}):
    print(data)
