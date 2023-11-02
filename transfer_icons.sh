#!/bin/bash
dos2unix Icons.txt
file="Icons.txt"
out_dir="$(pwd)/front/Icons"
mkdir $out_dir

while IFS= read -r line; do
    cp "$line" "$out_dir"
done < "$file"

echo "successfully transferred"