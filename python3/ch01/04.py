s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
numbers = [1,5,6,7,8,9,15,16,19]
ans = {}

words = s.split(' ')
for w, i in zip(words, range(1, len(words)+1)):
  if i in numbers:
    ans[w[:1]] = i
  else:
    ans[w[:2]] = i

print(ans)