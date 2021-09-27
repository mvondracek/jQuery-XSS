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

mkdir -p ./out/tmp/

echo "generate basic samples for each method"
for method in ${unsafe_methods[*]}; do
  echo -n "${method}, generate"
  method_dir="./out/tmp/${method}"
  mkdir "${method_dir}"
  for filepath in ./in/*.js; do
    filename=$(basename "$filepath")
    cp "$filepath" "${method_dir}/${batch}_${filename}"
    cp "${filepath%.js}.out" "${method_dir}/${batch}_${filename%.js}.out"
    echo -n "."
  done
  echo ""
  sed -i "s/__BATCH__/_${batch}_/g" "${method_dir}/"*.js
  sed -i "s/__METHOD__/${method}/g" "${method_dir}/"*.js
  echo "${method}, done"
  mv "${method_dir}/"*.js ./out/tmp/
  mv "${method_dir}/"*.out ./out/
  rmdir "${method_dir}"
  echo "${method}, moved"
  batch=$((batch+1))
done

echo "copy static samples"
cp ./static/*.js ./out/tmp/
cp ./static/*.out ./out/

echo -n "finalize all samples with xss from parameter"
for filepath in ./out/tmp/*.js; do
  filename=$(basename "$filepath")
  cat ./xss_param.js "$filepath" > "./out/${filename%.js}.gen.js"
  rm "$filepath"
  echo -n "."
done
echo ""
rmdir ./out/tmp/
echo "all samples finalized"
