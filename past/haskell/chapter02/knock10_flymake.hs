import System.Environment

main = do
  (filePath:argList) <- getArgs
  contents <- readFile filePath
  print (length $ lines contents)
  
