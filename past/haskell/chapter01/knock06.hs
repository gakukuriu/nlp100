import Data.List

s1 = "paraparaparadise"
s2 = "paragraph"

ngram :: Int -> [a] -> [[a]]
ngram n [] = []
ngram n xs = if length xs >= n then (take n xs) : (ngram n (tail xs)) else []

setX = nub $ ngram 2 s1
setY = nub $ ngram 2 s2
unionXY = union setX setY
intersectXY = intersect setX setY
difXY = setX \\ setY
difYX = setY \\ setX
seInX = "se" `elem` setX
seInY = "se" `elem` setY

main = do
  putStr "集合X: "
  print setX
  putStr "集合Y: "
  print setY
  putStr "XとYの和集合: "
  print unionXY
  putStr "XとYの積集合: "
  print intersectXY
  putStr "差集合X-Y: "
  print difXY
  putStr "差集合Y-X: "
  print difYX
  putStr "集合Xに'se'が含まれる: "
  print seInX
  putStr "集合Yに'se'が含まれる: "
  print seInY
  
  
  
  
  
