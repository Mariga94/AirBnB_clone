#!/usr/bin/python3
"""
console of the command interpreter
"""
from ast import Pass
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """End of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
