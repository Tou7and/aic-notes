#!/bin/bash

n_loop=1

for (( c=1; c<=$n_loop; c++)); do
  echo "n = $c"
  play "./michal_jackson/BeatIt.mp3"
  play "./michal_jackson/bille-jean.mp3"
  play "./michal_jackson/smooth-criminal.mp3"
done

