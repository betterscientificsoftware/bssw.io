#!/usr/bin/env bash

echo ""
echo "================================================================================"
echo ""
python validate_article.py -V --color=tty -f ../CuratedContent/WhatIsVersionControl.md
echo ""
echo "================================================================================"
echo ""
python validate_article.py -V --color=tty -f ../CuratedContent/WhatIsPerfPortabilityForCseApps.md
echo ""
echo "================================================================================"
echo ""
python validate_article.py -V --color=tty -f ../CuratedContent/SwTestingTutorials.Cse.md
echo ""
echo "================================================================================"
echo ""
python validate_article.py -V --color=tty -f ../CuratedContent/SwTestingTutorials.General.md
echo ""
echo "================================================================================"
echo ""
python validate_article.py -V --color=tty -f ../CuratedContent/SwTestingTutorials.md
echo ""
echo "================================================================================"
echo ""
python validate_article.py -V --color=tty -f ../CuratedContent/TestDrivenDevptInScientificSwASurvey.md


