import Text.Regex
import qualified Data.Map as Map

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
switch = [1, 5, 6, 7, 8, 9, 15, 16, 19]

main = print $ Map.fromList [if any (v==) switch then ((take 1 k), v) else ((take 2 k), v) | (k, v) <- zip (words s) [1..]]
