import sys, plyvel

artist_db = plyvel.DB(sys.argv[1])
query = ''
for el in sys.argv[2:]:
    query += el + ' '
query = query.strip()
value = artist_db.get(query.encode('utf-8'))
artist_db.close()

if value == None:
    print('Sorry, databases do not contain Your query')
else:
    print(query + ' is based on ' + value.decode('utf-8'))
