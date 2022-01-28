#!/bin/bash

n_loop=3

for (( c=1; c<=$n_loop; c++)); do
  echo "n = $c"
  play "./NieRA_OST/104. 砂塵ノ記憶.mp3"
#   play "./NieRA_OST/207. 全テヲ破壊スル黒キ巨人／怪獣.mp3"
#   play "./NieRA_OST/101. 意味／無／ジュニーク・ニコール.mp3"
  play "./NieRA_OST/107. 遊園施設.mp3"
  play "./NieRA_OST/108. 美シキ歌.mp3"
  play "./abyss/Made in Abyss OST 2. The First Layer.mp3"
  play "./NieRA_OST/203. 異形ノ末路.mp3"
  play "./NieRA_OST/313. 双極ノ悪夢.mp3"
#   play "./typemoon/梶浦由記 - Ⅳ paradigm.mp3"
  play "./pokemon/*.mp3"
done

