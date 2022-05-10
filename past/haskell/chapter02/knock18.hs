import System.Environment
import Codec.Binary.UTF8.String
import Data.List
import Data.List.Split

main = do
  (rfPath:argList) <- getArgs
  contents <- readFile rfPath
  putStr $ decodeString (unlines $ map splitCutMinus (sort $ map (splitCutPlus 2) (lines $ encodeString contents)))

splitCutPlus :: Int -> [Char] -> (Float, [Char])
splitCutPlus n column = (read ((splitOn "\t" column) !! n) :: Float, column)

splitCutMinus :: (Float, [Char]) -> [Char]
splitCutMinus (n, column) = column
