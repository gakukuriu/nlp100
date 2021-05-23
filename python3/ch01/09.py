import random

def typoglycemia(s):
  words = s.split(' ')
  ansWords = []
  for w in words:
    if len(w) > 4:
      subw = w[1:len(w)-1]
      ansWords.append(w[0] + ''.join(random.sample(subw, len(subw))) + w[len(w)-1])
    else:
      ansWords.append(w)
  return ' '.join(ansWords)

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(s))