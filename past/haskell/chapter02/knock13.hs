import System.Environment
import Codec.Binary.UTF8.String

main = do
  (rf1Path:(rf2Path:(wfPath:argList))) <- getArgs
  contents1 <- readFile rf1Path
  contents2 <- readFile rf2Path
  writeFile wfPath (zipColumn contents1 contents2)

zipColumn :: String -> String -> String
zipColumn text1 text2 = decodeString $ unlines (zipWith (\ t1 t2 -> t1 ++ "\t" ++ t2) (lines $ encodeString text1) (lines $ encodeString text2))
