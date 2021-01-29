#!/bin/sh

if [ $# -ne 1 ]; then
  echo "need to specify program number"
  exit 1
fi

#~/anaconda3/envs/atcoder/bin/python dp_$1.py < ./t/t_dp_$1.txt
/usr/local/bin/pypy3 dp_$1.py < ./t/t_dp_$1.txt