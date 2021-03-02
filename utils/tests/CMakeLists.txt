include(CMakePrintHelpers)

#
# Helper functions
#

function(wikize_refs_diff_test TEST_NAME)

  cmake_parse_arguments(PARSE
    "" # options
    "INPUT_FILE;OUTPUT_FILE;ARGS;EXPECTED_OUTPUT_FILE" # one_value_arguments
    # multi_value_keywords
    ""
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

wikize_refs_diff_test(wikize_refs_no_args
  INPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach.md
  OUTPUT_FILE ReferencesInMarkdownHybridApproach.md
  ARGS "-w"  # Have to ignore some warnings!
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md
  )
