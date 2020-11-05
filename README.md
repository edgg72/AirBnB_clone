<p align="center">
  <img src="https://console.kr-asia.com/wp-content/uploads/2019/04/Airbnb-M-Size-3-1175x500.jpg"/>
</p>
<p align="center">
  <img src="https://www.holbertonschool.com/holberton-logo.png" width="360"/>
         <br>

<h1 align="center">AirBnB Console</h1>

> Starting the amazing project of AirBnB.

The goal of the project is to deploy on your server a simple copy of the AirBnB website.
In this project we have a command interpreter to manipulate data without a visual interface.

## The console

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

Files and Directories

* `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* `tests` directory will contain all unit tests.
* `console.py` file is the entry point of our command interpreter.
* `models/base_model.py` file is the base class of all our models. It contains common elements:
	* attributes: `id`, `created_at` and `updated_at`
	* methods: `save()` and `to_json()`
* `models/engine` directory will contain all storage classes (using the same prototype). For the moment you will have only one: `file_storage.py`.

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

* Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
* Provide default value of any attribute
* In the future, provide the same model behavior for file storage or database storage

## File storage == JSON serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:

* convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method `my_instance.to_json()` to retrieve a dictionary
* convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a `my_string = JSON.dumps(my_dict)`
* write this string to a file on disk

And the process of deserialization?

The same but in the other way:

* read a string from a file on disk
* convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a `my_dict = JSON.loads(my_string)`
* convert this data structure to instance - for us it will be a `my_instance = MyObject(my_dict)`

## What’s a command interpreter?
We want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Execution

Your command interpreter should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<p align="center">
  <img src="https://i.imgur.com/di7Ffnb.png"/>
</p>


## Example of use

Here is an example to use `all`, `show`, `create`, `update` and `destroy`

```
rockstarteam@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

---
### :memo: - Files

#|Files|Description
---|---|---
1|[README.md](./README.md)| description of the project and description of the command interpreter
2|[AUTHORS](./AUTHORS)|  individuals having contributed content to this repository
3|[console.py](./console.py)|  individuals having contributed content to this repository
4|[models](./models)| contains all the classes (BaseModel, User, Amenity, Place, City, State, Review)
5|[tests](./tests)| contains all the tests for the classes (BaseModel, User, Amenity, Place, City, State, Review)

---

### :file_folder: Files - Directories Classes

#|Files|Description
---|---|---
4|[models](./models)| contains all the classes (BaseModel, User, Amenity, Place, City, State, Review)
4.1|[engine](./models/engine)| contain the class FileStorage
4.1.1|[`__init__.py`](./models/engine/__init__.py)| init file
4.1.2|[`file_storage.py`](./models/engine/file_storage.py)| FileStorage class that handles persistency
4.2|[`__init__.py`](./models/__init__.py)| init file
4.3|[`amenity.py`](./models/amenity.py)| Amenity class
4.4|[`base_model.py`](./models/base_model.py)| BaseModel class
4.5|[`city.py`](./models/city.py)| City class
4.6|[`place.py`](./models/place.py)| Place class
4.7|[`review.py`](./models/review.py)| Review class
4.8|[`state.py`](./models/state.py)| State class
4.9|[`user.py`](./models/user.py)| User class

### :file_folder: Files - Directories Classes

#|Files|Description
---|---|---
5|[tests](./tests)| contains all the tests for the classes (BaseModel, User, Amenity, Place, City, State, Review)
5.1|[test_models](./tests/test_models)| contain tests models
5.1.1|[`__init__.py`](./tests/test_models/__init__.py)| init file
5.1.2|[`test_amenity.py`](./tests/test_models/test_amenity.py)| Test for Amenity class
5.1.3|[`test_base_model.py`](./tests/test_models/test_base_model.py)| Test for BaseModel class
5.1.4|[`test_city.py`](./tests/test_models/test_city.py)| Test for City class
5.1.5|[`test_place.py`](./tests/test_models/test_place.py)| Test for Place class
5.1.6|[`test_review.py`](./tests/test_models/test_review.py)| Test for Review class
5.1.7|[`test_state.py`](./tests/test_models/test_state.py)| Test for State class
5.1.8|[`test_user.py`](./tests/test_models/test_user.py)| Test for User class
5.1.9|[test_engine](./tests/test_models/test_engine)| contain tests models for engine
5.1.9.1|[`__init__.py`](./tests/test_models/test_engine/__init__.py)| init file
5.1.9.2|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py)| Test for FileStorage class
5.2|[`__init__.py`](./models/engine/__init__.py)| init file
5.3|[`test_console.py`](./tests/test_console.py)| test for the console


> This repo has a main, devarias and ever branches

---
<p align="center">
    <h2 align="center">Made by, David Arias Fuentes</h2>
          <p align="center">
	          <a href="https://twitter.com/DavidDevArias" target="_blank">
		              <img alt="twitter_page" src="https://github.com/gedafu/readme-template/blob/master/images/twitter.png" style="float: center; margin-right: 10px" height="50" width="50">
			              </a>
				              <a href="https://www.linkedin.com/in/devarias/" target="_blank">
					                  <img alt="linkedin_page" src="https://github.com/gedafu/readme-template/blob/master/images/linkedin.png" style="float: center; margin-right: 10px" height="50"  width="50">
							          </a>
								          <a href="https://medium.com/@daviddevarias" target="_blank">
									              <img alt="medium_page" src="https://github.com/gedafu/readme-template/blob/master/images/medium.png" style="float: center; margin-right: 10px" height="50" width="50">
										              </a>
											            </p>
												    </p>
<p align="center">
    <h2 align="center">Made by, Ever Daniel Gonzalez</h2>
          <p align="center">
	          <a href="https://twitter.com/EverD_Gonzalez" target="_blank">
		              <img alt="twitter_page" src="https://github.com/gedafu/readme-template/blob/master/images/twitter.png" style="float: center; margin-right: 10px" height="50" width="50">
			              </a>
				              <a href="https://www.linkedin.com/in/ever-daniel-gonzalez-2b49881ab/" target="_blank">
					                  <img alt="linkedin_page" src="https://github.com/gedafu/readme-template/blob/master/images/linkedin.png" style="float: center; margin-right: 10px" height="50"  width="50">
							          </a>
								          <a href="https://medium.com/@edgg72" target="_blank">
									              <img alt="medium_page" src="https://github.com/gedafu/readme-template/blob/master/images/medium.png" style="float: center; margin-right: 10px" height="50" width="50">
										              </a>
											            </p>
												    </p>

<p align="center">
   <img src="https://www.holbertonschool.com/holberton-logo.png"
        alt="Flow chart"
	     style="float: left; margin-right: 10px;">
	     </p>
	     <p align="center">
	     <b>Holberton School - Colombia<b><br>
	     </p>
	     <p align="center">
	     <b>November, 2020.<b>
	     </p>