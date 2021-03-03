include(CMakePrintHelpers)

#
# Helper functions
#

function(wikize_refs_diff_test TEST_NAME)

  cmake_parse_arguments(PARSE
    "COMPARE_SAVED_INPUT_FILE" # options
    "INPUT_FILE;OUTPUT_FILE;EXPECTED_OUTPUT_FILE" # one_value_arguments
    "ARGS" # multi_value_keywords
    ${ARGN} # args
    )

  #cmake_print_variables(TEST_NAME PARSE_INPUT_FILE PARSE_OUTPUT_FILE PARSE_ARGS PARESE_EXPECTED_OUTPUT_FILE)

   add_test(NAME ${TEST_NAME} COMMAND ${CMAKE_COMMAND}
     -D "TEST_NAME=${TEST_NAME}"
     -D "INPUT_FILE=${PARSE_INPUT_FILE}"
     -D "WIKIZE_REFS_ARGS=${PARSE_ARGS}"
     -D "OUTPUT_FILE=${PARSE_OUTPUT_FILE}"
     -D "EXPECTED_OUTPUT_FILE=${PARSE_EXPECTED_OUTPUT_FILE}"
     -D "COMPARE_SAVED_INPUT_FILE=${PARSE_COMPARE_SAVED_INPUT_FILE}"
     -P ${CMAKE_CURRENT_LIST_DIR}/run_wikize_ref_diff_test.cmake
     )
  set_tests_properties(${TEST_NAME} PROPERTIES
    PASS_REGULAR_EXPRESSION "RUN_WIKIZE_REF_DIFF_TEST: ALL PASSED"
    )

endfunction()


#
# System-level tests of wikize_refs.py
#

get_filename_component(bsswioBaseDir "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)

wikize_refs_diff_test(wikize_refs_help
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  ARGS --help
  )
set_tests_properties(wikize_refs_help PROPERTIES
  PASS_REGULAR_EXPRESSION "Re-formats a series of reference style links in a GitHub Markdown file"
  )

wikize_refs_diff_test(wikize_refs_no_args_pass
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach-wikized.md
  ARGS -w   # Have to ignore some warnings!
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  )

wikize_refs_diff_test(wikize_refs_no_args_fail
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  )
set_tests_properties(wikize_refs_no_args_fail PROPERTIES
  PASS_REGULAR_EXPRESSION "Correct above issues and re-try"
  )

wikize_refs_diff_test(wikize_refs_in_place
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS -w -i
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  COMPARE_SAVED_INPUT_FILE
  )

wikize_refs_diff_test(wikize_refs_in_place_no_save_orig
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS -w -s -i
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  # There will be no input file saved here!
  )

wikize_refs_diff_test(wikize_refs_explicit_out
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach-generated.md
  ARGS -w -o ReferencesInMarkdownHybridApproach-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  # There will be no input file saved here!
  )


# ToDo: Add arg PASS_REGULAR_EXPRESSION into function wikize_refs_diff_test() ...

# ToDo: Add test for -i and -o both being set which is an error