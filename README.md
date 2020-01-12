# Battleship

## Contents
* [Introduction](#introduction)
   * [Brief](#brief)
   * [Battleship Application](#battleship-application)
* [CI Pipeline](#ci-pipeline)
* [Documentation](#documentation)
* [Risk Assessment](#risk-assessment)
* [Testing and Coverage](#testing-and-coverage)
* [Future Improvements](#future-improvements)
* [Author](#author)

# Introduction

## Brief
The project brief was to make a system that automates the 
## Battleship Application
For service 2, it outputs a random letter between the letters 'a' to 'e' in lowercase; and for service 3, it outputs a random number between one and five. Thus this creates a five-by-five array,giving the users 25 coordinates to place their ships.
For service 4 get the outputs from both services and combine them to form a coordination. The program will check if the coordination matches any of the coordinates that contains a ship and if it does, it would return "You hit my battleship!" or "You miss my battleship!". The information gathered and outputted from service 4 will then be passed into the service 1 through json and service 1 will display the result on the web.

The front-page shows:


### CI Pipeline
The software used in this project include:
*Jenkins
*Ansible
*Docker and Docker Swarm 

Ansible, Jenkins and the flask services have a VM of their own. 

Jenkins VM ssh into the flask services VM and automate the build of docker-compose. 

![ci][ci]

##Documentation

![trello][trello]


## Risk Assessment

![RiskAssessment][riskassessment]

## Testing and Coverage 
Two tests have been conducted, one for service 2 to test if it outputs a random between the letters 'a' to 'e' in lowercase; and another for service 3 to test if the output is between one and five.
Service 1 and 4 depends on other services, hence it wasn’t possible to test them both.
The database was tested on service 1.

![coverage][coverage]


## Future Developmenti

## Authors
Simon Chen

### Links:
* Trello: https://trello.com/b/PUBvtaAZ/individual-project-2
* Website: http://http://34.89.25.151:5000/

[ci]: https://i.imgur.com/2G7joFp.png
[riskassessment]: https://i.imgur.com/btY8HRY.png
[coverage]: https://i.imgur.com/WDaANiD.png
[trello]: https://i.imgur.com/etDOlwa.png
