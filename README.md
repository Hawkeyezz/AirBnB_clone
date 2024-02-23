# This is a team project on AirBnB clone - The console, but i did solo on the project.

# Welcome to the AirBnB clone project!
First step: i'll Write a command interpreter to manage my AirBnB objects.

This is the first step towards building my first full web application: the AirBnB clone. This first step is very important because i'll will use what i build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

# What’s a command interpreter?
just like the shell, It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object.

# Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# This project implements some of the features of the AirBnB website. It covers the fundamental concepts of the high level programming track. The features are the following:

# FEATURES

# Command Interpreter
Description!
The Command Interpreter is used to manage the whole application's functionality from the command line, such as:

Create a new object.
Retrieve an object from a file, database, etc.
Execute operation on objects. e.g. Count, compute statistics, etc.
Update object's attributes.
Destroy an object.
Usage
To launch the console application in interactive mode simply run:

console.py 

or to use the non-interactive mode run:

echo "your-command-goes-here" | ./console.py

# Commands
Commands	Description	Usage
help or ?	Displays the documented commands.	help
quit	Exits the program.	quit
EOF	Ends the program. Used when files are passed into the program.	N/A
create	Creates a new instance of the <class_name>. Creates a Json file with the object representation. and prints the id of created object.	create <class_name>
show	Prints the string representation of an instance based on the class name and id.	show <class_name class_id>
destroy	Deletes and instance base on the class name and id.	destroy <class_name class_id>
all	Prints all string representation of all instances based or not on the class name	all or all <class_name class_id>
update	Updates an instance based on the class name and id by adding or updating attribute	update <class_name class_id key value>

# Tests
If you wish to run at the test for this application all of the test are located under the test/ folder and can execute all of them by simply running:

python3 -m unittest discover tests 

from the root directory.
