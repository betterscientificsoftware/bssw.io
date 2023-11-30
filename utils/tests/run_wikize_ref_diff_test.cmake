#
# CMake -P script to run a system-level test of the wikize_refs.py script
#
# Usage:
#
#  cmake \
#    -D TEST_NAME=<testName> \
#    -D INPUT_FILE=<inputFile> \
#    -D WIKIZE_REFS_ARGS=<wikizeRefsArgs> \
#    [-D COMPARE_SAVED_INPUT_FILE=[TRUE|FALSE\] \
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
# If COMPARE_SAVED_INPUT_FILE=TRUE is passed in, then the saved original file
# name(<inputFile>)~ will be compared to the original <inputFile> to make sure
# the original file is saved.  If COMPARE_SAVED_INPUT_FILE=FALSE, then the file
# name(<inputFile>)~ cannot exist after running wikize_refs.py or an error
# will be recorded.
#
# If the wikize_refs.py command runs to completion without error and the diff
# of the output file against the expected output file returns no change, then
# this CMake -P script will return 0.  Otherwise, it will return non-zero and
# print the error to STDOUT.
#


#
# Helper functions
#


function(diff_files fileName1 fileName2)
  message("Diffing '${fileName1}' and '${fileName1}'")
  execute_process(
    COMMAND diff "${fileName1}" "${fileName2}"
    WORKING_DIRECTORY "${TEST_NAME}"
    RESULT_VARIABLE diffRtnCode
    )
  if (NOT diffRtnCode EQUAL 0)
    message(FATAL_ERROR "diff returned '${diffRtnCode}'")
  endif()
endfunction()

# NOTE: Above, we could make this work on all platforms by switching to use:
#
#  cmake -E compare_files <fileName1> <fileName2>
#
# but that command does not return the actually diff, only if the files match
# or don't match.  So if the diff fails, you get no useful output at all.
# That is not good for an automated test.


#
# Main
#

get_filename_component(inputFileName "${INPUT_FILE}" NAME)

# A) Set up test directory to hold the input and output files

if (EXISTS ${TEST_NAME})
  message("Removing dir ${TEST_NAME}")
  file(REMOVE_RECURSE "${TEST_NAME}")
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
  diff_files("${EXPECTED_OUTPUT_FILE}" "${OUTPUT_FILE}")
else()
  message("Skipping diff of output file since no expected output given!")
endif()

# E) Compared the saved input file

set(savedInputFileName "${inputFileName}~")

if (COMPARE_SAVED_INPUT_FILE)
  diff_files( "${INPUT_FILE}" "${savedInputFileName}")
else()
  if (EXISTS "${savedInputFileName}")
    message(FATAL_ERROR "The saved input file '${savedInputFileName}' exists when it should not!")
  else()
    message("Saved input file '${savedInputFileName}' does not exist!")
  endif()
endif()

# F) Report all passed!

# If we get here, then we did not detect any errors!
message("RUN_WIKIZE_REF_DIFF_TEST: ALL PASSED!")

# NOTE: By printing 'ALL PASSED' and grepping for that, we ensure that this
# script runs to completion with no fatal errors.  That is a stronger check
# that just checking the return code.
