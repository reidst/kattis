-- kattis-accepted
import Data.List (sort)

main :: IO ()
main = interact solve

solve :: String -> String
solve s = solveNums (potionTimes s) (drinkTime s)
  
potionTimes :: String -> [Int]
potionTimes = reverse . sort . map read . tail . lines

drinkTime :: String -> Int
drinkTime = read . last . words . head . lines

solveNums :: [Int] -> Int -> String
solveNums []     _ = "YES"
solveNums (x:xs) t
  | length xs * t < x = solveNums xs t
  | otherwise         = "NO"
