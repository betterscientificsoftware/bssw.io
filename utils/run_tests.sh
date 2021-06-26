#!/bin/bash
#
# Simple driver to run tests in one command

usage_str="Usage: run_tests.sh [-l|--enable-link-check-tests] [-s|--submit-to-cdash]"

enable_link_check_tests=0
submit_to_cdash=0

while (( "$#" )); do
  case "$1" in
    -l|--enable-link-check-tests)
      enable_link_check_tests=1
      shift
      ;;
    -s|--submit-to-cdash)
      submit_to_cdash=1
      shift
      ;;
    -h|--help)
      echo "${usage_str}"
      exit 0
      ;;
    *) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      echo "${usage_str}"
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

if [[ "${submit_to_cdash}" == "1" ]] ; then
  ctest -M Experimental -T Start -T Configure -T Build -T Test -T Submit
else
  ctest
fi
