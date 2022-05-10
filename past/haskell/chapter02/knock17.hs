import System.Environment
import Codec.Binary.UTF8.String
import Data.List
import Data.List.Split

main = do
  (rfPath:argList) <- getArgs
  contents <- readFile rfPath
  let baseSet = cutColumn 0 contents
  putStr $ decodeString (unlines $ nub baseSet)


splitCut :: Int -> [Char] -> [Char]
splitCut n column = (splitOn "\t" column) !! n

cutColumn :: Int -> String -> [String]
cutColumn n texts = map (splitCut n) (lines $ encodeString texts)


