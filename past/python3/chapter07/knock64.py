import sys, pymongo, json

with open(sys.argv[1], 'r') as rf:
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_db
    co = db.artist
    for line in rf:
        co.insert_one(json.loads(line))
    co.create_index([('name', pymongo.ASCENDING)])
    co.create_index([('aliases.name', pymongo.ASCENDING)])
    co.create_index([('tags.value', pymongo.ASCENDING)])
    co.create_index([('rating.value', pymongo.ASCENDING)])
