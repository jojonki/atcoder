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
  echo "Generate abc$1$char" 
  # touch ./abc$1$char.py
  cp template.py ./abc$1$char.py
  touch ./t/t_abc$1$char.txt
done