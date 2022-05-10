{-# LANGUAGE DeriveGeneric #-}

import System.Environment
-- import Codec.Binary.UTF8.String
import qualified Data.Aeson as Aes
import GHC.Generics


data WikiDic = WikiDic {title :: String, text :: String} deriving (Show, Generic)
instance Aes.FromJSON WikiDic
instance Aes.ToJSON WikiDic

-- main = do
--  (rfPath:(wfPath:argList)) <- getArgs
--  contents <- readFile rfPath
--  let json = "{\"title\":\"a\",\"text\":\"com\"}"
--  case Aes.decode json :: Maybe WikiDic of
--    Nothing -> print "Parse Error" 
--   Just x -> print x

  


