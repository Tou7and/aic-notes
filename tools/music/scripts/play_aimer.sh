#!/bin/bash
# sox input.wav output.wav speed 1.33
n_loop=2

for (( c=1; c<=$n_loop; c++)); do
  echo "n = $c"
  play "./aimer/Aimer-春はゆく.mp3" 
  play "./aimer/Aimer-残響散歌.mp3"
done

