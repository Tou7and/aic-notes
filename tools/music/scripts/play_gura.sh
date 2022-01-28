#!/bin/bash
# sox input.wav output.wav speed 1.33
n_loop=2

for (( c=1; c<=$n_loop; c++)); do
  echo "n = $c"
  play "./gura/omg.mp3" tempo 0.8
  play "./gura/booba.mp3" tempo 0.8
done

