#!/bin/bash

# Menggunakan loop untuk mencetak setiap file dengan path lengkap
for item in "outlier"/*; do
    if [ -d "$item" ]; then
        dir_basename=$(basename "$item")

        for file in "$item"/*; do
          file_basename=$(basename "$file")
          dataset=$(echo "$file_basename" | sed -E 's/^dataset_(.*)\.csv$/\1/')

          # Membuat pesan commit
          commit_message="feat: outlier $dir_basename $dataset"

          # Menambahkan file ke staging area
          echo "$file"
          git add "$file"

          # Melakukan commit dengan pesan yang sesuai
          echo "$commit_message"
          git commit -m "$commit_message"
        done
    fi
done