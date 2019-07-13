# smart_alarm

## Introduction
smart_alarm is a small IoT project with the focus on getting me out of my bed everyday, it utilizes:
* Raspberry Pi 3+ and Pi camera
* Google Vision API 
* flask
* crontabs
* Lifx lightbulb
* lifxlan, python API library for Lifx lightbulb

Using these components, the web application can list alarms, setup new alarms and delete alarms. The application will update crontabs in each operation; these crontabs will be used to run the script for the smart_alarm

## Requirements
Inorder to run this, you must have:
* A Rasperberry Pi and a Pi camera
* Google Cloud Platform key with Vision API enabled
* A Lifx lightbulb

## Running the code
Getting the Google Cloud Platform secret key:
* Follow this [link](https://codelabs.developers.google.com/codelabs/cloud-vision-intro/index.html?index=..%2F..cloudai#2) and do steps 3-6.
* Download and copy the api key to the smart_alarm repository.

Set-up:
1. sudo pip install virtualenv virtualenvwrapper
2. sudo rm -rf ~/get-pip.py ~/.cache/pip
3. export WORKON_HOME=$HOME/.virtualenvs
4. export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
5. source /usr/local/bin/virtualenvwrapper.sh
6. source ~/.profile
7. mkvirtualenv smart_alarm -p python3
8. workon smart_alarm
9. pip install -r requirements.txt
10. cd web_app
11. python app.py

## Note
There might be some errors because of the unique way each raspberry pi is configured.
Contact me on GitHub if you want tips to get the application working.
