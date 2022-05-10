import sys, plyvel

artist_db = plyvel.DB(sys.argv[1])

num = 0
for k, v in artist_db:
    if v.decode('utf-8') == 'Japan':
        num += 1

artist_db.close()        
print(num)
