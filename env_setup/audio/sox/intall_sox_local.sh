#!/bin/bash
set -eo pipefail

install_dir="/home/t36668/sox/bin"
install_bin="${install_dir}/sox"

tar_file="sox-14.4.2.tar.gz"
sox_dir="sox-14.4.2"

if [ ! $tar_file ]; then
  echo "Download the tar ball from sourceforge..."
  wget https://nchc.dl.sourceforge.net/project/sox/sox/14.4.2/sox-14.4.2.tar.gz
  tar xvfz sox-14.4.2.tar.gz
fi

if [ ! $sox_dir ]; then
  cd sox-14.4.2
  ./configure --prefix=$INSTALL_DIR
  make
  make install
fi

if [ $install_bin ]; then
  echo "Installation is complete."
  echo "You can add the following line in the bash profile now:"
  echo "export PATH=\$PATH:${install_dir}"
fi

