
PYTHON := ${PWD}/venv/bin/python3
PIP := ${PWD}/venv/bin/pip3

wget:
	wget -P ${PWD}/data https://www.dropbox.com/s/mchpweqebj9ppm2/part-00000.json.gz
	wget -P ${PWD}/data https://www.dropbox.com/s/wdpgftxdfglsir9/part-00001.json.gz
	wget -P ${PWD}/data https://www.dropbox.com/s/vuoauc5s1gqjw28/part-00002.json.gz
	wget -P ${PWD}/data https://www.dropbox.com/s/7c977bkn3opqpim/part-00003.json.gz
	wget -P ${PWD}/data https://www.dropbox.com/s/1k8mqupr3fwozf3/part-00004.json.gz 


venv:
	virtualenv venv -p python3.7

install: wget venv
	${PIP} install -r requirements.txt

clean: 
	sudo rm -rf venv data
