import System.Environment
import Codec.Binary.UTF8.String

main = do
  (headNumber:(rfPath:argList)) <- getArgs
  contents <- readFile rfPath
  putStr (decodeString $ unlines (take (read headNumber :: Int) (lines $ encodeString contents)))
