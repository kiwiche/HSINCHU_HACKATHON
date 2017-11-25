x=500

while [ $x -gt 0 ]

do
    echo $x

    python3 /home/qoo/Documents/ubike/get_file.py

    x=$(( $x - 1 ))

    sleep 5m

done
