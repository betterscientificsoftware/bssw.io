#
# Helper functions
#

function(wikize_refs_diff_test TEST_NAME)

  cmake_parse_arguments(PARSE
    "COMPARE_SAVED_INPUT_FILE;LINK_CHECK_TEST" # options
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

  if (PARSE_LINK_CHECK_TEST AND (NOT ENABLE_LINK_CHECK_TESTS))
    set_tests_properties(${TEST_NAME} PROPERTIES DISABLED ON)
  endif()
   
endfunction()


#
# System-level tests of wikize_refs.py
#

get_filename_component(bsswioBaseDir "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)

set(ENABLE_LINK_CHECK_TESTS OFF CACHE BOOL
  "Enable tests that check links and therefore do cummunication")

# /dev/null won't work on Windows. Do we care?
# Would be nice if empty string was allowed.
# Use a string here that is unlikely to change as wikize_refs evolves.
# Note: True regular expressions do not appear to be supported.
# I tried to anchor the re to beginning of a line as in ^usage:...
# and that fails and (--warn) in the regex string created problems too.

wikize_refs_diff_test(wikize_refs_help
  INPUT_FILE /dev/null 
  ARGS --help
  PASS_REGULAR_EXPRESSION "usage: wikize_refs.py" )

wikize_refs_diff_test(wikize_refs_no_args_pass
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_wikizer.md
  OUTPUT_FILE test_wikizer-wikized.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_wikizer-wikized.md )

wikize_refs_diff_test(wikize_refs_alpha_labels
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_alpha_labels.md
  OUTPUT_FILE test_alpha_labels-generated.md
  ARGS -o test_alpha_labels-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_alpha_labels-wikized.md )

wikize_refs_diff_test(wikize_refs_anywhere_linkdefs
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_anywhere_linkdefs.md
  OUTPUT_FILE test_anywhere_linkdefs-generated.md
  ARGS -o test_anywhere_linkdefs-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_anywhere_linkdefs-wikized.md )

wikize_refs_diff_test(wikize_refs_rerun
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_rerun.md
  PASS_REGULAR_EXPRESSION "\"test_rerun.md\" is up to date. No changes will be made." )

wikize_refs_diff_test(wikize_refs_rerun_after_adding_link
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_rerun_after_adding_link.md
  OUTPUT_FILE test_rerun_after_adding_link-generated.md
  ARGS -o test_rerun_after_adding_link-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_rerun_after_adding_link-wikized.md )

wikize_refs_diff_test(wikize_refs_goodlinks
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_goodlinks.md
  OUTPUT_FILE test_goodlinks-generated.md
  ARGS -c 20 -o test_goodlinks-generated.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_goodlinks-wikized.md
  LINK_CHECK_TEST )

wikize_refs_diff_test(wikize_refs_badlinks1
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_badlinks.md
  ARGS -c 20
  PASS_REGULAR_EXPRESSION "Invalid URL:"
  LINK_CHECK_TEST )

wikize_refs_diff_test(wikize_refs_badlinks2
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_badlinks.md
  ARGS -c 20 -w
  PASS_REGULAR_EXPRESSION "Broken URL: \"https://github.com/markcmiller86/SAF/blob/master/src/safapi/docs/miller002.pdf\""
  LINK_CHECK_TEST )

wikize_refs_diff_test(wikize_refs_no_args_fail
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_unused_linkdefs.md
  PASS_REGULAR_EXPRESSION "Either correct above errors or run with -w")

wikize_refs_diff_test(wikize_refs_unused_linkdefs
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_unused_linkdefs.md
  PASS_REGULAR_EXPRESSION "['26', '16']" )

wikize_refs_diff_test(wikize_refs_nonexistent_linkdef
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_nonexistent_linkdef.md
  PASS_REGULAR_EXPRESSION "['aa', '26']" )

wikize_refs_diff_test(wikize_refs_too_many_footnotes
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_too_many_footnotes.md
  PASS_REGULAR_EXPRESSION "Extra footnotes beyond 3 between <sup>...</sup> at line 79" )

wikize_refs_diff_test(wikize_refs_smartquotes
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_smartquotes.md
  PASS_REGULAR_EXPRESSION "Replace smart/curly quotes in link definition at line 148 with straight quotes" )

wikize_refs_diff_test(wikize_refs_smartquotes_warn
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_smartquotes.md
  ARGS -w
  PASS_REGULAR_EXPRESSION "Replace smart/curly quotes in link definition at line 155 with straight quotes" )

wikize_refs_diff_test(wikize_refs_in_place
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_inplace.md
  OUTPUT_FILE test_inplace.md
  ARGS -w -i
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_inplace-wikized.md
  COMPARE_SAVED_INPUT_FILE )

wikize_refs_diff_test(wikize_refs_in_place_no_save_orig
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_inplace.md
  OUTPUT_FILE test_inplace.md
  ARGS -w -i -s
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_inplace-wikized.md)

wikize_refs_diff_test(wikize_refs_in_place_and_explicit_out_fail
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_wikizer.md
  ARGS -w -i -o test_wikizer-generated.md
  PASS_REGULAR_EXPRESSION "Can't set both -i and -o options" )

wikize_refs_diff_test(wikize_refs_linkdef_databases
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_linkdef_dbs_source.md
  OUTPUT_FILE test_linkdef_dbs_source-wikized.md
  ARGS -w -l ${bsswioBaseDir}/utils/tests/test_linkdef_dbs_database.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_linkdef_dbs_source-wikized.md )

wikize_refs_diff_test(wikize_refs_linkdef_databases_pure
  INPUT_FILE ${bsswioBaseDir}/utils/tests/test_linkdef_dbs_source_pure.md
  OUTPUT_FILE test_linkdef_dbs_source_pure-wikized.md
  ARGS -w -l ${bsswioBaseDir}/utils/tests/test_linkdef_dbs_database_pure.md
  EXPECTED_OUTPUT_FILE ${bsswioBaseDir}/utils/tests/test_linkdef_dbs_source_pure-wikized.md )
