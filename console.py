#!/usr/bin/python3
"""
console of the command interpreter
"""
from models.base_model import BaseModel
from models import storage
from ast import Pass
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB cmd.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb)'

    """Stores all classes to be created """
    __inst_classes = {
            "BaseModel",
            "City",
            "User",
            "Amenity",
            "State",
            "Place",
            "Review",
            }

    def emptyline(self):
        """Nothing"""
        pass

    def do_EOF(self, arg):
        """End of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        arg1 = parse(arg)

        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__inst_classes:
            print("** class doesn't exist **")
        elif arg1[0] in HBNBCommand.__inst_classes:
            new = BaseModel()
            new.save()

    def do_show(self, arg):
        """Prints string representation of an instance based
        on the class name and id"""
        arg1 = parse(arg)
        my_storage = storage.all()

        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__inst_classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in my_storage:
            print("** no instance found **")
        else:
            print(my_storage["{}.{}".format(arg1[0], arg1[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg1 = parse(arg)
        my_storage = storage.all()

        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in my_storage:
            print("** no instance found **")
        else:
            my_storage.pop("{}.{}".format(arg1[0], arg1[1]))
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        my_storage = storage.all()
        arg1 = parse(arg)
        my_list = []
        if len(arg1) > 0 and arg[0] not in HBNBCommand.__inst_classes:
            print("** class doesn't exist **")
        for value in my_storage.values():
            if len(arg1) > 0 and arg1[0] == value.__class__.__name__:
                my_list.append(value.__str__())
            elif len(arg1) == 0:
                my_list.append(value.__str__())
        print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        arg1 = parse(arg)
        my_storage = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[1] not in HBNBCommand.__inst_classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in my_storage:
            print("** no instance found **")
        elif len(arg1) == 2:
            print("** attribute name missing **")
        elif len(arg1) == 3 and "{}.{}".format(
                arg1[0], arg1[2]) not in my_storage:
            print("** value missing **")
        elif len(arg1) == 4:
            my_obj = my_storage["{}.{}".format(arg1[0], arg1[1])]
            if arg1[2] in my_obj.__class__.__dict__.keys():
                value = type(my_obj.__class__.dict__[arg1[2]])
                my_obj.__dict__[arg1[2]] = value(arg1[3])
            else:
                my_obj.__dict__[arg1[2]] = arg1[3]

    def do_count(self, arg):
        """Counts number of instances"""
        arg1 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg1[0] == obj.__class__.__name__:
                count += 1
        print(count)


def parse(arg):
    "Convert a series of string to argument list"
    return list(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
