x = 12
y = "気温"
z = 22.4

templatefun x y z = show x ++ "時の" ++ y ++ "は" ++ show z

main = putStrLn (templatefun x y z)
