#!/bin/bash
dos2unix Icons.txt
file="Icons.txt"
out_dir="C:\Users\bcz\Desktop\MaktabSherif\week12\miniproject\MaktabsharifMiniProject3-1\front\Icons"
mkdir $out_dir

while IFS= read -r line; do
    cp "$line" "$out_dir"
done < "$file"

echo "successfully transferred"