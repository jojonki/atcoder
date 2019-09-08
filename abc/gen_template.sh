#!/bin/sh

if [ $# -ne 1 ]; then
  echo "need to specify program number"
  exit 1
fi

cp code_template.cc ./abc$1a.cc
cp code_template.cc ./abc$1b.cc
cp code_template.cc ./abc$1c.cc
cp code_template.cc ./abc$1d.cc

touch ./t/t_abc$1a.txt
touch ./t/t_abc$1b.txt
touch ./t/t_abc$1c.txt
touch ./t/t_abc$1d.txt
