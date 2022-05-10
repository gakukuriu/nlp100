import System.Environment
import Codec.Binary.UTF8.String

main = do
  (tailNumber:(rfPath:argList)) <- getArgs
  contents <- readFile rfPath
  let contentLines = lines $ encodeString contents
  putStr (decodeString $ unlines (drop ((length contentLines) - (read tailNumber :: Int)) contentLines))
