#!/bin/bash

mp3_dir="/Users/mac/data/audio/mp3/kotoko/"
nc_dir="/Users/mac/data/audio/mp3/kotoko/nightcore"

mkdir $nc_dir

for mp3 in $mp3_dir/*.mp3 
do
  new_mp3=$(echo "$mp3" | sed "s,$mp3_dir,$nc_dir,g")
  echo "$mp3 > $new_mp3"
  echo "start processing ..."
  python ./mp3_to_nightcore.py $mp3 $new_mp3
  echo "end processing."
done

