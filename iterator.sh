#!/usr/bin/bash

# Menggunakan loop untuk mencetak setiap file dengan path lengkap
for file in "final dataset"/*; do
    if [ -f "$file" ]; then

        echo "$file"
    fi
done