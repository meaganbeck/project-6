#!/bin/bash

for t in tests/*.py
do
    nosetests3 $t
done
