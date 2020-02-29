#!/bin/bash

# Just run this file and you can test your circ files!
# Make sure your files are in the directory above this one though!

cp alu.circ cpu_tests_pipelined
cp regfile.circ cpu_tests_pipelined
cp cpu.circ cpu_tests_pipelined
cd cpu_tests_pipelined
./sanity_test.py
cd ..