import qualified Data.Set as S
import Data.Maybe (fromMaybe)

main :: IO ()
main = interact solve

solve :: String -> String
solve = answer . findBest Nothing . filter validName . tail . lines

answer :: Maybe String -> String
answer = fromMaybe "Neibb"

findBest :: Maybe String -> [String] -> Maybe String
findBest m [] = m
findBest Nothing (x:xs) = findBest (Just x) xs
findBest (Just b) (x:xs) = findBest (Just (bestOf b x)) xs

bestOf :: String -> String -> String
bestOf a b = case compare (length a) (length b) of
  LT -> a
  GT -> b
  EQ -> max a b

validName :: String -> Bool
validName s
  | length s < 5 = False
  | containsDuplicate S.empty s = False
  | otherwise = True

containsDuplicate :: Ord a => S.Set a -> [a] -> Bool
containsDuplicate _ [] = False
containsDuplicate s (x:xs)
  | S.member x s = True
  | otherwise = containsDuplicate (S.insert x s) xs
