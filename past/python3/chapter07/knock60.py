import sys, plyvel, json

with open(sys.argv[1], 'r') as rf:
    artist_db = plyvel.DB(sys.argv[2], create_if_missing=True)
    for line in rf:
        inf = json.loads(line)
        artist_db.put((inf.get('name', 'N/A')).encode('utf-8'), (inf.get('area', 'N/A')).encode('utf-8'))
    artist_db.close()
