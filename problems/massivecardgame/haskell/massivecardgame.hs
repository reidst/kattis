-- kattis-unsolved
import Data.List (sort)
import qualified Data.Map as M

main :: IO ()
main = interact solve

solve :: String -> String
solve input = case lines input of
  _:nums:_:ranges -> formatOutput $ solveRanges
    (makeDict 0 M.empty . sort . map read . words $ nums)
    (makeRanges ranges)

formatOutput :: [Int] -> String
formatOutput = unlines . map show

solveRanges :: M.Map Int (Int, Int) -> [(Int, Int)] -> [Int]
solveRanges m = map $ solveRange m

{- TODO
 - * left element of `l` in the map
 -   * use least key `>= l` in the map (lookupGE)
 - * right element of `r` in the map
 -   * use greatest key `<= r` in the map (lookupLE)
 - * return right element - left element + 1
 -}
solveRange :: M.Map Int (Int, Int) -> (Int, Int) -> Int
solveRange m (l, r) = undefined

makeDict :: Int -> M.Map Int (Int, Int) -> [Int] -> M.Map Int (Int, Int)
makeDict i m [] = m
makeDict i m (x:xs) = case M.lookup x m of
  Nothing -> makeDict (i + 1) (M.insert x (i, i) m) xs
  Just (s, e) -> makeDict (i + 1) (M.insert x (s, i) m) xs

makeRanges :: [String] -> [(Int, Int)]
makeRanges = map ((\[x,y] -> (x,y)) . map read . words)
