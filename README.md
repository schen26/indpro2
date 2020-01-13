# Battleship Solver

## Brief
The project brief was to make a service-orientated architecture, which contains four services:
* Service 1- core service, render Jinja2 template, SQL database
* Service 2 and 3- generate random objects
* Service 4- creates an object based on the previous two services 
The services also need to have two implementations and are able to switch between the two without any disruptions to the user. 


## Battleship Solver Application
For Service 2, it outputs a random letter between the letters 'a' to 'e' in lowercase; and for Service 3, it outputs a random number between one and five. Thus this creates a five-by-five array, giving the users 25 coordinates to place their ships. Within this array there is one ship of length 4 in located in a1, b2, c3 and d4, this is stored in a list inside Service 4.

For Service 4, it gets the outputs from Service 2 and 3, and combines them to form a coordinate. The application will check list of coordinates that contains part of a ship and if it does, it would return "You hit my battleship!" or "You miss my battleship!" if it doesn’t. 

The information gathered and outputted from Service 4 will then be passed into the service 1 through json and service 1 will display the result on the web. Service 1 is also where the coordinates are stored in mySQL.

* Website: http://http://34.89.25.151:5000/

### CI Pipeline
The CI tools and software used in this project include:
* CI Server Jenkins 
* Ansible for Configuration Management
* GCP VMs
* Docker and Docker Swarm 
* Trello Kanban board 
* Git Version Control 

Jenkins and the Flask Services have a VM of their own. 
Jenkins webhooks any changes made on the application from Github. 
On Jenkins VM, it contains Jenkins and Docker Registry. Jenkins automates the build of the images and places it into the registry.
Jenkins then ssh into the Flask-Services VM, which is a manager node in Docker Swarm and node creates Docker Stack and deploy the services if needed.
Ideally Ansible should be on another VM, however it is placed in the Flask-Service VM for ease of assessing the entire application.

## Documentation
The following are documentation from Trello in order to keep track of the project progress, and a Risk Assessment matrix.

### Trello

* Trello: https://trello.com/b/PUBvtaAZ/individual-project-2

### Risk Assessment

* Risk Assessment: https://docs.google.com/spreadsheets/d/1oo7wguKR8sefzVaVCjLgZnzoyaDsgtlERXG5RS0uxJ8/edit#gid=0

## Testing and Coverage 
Three unit tests have been conducted through pytest for Service 1, 2 and 3. All passed with a coverage of 49%, 90% and 89% respectively.
Service 4 requires on Services 1 and 2 to run to test the output, hence it wasn’t possible to test it without further configuration of the environment.
The database was tested on Service 1 for its ability to add to the database.

* Presentation: https://docs.google.com/presentation/d/1KqmrXVLW7X2874goL3qRIz_XFjn9wPi7bLrORbKw5xM/edit#slide=id.g76613142fe_0_21

## Future Development
There are some issues within this application that can be resolved if more time is given, these include:
* The game doesn’t stop when all parts of the ship has been hit.
* The game doesn’t stop after all coordinations has been hit.
* The coordinates repeat itself, hence it would take longer to complete the solve. 
* Tests to be created for Service 4.
* More tests for Service 1, 2 and 3. 

## Conclusion
By utilising what has been taught in the previous project, in addition to other CI tools after that, it resulted in the creation of this project; which is a battleship solver that will identify the location of the coordinates that contain part of the ship. 
The tools allowed me to implement my code to different machines and environments without having to worry if the application will run or not.
Three tests are conducted with a coverage of 49%, 90% and 89% for Service 1, 2 and 3 respectively. 
Further improvements on the project are needed such as additional features, to make the application more like the actual game. 

## Author
Simon Chen

