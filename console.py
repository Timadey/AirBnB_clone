#!/usr/bin/python3
"""
Command Line Interpreter for performing administrative operations
on AirBnb objects
"""
import cmd
from shlex import split

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State

from models import storage


class HBNBCommand(cmd.Cmd):
    """The command line interpreter (CLI) for performing administrative
    operations on AirBnB objects. It imports the cmd.Cmd class which is
    a framework for writing line-oriented command interpreters.
    It supports the following, operations; create, read, update, delete

    """
    _classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "Amenity": Amenity,
    }
    _commands = ["create", "update", "show", 'all', 'destroy', 'count']
    prompt = "(hbnb) "
    intro = """Welcome to AirBnb clone console(CLI)
    This console helps to manipulate objects used in this project
    Source code: https://github.com/Timadey/AirBnB_clone.git
    Run `help` to show available command
    `help command` to show detailed usage of command
    """

    def precmd(self, line: str) -> str:
        """Parse command input before execution"""
        if '.' in line and '(' in line and ')' in line:
            cls = line.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')
            if cls[0] in self._classes.keys() and cmd[0] in self._commands:
                line = cmd[0] + ' ' + cls[0] + ' ' + args[0]
        return line

    def do_count(self, cls_name):
        """Prints the number of instances a class has in storage
        Usage: [class name].count()
        Example: User.count()
        """
        count = 0
        objects = storage.all()
        for key in objects.keys():
            class_name = key.split('.')
            if class_name[0] == cls_name:
                count = count + 1
        print(count)

    def emptyline(self):
        """What the command line should when an empty line is inputted
        and ENTER key pressed. In other word, this method runs when
        the user doesn't give any input

        """
        pass

    def get_instance(self, line) -> "(tuple[str, dict, list]) | None":
        """Get an instance attributes from storage using the class name and id

        Return a tuple containing the key and attributes of the instance
        in the storage with a list of the parsed line or None if not found
        """
        line = split(line)
        if len(line) < 1:
            print("** class name missing **")
            return None
        elif len(line) < 2:
            print("** instance id missing **")
            return None
        else:
            if not self._classes.get(line[0]):
                print("** class doesn't exist **")
                return None
            key = f"{line[0]}.{line[1]}"
            class_dict = storage.all().get(key)
            if class_dict is None:
                print("** no instance found **")
                return None
            return key, class_dict, line

    @staticmethod
    def cast_type(obj):
        """Returns the real value of an object in a string"""
        try:
            return eval(obj)
        except Exception:
            return obj

    def do_quit(self, line):
        """Command to quit or exit the command line"""
        print("Bye")
        return True

    def do_EOF(self, line):
        """Exit the interpreter when an EOF is entered"""
        print("Bye")
        return True

    def do_create(self, line):
        """Create a new instance of a class and save the instance in storage
        Usage: ``create [class name]``
        Example: ``create BaseModel``
        Prints the id of the new class created to stdout
        """
        if line == '':
            print("** class name missing **")
        else:
            try:
                instance = self._classes.get(line)()
                storage.save()
                print(instance.id)
            except TypeError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Print the string representation of an instance

        Usage: ``show [class name] [instance id]``
        Example: ``show BaseModel 3b846d84-b15b-4eb2-928f-939621b5fbb1``
        Prints the string representation of BaseModel with id
        3b846d84-b15b-4eb2-928f-939621b5fbb1
        """
        class_instance = self.get_instance(line)
        if class_instance is not None:
            print(class_instance[1])

    def do_destroy(self, line):
        """Deletes an instance from storage
        given the class name and instance id

        Usage: ``destroy [class name] [insatnce id]``
        Example: ``destroy BaseModel 3b846d84-b15b-4eb2-928f-939621b5fbb1``
        """
        class_instance = self.get_instance(line)
        if class_instance is not None:
            del storage.all()[class_instance[0]]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances in the storage
        Based or not on the class name
        Usage: all [-class name] #: class name is optional
        Example:
            all #: print all instances
            all BaseModel #:print all "BaseModel" instances
        """
        line = self.parseline(line)
        all_instances = storage.all()
        instance_list = []
        if line[0] is not None:
            class_name = self._classes.get(line[0])
            if class_name is None:
                print("** class doesn't exist **")
                return
            else:
                for key in list(all_instances.keys()):
                    if line[0] in key:
                        instance = class_name(**all_instances.get(key))
                        instance_list.append(str(instance))
        else:
            for key in list(all_instances.keys()):
                class_name = self._classes.get(key.split(".")[0])
                instance = class_name(**all_instances.get(key))
                instance_list.append(str(instance))
        print(instance_list)

    def do_update(self, line):
        """Update an instance based on the class name and id
        By adding or updating the attribute and saveing to storage

        Usage: update [class name] [id] [attribute name] [attribute value]
        Example: update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Note: The following rules must be adhered to
            * Arguments must be in the right order
            * Each arguments are separated by a space
            * A string argument with a space must be between double quote
            * The error management starts from the first argument to
            the last one
        """
        class_instance = self.get_instance(line)
        if class_instance is None:
            return
        line = class_instance[2][2:]
        if len(line) < 1:
            print("** attribute name missing **")
            return
        if len(line) < 2:
            print("** value missing **")
            return
        attr_name, attr_value = line[0], line[1]
        class_name = self._classes.get(class_instance[2][0])
        instance = class_name(**class_instance[1])
        instance.__setattr__(attr_name, self.cast_type(attr_value))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
