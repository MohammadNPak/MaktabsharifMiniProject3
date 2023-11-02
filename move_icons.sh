#!/bin/bash
mkdir "/Users/alora/Maktab/sending projects/hw7/untitled folder/MaktabsharifMiniProject3/front/Icons"
file="Icons.txt"
while read -r line; do
    echo "$line"
    mv "$line" "front/Icons/"
done <$file
# mv "/Users/alora/Maktab/sending projects/hw7/untitled folder/MaktabsharifMiniProject3/front/images/img-1.png" "front/Icons/"
