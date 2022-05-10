import System.Environment
import Codec.Binary.UTF8.String
import Data.List
import Data.List.Split
import qualified Data.Map.Strict as Map

main = do
  (rfPath:argList) <- getArgs
  contents <- readFile rfPath
  let sourceList = count_dict (map (splitCutPlus 0) (lines $ encodeString contents))
  putStr $ decodeString (settleList $ reverse (sort (Map.elems sourceList)))


splitCutPlus :: Int -> [Char] -> ([Char], [Char])
splitCutPlus n column = ((splitOn "\t" column) !! n, column)

colWithSource k (nn, nc) (on, oc) = (nn + on, nc++"\n"++oc)   
count_dict [] = Map.empty
count_dict ((col,source):xs) = Map.insertWithKey colWithSource col (1, source) (count_dict xs)

settleList [] = ""
settleList ((n, source):xs) = source ++ "\n" ++ settleList xs
