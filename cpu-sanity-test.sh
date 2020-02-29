#!/bin/bash

# Just run this file and you can test your circ files!
# Make sure your files are in the directory above this one though!

cp alu.circ cpu_tests
cp regfile.circ cpu_tests
cp cpu.circ cpu_tests
cd cpu_tests
./sanity_test.py
cd ..