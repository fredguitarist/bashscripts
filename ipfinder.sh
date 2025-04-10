#!/bin/bash

network="192.168.100"

echo "Свободные IP-адреса в сети $network.0/24:"

for i in {1..254}; do
    ip="$network.$i"
    if ! ping -c 1 -W 1 $ip &> /dev/null; then
        echo $ip
    fi
done
