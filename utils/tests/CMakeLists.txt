include(CMakePrintHelpers)

#
# Helper functions
#

function(wikize_refs_diff_test TEST_NAME)

  cmake_parse_arguments(PARSE
    "" # options
    "INPUT_FILE;OUTPUT_FILE;EXPECTED_OUTPUT_FILE" # one_value_arguments
    # multi_value_keywords
    "ARGS"
    # args
    ${ARGN}
    )

  #cmake_print_variables(TEST_NAME PARSE_INPUT_FILE PARSE_OUTPUT_FILE PARSE_ARGS PARESE_EXPECTED_OUTPUT_FILE)

   add_test(NAME ${TEST_NAME} COMMAND ${CMAKE_COMMAND}
     -D "TEST_NAME=${TEST_NAME}"
     -D "INPUT_FILE=${PARSE_INPUT_FILE}"
     -D "OUTPUT_FILE=${PARSE_OUTPUT_FILE}"
     -D "WIKIZE_REFS_ARGS=${PARSE_ARGS}"
     -D "EXPECTED_OUTPUT_FILE=${PARSE_EXPECTED_OUTPUT_FILE}"
     -P ${CMAKE_CURRENT_LIST_DIR}/run_wikize_ref_diff_test.cmake
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
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS "-w"  # Have to ignore some warnings!
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  )

wikize_refs_diff_test(wikize_refs_no_args_fail
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS # Allow error about missing refs
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  )
set_tests_properties(wikize_refs_no_args_fail PROPERTIES
  PASS_REGULAR_EXPRESSION "Correct above issues and re-try"
  )

wikize_refs_diff_test(wikize_refs_in_place
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS -w -i
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  )

wikize_refs_diff_test(wikize_refs_explicit_out
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach-generated.md
  ARGS -w -o ReferencesInMarkdownHybridApproach-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  )

