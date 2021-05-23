def cipher(s):
  s2 = ""
  for c in s:
    if c.islower():
      s2 += chr(219 - ord(c))
    else:
      s2 += c
  return s2

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(cipher(s))