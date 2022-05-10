s1 = "パトカー"
s2 = "タクシー"

pairLtoL :: [(a, a)] -> [a]
pariLtoL [] = []
pairLtoL ((x1, x2):xs) = x1:x2:(pairLtoL xs)

main = putStrLn $ pairLtoL (zip s1 s2)
