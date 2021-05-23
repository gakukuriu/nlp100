import sys, re, requests

filepath = sys.argv[1]
start = re.compile(r'\{\{基礎情報')
end = re.compile(r'\}\}')
info = re.compile(r'\|([^\=]+)(\=)([^\=]+)')
ansDict = {}
flag = 0
flag2 = 0

with open(filepath) as f:
  for line in f:
    if flag2:
      i = info.match(line)
      if i:
        flag2 = 0
        key = i[1].strip()
        value = i[3].strip()
        ansDict[key] = re.sub(r'[\'\[\]\|\{\}]', '', value)
      else:
        ansDict['公式国名'] = ansDict['公式国名'] + re.sub(r'[\'\[\]\|\{\}]', '', line)
    else:
      if flag:
        e = end.match(line)
        if e:
          flag = 0
        else:
          i = info.match(line)
          key = i[1].strip()
          value = i[3].strip()
          ansDict[key] = re.sub(r'[\'\[\]\|\{\}]', '', value)
          if key == '公式国名':
            flag2 = 1
      else:
        s = start.match(line)
        if s:
          flag = 1
  
  S = requests.Session()
  URL = "https://en.wikipedia.org/w/api.php"
  PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:" + ansDict['国旗画像']
  }
  R = S.get(url=URL, params=PARAMS)
  DATA = R.json()
  PAGES = DATA["query"]["pages"]
  for k, v in PAGES.items():
    print(v['imageinfo'][0]['url'])