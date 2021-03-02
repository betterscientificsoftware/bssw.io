#
# CMake -P script to run a system-level test of the wikize_refs.py script
#
# Usage:
#
#  cmake \
#    -D TEST_NAME=<testName> \
#    -D INPUT_FILE=<inputFile> \
#    -D WIKIZE_REFS_ARGS=<wikizeRefsArgs> \
#    -D COMPARE_SAVED_INPUT_FILE=[TRUE|FALSE] \
#    [-D OUTPUT_FILE=<outputFile>] \
#    [-D EXPECTED_OUTPUT_FILE=<expectedOutputFile>] \
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
# If COMPARE_SAVED_INPUT_FILE=TRUE is passed in, then the file
# name(<inputFile>)~ will be compared to <inputFile> make make sure the
# orginal file is saved.  If COMPARE_SAVED_INPUT_FILE=FALSE, then that file
# can not exist after running wikize_refs.py.
#
# If the wikize_refs.py command runs to completion without error and the diff
# of the output file against the expected output file returns no change, then
# this CMake -P script will return 0.  Otherwise, it will return non-zero and
# print the error to STDOUT.
#

#include(CMakePrintHelpers)
#cmake_print_variables(TEST_NAME INPUT_FILE OUTPUT_FILE WIKIZE_REFS_ARGS EXPECTED_OUTPUT_FILE)

get_filename_component(inputFileName "${INPUT_FILE}" NAME)

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

if (NOT EXPECTED_OUTPUT_FILE STREQUAL "")
  message("Diffing expected output '${EXPECTED_OUTPUT_FILE}' to output '${OUTPUT_FILE}'")
  execute_process(
    COMMAND diff "${EXPECTED_OUTPUT_FILE}" "${OUTPUT_FILE}" 
    WORKING_DIRECTORY "${TEST_NAME}"
    RESULT_VARIABLE diffRtnCode
    )
  if (NOT diffRtnCode EQUAL 0)
    message(FATAL_ERROR "diff returned '${diffRtnCode}'")
  endif()
else()
  message("Skipping diff of output file since none given!")
endif()

# E) Compared the saved input file

set(savedInputFileName "${inputFileName}~")

if (COMPARE_SAVED_INPUT_FILE)
  message("Diffing saved input file '${savedInputFileName}' to input '${INPUT_FILE}'")
  execute_process(
    COMMAND diff "${savedInputFileName}" "${INPUT_FILE}"
    WORKING_DIRECTORY "${TEST_NAME}"
    RESULT_VARIABLE diffRtnCode
    )
  if (NOT diffRtnCode EQUAL 0)
    message(FATAL_ERROR "diff returned '${diffRtnCode}'")
  endif()
else()
  message("Ensure that saved input file '${savedInputFileName}' does not exist!")
  if (EXISTS "${savedInputFileName}")
    message(FATAL_ERROR "The saved input file '${savedInputFileName}' exists when it should not!")
  endif()
endif()
