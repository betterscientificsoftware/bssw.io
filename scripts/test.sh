#!/usr/bin/env bash

echo ""

#echo "================================================================================"
#echo ""
#python validate_article.py -V --color=tty -f ../CuratedContent/WhatIsVersionControl.md
#echo ""

#echo "================================================================================"
#echo ""
#python validate_article.py -V --color=tty -f ../CuratedContent/WhatIsPerfPortabilityForCseApps.md
#echo ""

#echo "================================================================================"
#echo ""
#python validate_article.py -V --color=tty -f ../CuratedContent/SwTestingTutorials.Cse.md
#echo ""

#echo "================================================================================"
#echo ""
#python validate_article.py -V --color=tty -f ../CuratedContent/SwTestingTutorials.General.md
#echo ""

#echo "================================================================================"
#echo ""
#python validate_article.py -V --color=tty -f ../CuratedContent/SwTestingTutorials.md
#echo ""

#echo "================================================================================"
#echo ""
#python validate_article.py -D --color=tty -f ../CuratedContent/TestDrivenDevptInScientificSwASurvey.md


#echo "================================================================================"
#echo ""
# python validate_article.py -D --color=tty -f ../CuratedContent/BestPracticesForHPCSwDevelopersWebinarSeries.md


echo "================================================================================"
echo ""
python validate_article.py -f test_file_001.md -s metadata_spec.txt -D --color=tty

echo "================================================================================"
echo ""
python validate_article.py -f test_file_002.md -s metadata_spec.txt -D --color=tty

echo "================================================================================"
echo ""
python validate_article.py -f test_file_003.md -s metadata_spec.txt -D --color=tty


