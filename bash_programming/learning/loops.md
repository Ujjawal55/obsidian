```bash

#!/bin/bash
# while loop

# A script to display a series of numbers using a while loop.

counter=1
while [[ "$counter" -le 10 ]]; do
    echo "The counter is at: $counter"
    counter=$((counter + 1))
done
echo "The count has finished."

# until loop

counter=1
until [[ "$counter" -gt 10 ]]; do
    echo "The counter is at: $counter"
    counter=$((counter + 1))
done
echo "The count has finished."

# traditional for loop

services=("loadbalancer" "virtualmachine" "storage")

for i in "${services[@]}"
do
   echo $i
done

# new for loop

for (( i=0; i<5; i=i+1 )); do
    echo "The counter is at: $i"
done


```
