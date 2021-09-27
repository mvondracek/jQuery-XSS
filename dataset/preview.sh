#!/usr/bin/env bash

cd ./out/ || exit 1
for file in *.gen.js; do
  read -n 1 -s -r -p "Press any key to continue"; echo "";
  echo "$file";
  python -m pygments -g -f 16m "$file" | cat -n
  echo "out:"; cat -n "${file%.gen.js}.out"
  echo "jqxss:"; cat -n "${file%.gen.js}.jqxss"
  echo "eslint:"; cat -n "${file%.gen.js}.eslintp"
  diff --strip-trailing-cr -q "${file%.gen.js}.jqxss" "${file%.gen.js}.out"
  sed -e "s/^${file}:\([0-9]\+\):\([0-9]\+\):.*$/\1:\2/" "${file%.gen.js}.eslintp" | diff --strip-trailing-cr -q - "${file%.gen.js}.out"
  echo -e "-----\n\n\n"
done
cd ..
