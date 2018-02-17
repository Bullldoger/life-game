#!/usr/bin/env bash


find life/ -iname "*.py" | xargs pylint --rcfile=.pylintrc >> reports/pylint_report.txt
cat reports/pylint_report.txt

cd docs/
sphinx-apidoc -f -o source/ ../
make html
cd ../