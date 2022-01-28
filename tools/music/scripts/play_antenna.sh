#!/bin/bash

n_loop=2

for (( c=1; c<=$n_loop; c++)); do
  echo "n = $c"
  play "./miku/sun-disco.mp3"
  play "./wakaband/腦漿炸裂Girl-wakaband.mp3"
  play "./typemoon/love-me-if-you-can.mp3"
done

