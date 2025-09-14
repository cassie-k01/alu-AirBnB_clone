#!/usr/bin/python3
"""Console for AirBnB_clone project."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance, save it, and print its id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        cls = classes.get(args[0])
        if not cls:
            print("** class doesn't exist **")
            return
        instance = cls()
        storage.new(instance)
        storage.save()
        print(instance.id)

    def do_show(self, arg):
        """Show string representation of an instance by class and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all instance strings, optionally by class"""
        args = shlex.split(arg)
        objs = storage.all().values()
        if args and args[0] not in classes:
            print("** class doesn't exist **")
            return
        result = []
        for obj in objs:
            if not args or obj.__class__.__name__ == args[0]:
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance by adding or updating attribute."""
        try:
            args = shlex.split(arg)
        except ValueError:
            print("** Invalid command format **")
            return

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        attr_name, attr_val = args[2], args[3]
        try:
            if hasattr(obj, attr_name):
                current_type = type(getattr(obj, attr_name))
                if current_type in [int, float]:
                    attr_val = current_type(attr_val)
        except Exception:
            pass
        setattr(obj, attr_name, attr_val)
        obj.save()
        storage.save()

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_EOF(self, arg):
        """Exit the console on EOF."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the console."""
        return True


if __name__ == "__main__":
    storage.reload()
    HBNBCommand().cmdloop()
