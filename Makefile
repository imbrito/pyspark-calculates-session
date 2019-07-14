
PYTHON := ${PWD}/venv/bin/python3
PIP := ${PWD}/venv/bin/pip3

wget:
	wget -P ${PWD}/data https://s3.amazonaws.com/grupozap-data-engineer-test/part-00000.json.gz 
	wget -P ${PWD}/data https://s3.amazonaws.com/grupozap-data-engineer-test/part-00001.json.gz 
	wget -P ${PWD}/data https://s3.amazonaws.com/grupozap-data-engineer-test/part-00002.json.gz 
	wget -P ${PWD}/data https://s3.amazonaws.com/grupozap-data-engineer-test/part-00003.json.gz 
	wget -P ${PWD}/data https://s3.amazonaws.com/grupozap-data-engineer-test/part-00004.json.gz 

venv:
	virtualenv venv -p python3.7

install: wget venv
	${PIP} install -r requirements.txt

clean: 
	sudo rm -rf venv data
