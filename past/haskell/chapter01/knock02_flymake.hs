s1 = "パトカー"
s2 = "タクシー"

charpairZip [] = []
charpairZip ((x1, x2):xs) = x1:x2:(stringGen xs)

main = putStrLn (charpairZip [p | p <- zip s1 s2])
