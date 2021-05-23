def nGram_word(s, n):
  words = s.split(' ')
  ans = []
  for i, j in zip(range(len(words)), range(n, len(words)+1)):
    ans.append(words[i:j])
  return ans

def nGram_letter(s, n):
  ans = []
  for i, j in zip(range(len(s)), range(n, len(s)+1)):
    ans.append(s[i:j])
  return ans

s = "I am an NLPer"
print(nGram_word(s, 2))
print(nGram_letter(s, 2))