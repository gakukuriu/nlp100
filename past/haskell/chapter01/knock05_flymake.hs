s = "I am an NLPer"

ngram :: Int -> [a] -> [[a]]
ngram n [] = []
ngram n xs = if length xs >= n then (take n xs) : (ngram n (tail xs)) else []

main = do
  putStr "単語bi-gram: "
  print (ngram 2 (words s))
  putStr "文字bi-gram: "
  print (ngram 2 s)
