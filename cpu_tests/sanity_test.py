#!/usr/bin/env python2

import autograder_base
import os.path

from autograder_base import file_locations, AbsoluteTestCase, main

tests = [
  ("Single-cycle CPU add/lui/sll test",AbsoluteTestCase(os.path.join(file_locations,'CPU-add_lui_sll.circ'),os.path.join(file_locations,'reference_output/CPU-add_lui_sll.out'),1)),
  ("Single-cycle CPU memory test",AbsoluteTestCase(os.path.join(file_locations,'CPU-mem.circ'),os.path.join(file_locations,'reference_output/CPU-mem.out'),1)),
  ("Single-cycle CPU branch test",AbsoluteTestCase(os.path.join(file_locations,'CPU-branch.circ'),os.path.join(file_locations,'reference_output/CPU-branch.out'),1)),
  ("Single-cycle CPU jump test",AbsoluteTestCase(os.path.join(file_locations,'CPU-jump.circ'),os.path.join(file_locations,'reference_output/CPU-jump.out'),1))
]

if __name__ == '__main__':
  main(tests)
