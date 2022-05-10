import sys, plyvel, json, pickle

with open(sys.argv[1], 'r') as rf:
    artist_db = plyvel.DB(sys.argv[2], create_if_missing=True)
    for line in rf:
        info = json.loads(line)
        artist_db.put((info.get('name', 'N/A')).encode('utf-8'), pickle.dumps(info.get('tags', [])))
    query = 'Nurse With Wound'
    value = artist_db.get(query.encode('utf-8'))
    if value == None:
        print('Sorry, databases do not contain Your query')
    else:
        print(query + "'s tags are", pickle.loads(value))
    artist_db.close()
