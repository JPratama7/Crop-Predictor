#!/bin/bash

# Menggunakan loop untuk mencetak setiap file dengan path lengkap
for file in "final dataset"/*; do
    if [ -f "$file" ]; then
        modified_name=$(basename "$file" | sed 's/Datasaet //' | sed 's/.xlsx//')
        final_name=$(echo "$modified_name" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')
        python preprocess.py -i "$file" -o "preprocessed/$final_name.csv"
    fi
done