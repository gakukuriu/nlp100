import Data.Char

s = "I am an NLPer"

cipherChar :: Char -> Char
cipherChar c = if isLower c then chr (219 - (ord c)) else c

cipher :: [Char] -> [Char]
cipher s = map cipherChar s

main = do
  putStrLn $ "Default: " ++ s
  putStrLn $ "ciphered: " ++ (cipher s)
