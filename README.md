# AirBnB Clone [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/luischaparroc/AirBnB_clone/blob/master/LICENSE)
![HBnB Logo](./image/hbnb_logo.png)


### Contents

- [Description](#description-pagefacingup)
- [Technology used](#technology-used-gear)
- [Requirements](#requirements-memo)
- [Repo Contents](#repo-contents-clipboard)
- [Installation](#installation-hammerandwrench)
- [Usage](#usage-wrench)
- [Example](#example)
- [Further Information](#further-information-bookmarktabs)

## Description :page_facing_up:
This is the first step towards building an AirBnB clone. A command line interpreter(console) is built to help create objects and manipulat AirBnB objects. The console has the ability to do the following:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


## Technology used :gear:
The console was developed in
* Environment: Ubuntu 20.04LTS
* Language: python3 (version 3.8.10)
* Style guide: pycodestyle


## Requirements :memo:
* Knowledge in python3
* how to use a command line interpreter
* Ubuntu 20.04, python3 and pep8 style corrector installed

## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/Timadey/AirBnB_clone.git
$ Cloning into 'AirBnB_clone'...
$ ......
$ ./console.py

```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

###### Example

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
Welcome to AirBnb clone console(CLI)
    This console helps to manipulate objects used in this project
    Source code: https://github.com/Timadey/AirBnB_clone.git
    Run `help` to show available command
    `help command` to show detailed usage of command

// Create new user object
(hbnb) create User
71d6e089-099c-4a7b-95c4-efcaff61cdd7

// Read that User object
(hbnb) show User 71d6e089-099c-4a7b-95c4-efcaff61cdd7
{'id': '71d6e089-099c-4a7b-95c4-efcaff61cdd7', 'created_at': '2022-09-03T21:40:07.723677', 'updated_at': '2022-09-03T21:40:07.723677', '__class__': 'User'}

// Update the User object
(hbnb) update User 71d6e089-099c-4a7b-95c4-efcaff61cdd7
** attribute name missing **
(hbnb) update User 71d6e089-099c-4a7b-95c4-efcaff61cdd7 name "Timadey"

// Check that update was done
(hbnb) show User 71d6e089-099c-4a7b-95c4-efcaff61cdd7
{'id': '71d6e089-099c-4a7b-95c4-efcaff61cdd7',
'created_at': '2022-09-03T21:40:07.723677',
'updated_at': '2022-09-03T21:42:01.196758',
 'name': 'Timadey', '__class__': 'User'}

// Read all objects
(hbnb) all
["[BaseModel] (72132fac-8071-4837-a82c-cd6ff6d77cef)
{'id': '72132fac-8071-4837-a82c-cd6ff6d77cef', 'created_at': datetime.datetime(2022, 8, 31, 22, 35, 47, 154823), 'updated_at': datetime.datetime(2022, 9, 2, 17, 18, 34, 396999),
'name': 'My_First_Model', 'my_number': 89, 'email': 18383.322, 'email_alias': '89'}", ...,
"[User] (71d6e089-099c-4a7b-95c4-efcaff61cdd7)
{'id': '71d6e089-099c-4a7b-95c4-efcaff61cdd7',
'created_at': datetime.datetime(2022, 9, 3, 21, 40, 7, 723677),
'updated_at': datetime.datetime(2022, 9, 3, 21, 40, 7, 723677)}"]

// Read all Users
(hbnb) all User
["[User] (6932c087-6d06-4821-9189-7ea19319163e)
{'id': '6932c087-6d06-4821-9189-7ea19319163e', 'created_at': datetime.datetime(2022, 9, 3, 20, 18, 4, 553033),
'updated_at': datetime.datetime(2022, 9, 3, 20, 18, 4, 553033)}", ..., "[User] (71d6e089-099c-4a7b-95c4-efcaff61cdd7)
{'id': '71d6e089-099c-4a7b-95c4-efcaff61cdd7', 'created_at': datetime.datetime(2022, 9, 3, 21, 40, 7, 723677),
'updated_at': datetime.datetime(2022, 9, 3, 21, 42, 1, 196758), 'name': 'Timadey'}"]

// Destroy User
(hbnb) destry User 71d6e089-099c-4a7b-95c4-efcaff61cdd7
*** Unknown syntax: destry User 71d6e089-099c-4a7b-95c4-efcaff61cdd7
(hbnb) destroy User 71d6e089-099c-4a7b-95c4-efcaff61cdd7

// Check that User was destroyed successfully
(hbnb) show User 71d6e089-099c-4a7b-95c4-efcaff61cdd7
** no instance found **

// Exit console using quit or CTRL-D
(hbnb) quit
Bye

```

### Further information :bookmark_tabs:
Each module and methods are well documented with docstrings.
For further information and documentation visit [python.org](https://www.python.org/).


### Authors :fountain_pen:
* [Timothy Adeleke](https://www.linkedin.com/in/timadey)
* Mohzaey Balogun
