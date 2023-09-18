read a b c
if [ $((a + b)) -eq $c ]; then
    echo correct!
else
    echo wrong!
fi
