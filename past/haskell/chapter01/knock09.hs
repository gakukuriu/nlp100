import System.Random.Shuffle

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

wordExchange s | length s > 4 = do
                   shuffledList <- shuffleM (tail $ init s)
                   return $ [head s] ++ shuffledList ++ [last s]
               | otherwise = return s

main = do
  slist <- mapM wordExchange (words s)
  putStrLn $ "Normal: " ++ s
  putStrLn $ "Typoglycemia: " ++ (unwords slist)
