def nGram_letter(s, n):
  ans = []
  for i, j in zip(range(len(s)), range(n, len(s)+1)):
    ans.append(s[i:j])
  return ans

w1 = "paraparaparadise"
w2 = "paragraph"

X = set(nGram_letter(w1, 2))
Y = set(nGram_letter(w2, 2))

print("XとYの和集合: ", X | Y)
print("XとYの積集合: ", X & Y)
print("XからYを引いた差集合: ", X - Y)
print("YからXを引いた差集合: ", Y - X)

if 'se' in X:
  print("Xにseは含まれています")
else:
  print("Xにseは含まれていません")

if 'se' in Y:
  print("Yにseは含まれています")
else:
  print("Yにseは含まれていません")
