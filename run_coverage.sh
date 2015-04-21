export PYTHONPATH=/home/azazello/DuckTags/Test:/home/azazello/DuckTags

rm -f .coverage
coverage run `pwd`/Test/DuckTagsUnitTests.py
coverage html --omit=/usr/local/lib/python2.7/*
