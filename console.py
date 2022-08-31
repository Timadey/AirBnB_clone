#!/usr/bin/python3
"""
Command interpreter for performing administrative operations
on AirBnb objects
"""
import cmd


class HBNBCommand(cmd.Cmd):
    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
