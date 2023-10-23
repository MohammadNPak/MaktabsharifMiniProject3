#!/bin/bash
if [[ ! -d ${icons} ]]; then
mkdir icons
fi
data="/home/flatlife/PycharmProjects/MaktabsharifMiniProject3/icons.txt"
file=$data
while read -r line; do
echo -e "$line\n"
cp $line "/home/flatlife/PycharmProjects/MaktabsharifMiniProject3/icons"
done <$file
