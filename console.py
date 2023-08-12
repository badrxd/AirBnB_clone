#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
import ast


class HBNBCommand(cmd.Cmd):
    """Represent the HBNB  command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def default(self, line):
        """Handle custom commands
        Attributes:
            line (str): command
        """
        mtd = {
            'all': 'do_all', 'count': 'do_count', 'show': 'do_show',
            'destroy': 'do_destroy', 'update': 'do_update'
        }
        cmds = line.split('.')
        if len(cmds) > 1:
            cmd = cmds[1].split('(')
            if cmd[0] in mtd and cmds[1].endswith(")"):
                match cmd[0]:
                    case "all" | "count":
                        eval("self." + mtd[cmd[0]])(cmds[0])
                    case "show" | "destroy":
                        cls_id = cmds[1].split('"')[1] if '"' \
                                in cmds[1] else "non"
                        arg = "{} {}".format(cmds[0], cls_id)
                        eval("self." + mtd[cmd[0]])(arg)
                    case _:
                        cheack = re.search(r'\{.*\}', cmds[1])
                        cls_id = cmds[1].split('"')[1]
                        if cheack:
                            to_obj = ast.literal_eval(cheack.group())
                            for k, v in to_obj.items():
                                arg = "{} {} {} {}".\
                                     format(cmds[0], cls_id, k, v)
                            print(arg)
                        else:
                            print("not dic")
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """ methode that count the number of the object based on 
        the class name
        Args: 
            arg (str): passing the calss name
        """

        objs = storage.all()
        counter = 0
        if arg not in globals():
            print("** class doesn't exist **")
        else:
            for key in objs:
                if arg in key:
                    counter += 1
            print(counter)

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_create(self, arg):
        """ Creates a new instance BaseModel,and saves prints its id
        """

        args = arg.split()
        if len(args) != 1:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of 
        an instances class name and id
        """

        args = arg.split()
        objs = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) != 2:
            print('** instance id missing **')
        elif "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        else:
            print(objs["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """ Deletes an instance by the class name and id 
        (save changes
        """

        args = arg.split()
        objs = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        else:
            del objs["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of the instances *****
        """

        args = arg.split()
        objs = storage.all()

        if len(arg) > 0 and args[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg) > 0 and args[0] in globals():
            objects = []
            for key in objs:
                if args[0] in key:
                    objects.append(str(objs[key]))
            print(objects)
        else:
            objects = []
            for obj in objs.values():
                objects.append(str(obj))
            print(objects)

    def do_update(self, arg):
        """ Updates an instance based on the class name & id """

        args = shlex.split(arg)
        objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[2]
            value = args[3]
            obj = "{}.{}".format(args[0], args[1])
            if (hasattr(objs[obj], key)):
                attr_type = type(getattr(objs[obj], key))
                try:
                    setattr(objs[obj], key, attr_type(value))
                except ValueError:
                    pass
            else:
                if '.' in value and value.split(".")[0].isdigit()\
                        and value.split(".")[1].isdigit():
                    value = float(value)
                elif value.isdigit():
                    value = int(value)
                else:
                    pass
                setattr(objs[obj], key, value)
            objs[obj].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
