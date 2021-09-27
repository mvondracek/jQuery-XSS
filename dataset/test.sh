#!/usr/bin/env bash

echo "run tested tools (jqxss, eslintp)"
cd ./out/ || exit 1
for file in *.gen.js; do
  python ../../jqueryxsscli.py -l -i "${file}" > "${file%.gen.js}.jqxss";
  npx eslint --format unix --stdin < "${file}" \
  | grep "<text>" \
  | sed -e "s/^<text>:/${file}:/" > "${file%.gen.js}.eslintp"
#  | sed -e 's/^<file>://' > "${file%.gen.js}.eslintp"
  echo "${file}";
done

echo "compare expected output with jqxss and eslintp"
echo "" > eslintp.diff.txt
echo "" > jqxss.diff.txt
for file in *.gen.js; do
  diff --strip-trailing-cr -q -s "${file%.gen.js}.jqxss" "${file%.gen.js}.out" >> jqxss.diff.txt
  sed -e "s/^${file}:\([0-9]\+\):\([0-9]\+\):.*$/\1:\2/" "${file%.gen.js}.eslintp" \
  | diff --strip-trailing-cr -q -s - "${file%.gen.js}.out" >> eslintp.diff.txt
  echo "${file}";
done

echo "collect results"
grep "" ./*.out > out.cat.txt
grep "" ./*.jqxss > jqxss.cat.txt
grep "" ./*.eslintp > eslintp.cat.txt

echo "finished"
