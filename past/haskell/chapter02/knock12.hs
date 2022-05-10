import System.Environment
import Codec.Binary.UTF8.String
import Data.List.Split

main = do
  (filePath:(wf1Path:(wf2Path:argList))) <- getArgs
  contents <- readFile filePath
  writeFile wf1Path (cutColumn 0 contents)
  writeFile wf2Path (cutColumn 1 contents)

splitCut :: Int -> [Char] -> [Char]
splitCut n column = (splitOn "\t" column) !! n

cutColumn :: Int -> String -> String
cutColumn n texts = decodeString $ unlines (map (splitCut n) (lines $ encodeString texts))
