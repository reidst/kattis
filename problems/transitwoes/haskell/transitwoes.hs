-- kattis-accepted
module Main where

main :: IO ()
main = interact $ output . solve . parse

parse :: String -> [[Int]]
parse = map (map read . words) . lines

solve :: [[Int]] -> Bool
solve [start:finish:_,[walk],[],[]] = start + walk <= finish
solve [start:finish:_,w:walk,b:bus,a:arrival]
  | start > finish = False
  | otherwise = solve [[newstart,finish],walk,bus,arrival]
  where
    newstart = travel start w b a

travel :: Int -> Int -> Int -> Int -> Int
travel start walk bus arrival = busRound arrival (start + walk) + bus

busRound :: Int -> Int -> Int
busRound arrival start = case start `mod` arrival of
  0 -> start
  m -> start - m + arrival

output :: Bool -> String
output b = if b then "yes" else "no"
