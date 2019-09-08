#!/bin/sh

if [ $# -ne 2 ]; then
  echo "need to specify program number"
  exit 1
fi

# echo $2
for char in `echo $2 | fold -w 1`; do
  echo "Generate abc$1$char" 
  cp code_template.cc ./abc$1$char.cc
  touch ./t/t_abc$1$char.txt
done