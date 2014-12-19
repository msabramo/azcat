#!/bin/sh
TESTS=$(echo test/*)

for f in $TESTS; do
   echo "************ $f"
  ./az $f
done
