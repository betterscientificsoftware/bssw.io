#!/usr/bin/env bash

debug_flag=""

echo ""

echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/WhatIsVersionControl.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/WhatIsPerfPortabilityForCseApps.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/SwTestingTutorials.Cse.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/SwTestingTutorials.General.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/SwTestingTutorials.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/TestDrivenDevptInScientificSwASurvey.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} --color=tty -s metadata_spec.txt -f ../CuratedContent/BestPracticesForHPCSwDevelopersWebinarSeries.md


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} -f test_data/test_file_001.md -s metadata_spec.txt --color=tty


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} -f test_data/test_file_002.md -s metadata_spec.txt --color=tty


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} -f test_data/test_file_003.md -s metadata_spec.txt --color=tty


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} -f test_data/test_file_004.md -s metadata_spec.txt --color=tty


echo "================================================================================"
echo ""
python validate_article.py ${debug_flag} -f test_data/test_file_005.md -s metadata_spec.txt --color=tty

