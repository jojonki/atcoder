#!/bin/sh

if [ $# -ne 2 ]; then
  echo "need to specify program number"
  exit 1
fi

#~/anaconda3/envs/atcoder/bin/python abc$1$2.py < ./t/t_abc$1$2.txt
/usr/local/bin/pypy3 dp_$1.py < ./t/t_dp_$1.txt