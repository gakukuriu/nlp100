import sys, json

filepath = sys.argv[1]
articlePath = sys.argv[2]

with open(filepath) as f, open(articlePath, 'w') as a:
  for j in f:
    article = json.loads(j)
    if article['title'] == 'イギリス':
      a.write(article['text'])      
  

