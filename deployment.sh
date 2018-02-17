#!/usr/bin/env bash


find life/ -iname "*.py" | xargs pylint --rcfile=.pylintrc >> reports/pylint_report.txt
cat reports/pylint_report.txt

find tests/ -iname "*.py" | xargs py.test --junitxml reports/tests_report.xml


sphinx-apidoc -f -o docs/source/ life/
cd docs/
make html
cd ../

git add .
git commit -m "Changes upload"
git push