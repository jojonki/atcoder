#!/bin/sh

if [ $# -ne 2 ]; then
  echo "need to specify program number"
  exit 1
fi

# c++
# for char in `echo $2 | fold -w 1`; do
#   echo "Generate abc$1$char" 
#   cp code_template.cc ./abc$1$char.cc
#   touch ./t/t_abc$1$char.txt
# done

# python
for char in `echo $2 | fold -w 1`; do
  # touch ./abc$1$char.py
  F="./past$1$char.py"
  if [ ! -e $F ]; then
    echo "Generate $F" 
    cp ../template.py $F
  else
    echo "$F already exists"
  fi
  touch ./t/t_past$1$char.txt
done