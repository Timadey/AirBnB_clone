#!/usr/bin/python3
"""
Command interpreter for performing administrative operations
on AirBnb objects
"""
import cmd
import sys

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The command interpreter for performing administrative
    operations on AirBnB objects. It imports the cmd.Cmd class which is
    a framework for writing line-oriented command interpreters.

    """
    classes = {
        "BaseModel": BaseModel,
    }
    prompt = "(hbnb) "

    def emptyline(self):
        """What the command line should when an empty line is inputted
        and ENTER key pressed. In other word, this method runs when the user doesn't give
        any input

        """
        pass

    def get_instance(self, line) -> "(tuple[str, dict]) | None":
        """Get an instance attributes from storage using the class name and id

        Return a tuple containing the key and attributes of the instance
        in the storage or None if not found
        """
        line = self.parseline(line)
        if line[0] is None or line[0] == '':
            print("** class name missing **")
            return None
        elif line[1] is None or line[1] == '':
            print("** instance id missing **")
            return None
        else:
            if not self.classes.get(line[0]):
                print("** class doesn't exist **")
                return None
            key = f"{line[0]}.{line[1]}"
            class_dict = storage.all().get(key)
            if class_dict is None:
                print("** no instance found **")
                return None
            return key, class_dict

    def do_quit(self, line):
        """Command to quit or exit the command line"""
        print("Bye")
        sys.exit(0)

    def do_EOF(self, line):
        """Exit the interpreter when an EOF is entered"""
        self.do_quit(line)

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
                new_class = self.classes.get(line)()
                new_class.save()
                print(new_class.id)
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
        """Deletes an instance from storage given the class name and instance id

        Usage: ``destroy [class name] [insatnce id]``
        Example: ``destroy BaseModel 3b846d84-b15b-4eb2-928f-939621b5fbb1``
        """
        class_instance = self.get_instance(line)
        if class_instance is not None:
            del storage.all()[class_instance[0]]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
