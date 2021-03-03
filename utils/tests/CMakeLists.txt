#
# Helper functions
#

function(wikize_refs_diff_test TEST_NAME)

  cmake_parse_arguments(PARSE
    "COMPARE_SAVED_INPUT_FILE" # options
    "INPUT_FILE;OUTPUT_FILE;EXPECTED_OUTPUT_FILE;PASS_REGULAR_EXPRESSION" # one_value_arguments
    "ARGS" # multi_value_keywords
    ${ARGN} # args
    )

   add_test(NAME ${TEST_NAME} COMMAND ${CMAKE_COMMAND}
     -D "TEST_NAME=${TEST_NAME}"
     -D "INPUT_FILE=${PARSE_INPUT_FILE}"
     -D "WIKIZE_REFS_ARGS=${PARSE_ARGS}"
     -D "OUTPUT_FILE=${PARSE_OUTPUT_FILE}"
     -D "EXPECTED_OUTPUT_FILE=${PARSE_EXPECTED_OUTPUT_FILE}"
     -D "COMPARE_SAVED_INPUT_FILE=${PARSE_COMPARE_SAVED_INPUT_FILE}"
     -P ${CMAKE_CURRENT_LIST_DIR}/run_wikize_ref_diff_test.cmake )

   set(passRegex "RUN_WIKIZE_REF_DIFF_TEST: ALL PASSED")
   if (PARSE_PASS_REGULAR_EXPRESSION)
     set(passRegex "${PARSE_PASS_REGULAR_EXPRESSION}")
   endif()
   set_tests_properties(${TEST_NAME} PROPERTIES PASS_REGULAR_EXPRESSION "${passRegex}")

endfunction()


#
# System-level tests of wikize_refs.py
#

get_filename_component(bsswioBaseDir "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)

wikize_refs_diff_test(wikize_refs_help
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  ARGS --help
  PASS_REGULAR_EXPRESSION "Re-formats a series of reference style links in a GitHub Markdown file" )

wikize_refs_diff_test(wikize_refs_no_args_pass
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach-wikized.md
  ARGS -w   # Have to ignore some warnings!
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md )

wikize_refs_diff_test(wikize_refs_no_args_fail
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  PASS_REGULAR_EXPRESSION "Correct above issues and re-try" )

wikize_refs_diff_test(wikize_refs_in_place
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS -w -i
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  COMPARE_SAVED_INPUT_FILE )

wikize_refs_diff_test(wikize_refs_in_place_no_save_orig
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS -w -s -i
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md )

wikize_refs_diff_test(wikize_refs_explicit_out
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach-generated.md
  ARGS -w -o ReferencesInMarkdownHybridApproach-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md )

wikize_refs_diff_test(wikize_refs_in_place_and_explicit_out_fail
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  ARGS -w -i -o ReferencesInMarkdownHybridApproach-generated.md
  PASS_REGULAR_EXPRESSION "Can't set both -i and -o options" )
