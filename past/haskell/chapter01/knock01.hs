s = "パタトクカシー"

main = putStrLn $ [w | (w, n) <- zip s [1..], odd n]
