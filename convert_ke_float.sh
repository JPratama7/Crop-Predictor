#!/bin/bash

# Menggunakan loop untuk mencetak setiap file dengan path lengkap
for file in "final dataset"/*; do
    if [ -f "$file" ]; then
        modified_name=$(basename "$file" | sed 's/Datasaet //' | sed 's/.xlsx//')
        final_name=$(echo "$modified_name" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')
        final_name+="_float"
        python convert_to_float.py -i "$file" -o "floated/$final_name.csv"
    fi
done