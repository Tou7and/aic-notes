#!/bin/sh
# This script works on NC24s_v2 (24 vcpu，448 GiB ram) Linux (ubuntu 18.04)

CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.0.130-1_amd64.deb  # cuda-repo-ubuntu1604_10.0.130-1_amd64.deb
wget -O /tmp/${CUDA_REPO_PKG} https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/${CUDA_REPO_PKG} 

sudo dpkg -i /tmp/${CUDA_REPO_PKG}
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub 
rm -f /tmp/${CUDA_REPO_PKG}

echo "Installing via apt ..."
sudo apt-get update
sudo apt-get install cuda-drivers
