#!/bin/bash
#
# Simple driver to run tests in one command

if [[ ! -d build_tests ]] ; then
    mkdir build_tests
fi

cd build_tests/

if [[ -e CMakeCache.txt ]] || [[ -d CMakeFiles/ ]] ; then
  rm -r CMake*
fi

cmake ..

ctest -M Experimental -T Start -T Test -T Submit

echo
echo "See results at https://my.cdash.org/index.php?project=BsswUtils"
