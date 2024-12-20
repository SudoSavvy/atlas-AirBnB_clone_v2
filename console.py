#!/usr/bin/python3
""" console module """
import cmd
import sys
import re
import json
import models
import ast
import shlex
from shlex import split
from models.base_model import BaseModel
from models.__init__ import storage
from models import storage
from shlex import split
from models import storage
from datetime import datetime
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


# Define the classes dictionary to map class names to classes
classes = {
    "State": State,
    "City": City,
    "User": User,
    "Place": Place
}


class HBNBCommand(cmd.Cmd):
    """ console class """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """ prints if isatty false """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """ reformat command line for alter syntax """
        _cmd = _cls = _id = _args = ''

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]

            _cls = pline[:pline.find('.')]

            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:

                pline = pline.partition(', ')

                _id = pline[0].replace('\"', '')

                pline = pline[2].strip()
                if pline:

                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')

            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """ prints if isatty false """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ quit command to exit program """
        exit()

    def help_quit(self):
        """ prints help documentation for quit """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ prints help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ overrides emptyline method of CMD """
        pass

    import re

    def do_create(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        # Create a new instance of the specified class
        new_instance = classes[class_name]()

        # Set attributes passed as parameters
        for param in args[1:]:
            if "=" in param:
                key, value = param.split("=", 1)
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace("_", " ")
                elif "." in value:
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        continue
                setattr(new_instance, key, value)

        # Save the new instance
        storage.new(new_instance)
        storage.save()

        # Print the ID to confirm creation
        print(new_instance.id)

    def help_create(self):
        """ help info for create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, arg):
        args = arg.split()
        if len(args) < 2:
            print("** class name or ID missing **")
            return

        class_name, instance_id = args[0], args[1]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            # Convert obj to dictionary and filter out undesired attributes
            if hasattr(obj, "to_dict"):
                obj_dict = obj.to_dict()
            else:
                obj_dict = obj.__dict__.copy()
            obj_dict.pop('_sa_instance_state', None)  # Rmv SQLA state if exis
            # Format the output as expected
            print("[{}] ({}) {}".format(class_name, obj.id, obj_dict))

    def help_show(self):
        """ help info for show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ destroys specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ help info for destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ shows all objects or all objects of class """
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ help info for all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """ count current number of class instances """
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ help info for help command """
        print("Counts current active class instances")
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ updates specified object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not att_name and args[0] != ' ':
                att_name = args[0]

            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):

            if (i % 2 == 0):
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return

                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        """ help info for update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
