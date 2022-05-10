import Text.Regex
import System.Environment
import Codec.Binary.UTF8.String

main = do
  (filePath:argList) <- getArgs
  contents <- readFile filePath
  putStr $ decodeString (subRegex (mkRegex "\t") (encodeString contents) " ")
