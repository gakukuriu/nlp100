import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = list(map(lambda w: len(re.sub('[^a-zA-Z]+', '', w)), s.split(' ')))

print(ans)