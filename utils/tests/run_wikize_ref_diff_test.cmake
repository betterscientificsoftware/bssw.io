#
# CMake -P script to run a system-level test of the wikize_refs.py script
#
# Usage:
#
#  cmake \
#    -D TEST_NAME=<testName> \
#    -D INPUT_FILE=<inputFile> \
#    -D OUTPUT_FILE=<outputFile> \
#    -D WIKIZE_REFS_ARGS=<wikizeRefsArgs> \
#    -D EXPECTED_OUTPUT_FILE=<expectedOutputFile> \
#    -P run_wikize_ref_diff_test.cmake
#
# Here, the filepaths for <inputFile> and <expectedOutputFile> should be
# absolute paths.  The name <outputFile> should not include a path as it is to
# be produced by the wikize_refs.py script.
#
# This script sets up the test output directory <testName>, copies in the
# input file <inputFile>, runs:
#
#   wikize_refs.py <wikizeRevsArgs> name(<inputFile>)
#
# (where name(<inputFile>) is the name without the directory path) and then diffs:
#
#   diff <expectedOutputFile> <outputFile>
#
# If the wikize_refs.py command runs to completion without error and the diff
# of the output file against the expected output file returns no change, then
# this CMake -P script will return 0.  Otherwise, it will return non-zero and
# print the error to STDOUT.
#

#include(CMakePrintHelpers)
#cmake_print_variables(TEST_NAME INPUT_FILE OUTPUT_FILE WIKIZE_REFS_ARGS EXPECTED_OUTPUT_FILE)

# A) Set up test directory to hold the input and output files

if (EXISTS ${TEST_NAME})
  message("Removing dir ${TEST_NAME}")
endif()

message("Creating dir ${TEST_NAME}")
file(MAKE_DIRECTORY "${TEST_NAME}")

# B) Copy input file to test directory

message("Copy input file '${INPUT_FILE}'") 
file(COPY "${INPUT_FILE}" DESTINATION "${TEST_NAME}")

# C) Run the wikize_refs command

set(wikizeRefs "${CMAKE_CURRENT_LIST_DIR}/../wikize_refs.py")
get_filename_component(inputFileName "${INPUT_FILE}" NAME)
set(wikizeRefsCmnd ${wikizeRefs} ${WIKIZE_REFS_ARGS} ${inputFileName})

message("Running: ${wikizeRefsCmnd}")

execute_process(
  COMMAND ${wikizeRefsCmnd}
  WORKING_DIRECTORY "${TEST_NAME}"
  RESULT_VARIABLE wikizRefsRtnCode
  )

if (NOT wikizRefsRtnCode EQUAL 0)
  message(FATAL_ERROR "wikize_refs.py returned '${wikizRefsRtnCode}'")
endif()

# D) Compare the output file to expected output

message("Diffing expected output '${EXPECTED_OUTPUT_FILE}' to output '${OUTPUT_FILE}'")

execute_process(
  COMMAND diff "${EXPECTED_OUTPUT_FILE}" "${OUTPUT_FILE}" 
  WORKING_DIRECTORY "${TEST_NAME}"
  RESULT_VARIABLE diffRtnCode
  )

if (NOT diffRtnCode EQUAL 0)
  message(FATAL_ERROR "diff returned '${diffRtnCode}'")
endif()
