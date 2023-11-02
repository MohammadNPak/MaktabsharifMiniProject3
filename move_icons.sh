#!/bin/bash
mkdir "./front/Icons"
file="Icons.txt"
while read -r line; do
    echo "$line"
    mv "$line" "front/Icons/"
done <$file

