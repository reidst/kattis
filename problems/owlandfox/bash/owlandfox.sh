# kattis-tle
read count
for i in $(seq 1 $count); do
    read x
    for ((y = 1; x%y == 0; y *= 10)); do :; done
    echo $((x - y / 10))
done
