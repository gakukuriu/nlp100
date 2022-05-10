import System.Environment
import Codec.Binary.UTF8.String

main = do
  (splitNumber:(rfPath:(wfPath:argList))) <- getArgs
  contents <- readFile rfPath
  let contentLines = lines $ encodeString contents
  splitSentence (read splitNumber :: Int) contentLines wfPath 0

splitSentence n [] wfName fileNumber = return ()
splitSentence n (x:xs) wfName fileNumber = do
  writeFile (wfName ++ show fileNumber ++ ".txt") (decodeString (unlines $ take n (x:xs)))
  splitSentence n (drop n (x:xs)) wfName (fileNumber + 1)
