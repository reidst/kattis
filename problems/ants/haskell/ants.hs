-- kattis-accepted
module Main where

import Data.List (sort)

main :: IO ()
main = interact solve

solve :: String -> String
solve = unlines . solveNum . tail . map read . words

solveNum :: [Int] -> [String]
solveNum [] = []
solveNum (len:count:xs) = oneAnswer : solveNum (drop count xs)
  where
    oneAnswer = solveOnce len $ take count xs

solveOnce :: Int -> [Int] -> String
solveOnce len ants = (unwords . map show)
  [ findShortest len ants
  , findLongest  len ants
  ]

findShortest :: Int -> [Int] -> Int
findShortest len = maximum . map (\a -> min a (len - a))

findLongest :: Int -> [Int] -> Int
findLongest len = maximum . map (\a -> max a (len - a))
