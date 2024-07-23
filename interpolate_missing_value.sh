#!/bin/bash

# Menggunakan loop untuk mencetak setiap file dengan path lengkap
for exec in interpolate*.py; do
  filename=$(basename "$exec")
  method=$(echo "$filename" | sed 's/interpolate_//' | sed 's/.py//')

  if [ ! -d "interpolate/$method" ]; then
    mkdir -p "interpolate/$method"
  fi

  for file in "floated"/*; do
      if [ -f "$file" ]; then
          filename=$(basename "$file")
          plant_type=$(echo "$filename" | sed -E 's/^(.*)_float\.csv$/\1/')
          plant_type+="."
          plant_type+="${filename##*.}"
          python "interpolate_$method.py" -i "$file" -o "interpolate/$method/$plant_type"
      fi
  done
done