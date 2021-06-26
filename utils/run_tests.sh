#!/bin/bash
#
# Simple driver to run tests in one command

enable_link_check_tests=0

while (( "$#" )); do
  case "$1" in
    -l|--enable-link-check-tests)
      enable_link_check_tests=1
      shift
      ;;
    -*|--*=) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      exit 1
      ;;
  esac
done

if [[ ! -d build_tests ]] ; then
    mkdir build_tests
fi

cd build_tests/

if [[ -e CMakeCache.txt ]] || [[ -d CMakeFiles/ ]] ; then
  rm -r CMake*
fi

if [[ "${enable_link_check_tests}" == "1" ]] ; then
  cmake_args="-DENABLE_LINK_CHECK_TESTS:BOOL=ON"
else
  cmake_args=
fi

cmake ${cmake_args} ..

ctest
