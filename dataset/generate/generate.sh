#!/usr/bin/env bash

unsafe_methods=(
  'html'
  'prepend'
  'prependTo'
  'append'
  'appendTo'
  'before'
  'after'
  'insertBefore'
  'insertAfter'
  'wrap'
  'wrapInner'
  'wrapAll'
)
batch=1

mkdir -p ./out/

echo "generate basic samples for each method"
for method in ${unsafe_methods[*]}; do
  mkdir "$method"
  for filepath in ./in/*.js; do
    filename=$(basename "$filepath")
    cp "$filepath" "${method}/${batch}_${filename}"
    sed -i "s/__BATCH__/_${batch}_/g" "${method}/"*.js
    sed -i "s/__METHOD__/${method}/g" "${method}/"*.js
  done
  echo "${method} done"
  mv "${method}/"*.js ./out/
  rmdir "${method}"
  echo "${method} moved"
  batch=$((batch+1))
done

echo "copy static samples"
cp ./static/*.js ./out/

echo "finalize all samples with xss from parameter"
mkdir -p ./out/final/
for filepath in ./out/*.js; do
  filename=$(basename "$filepath")
  cat ./xss_param.js "$filepath" > "./out/final/${filename%.js}.gen.js"
done
rm ./out/*.js
mv ./out/final/*.gen.js ./out/
rmdir ./out/final/
echo "all samples finalized"

echo "run tested tools (jqxss, eslintp)"
cd ./out/ || exit 1
for file in *.gen.js; do
  python ../../../jqueryxsscli.py -l -i "${file}" > "${file%.gen.js}.jqxss";
  npx eslint --format unix "${file}" | grep "${file}" | sed -e 's/^D:\\dev\\jQuery-XSS\\dataset\\generate\\out\\//' > "${file%.gen.js}.eslintp"   # TODO: fix path
  echo "${file}";
done

echo "compare expected output with eslintp and jqxss"
echo "" > eslintp.diff.txt
echo "" > jqxss.diff.txt
for file in *.gen.js; do
  sed -e "s/^${file}:\([0-9]\+\):\([0-9]\+\):.*$/\1:\2/" "${file%.gen.js}.eslintp" | diff --strip-trailing-cr -q -s - "${file%.gen.js}.out" >> eslintp.diff.txt
  diff --strip-trailing-cr -q -s "${file%.gen.js}.jqxss" "${file%.gen.js}.out" >> jqxss.diff.txt
done

echo "collect results"
grep "" ./*.out > out.cat.txt
grep "" ./*.eslintp > eslintp.cat.txt
grep "" ./*.jqxss > jqxss.cat.txt

echo "finished"
