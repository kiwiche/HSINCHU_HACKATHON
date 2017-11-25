x=500

while [ $x -gt 0 ]

do
    echo $x

    python3 get_file.py

    x=$(( $x - 1 ))

    sleep 5m

done
