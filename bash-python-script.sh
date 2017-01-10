#!/bin/bash

#Profiles the execution sorting by cumalative time
#/usr/local/bin/pypy3/bin/pypy3 -O -m cProfile -s cumtime ./giveMeAMove.py "$@"
#Runs the script without profiling
/usr/local/bin/pypy3/bin/pypy3 -O ./giveMeAMove.py "$@"
exit $?
