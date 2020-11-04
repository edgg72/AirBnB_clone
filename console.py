#!/usr/bin/python3
"""
program that contains the entry point of the command interpreter
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "
    __dictio = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

    def returdic(self):
        """return dictionary with all classes"""
        return self.__dictio

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """nothing happen"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        try:
            if not line:
                raise SyntaxError()
            if line not in self.returdic().keys():
                raise NameError()
            new = self.returdic()[line]()
            new.save()
            print(new.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        try:
            if not line:
                raise SyntaxError()
            name = line.split()
            if name[0] not in self.returdic().keys():
                raise NameError()
            if len(name) > 2:
                raise IndexError()
            objects = storage.all()
            real = name[0] + "." + name[1]
            if real not in objects:
                raise KeyError()
            print(objects[real])
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        try:
            if not line:
                raise SyntaxError()
            name = line.split()
            if name[0] not in self.returdic().keys():
                raise NameError()
            if len(name) < 2:
                raise IndexError()
            objects = storage.all()
            real = name[0] + "." + name[1]
            if real not in objects:
                raise KeyError()
            objects.pop(real)
            storage.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()
        my_list = []
        if not line:
            for key in objects:
                my_list.append(str(objects[key]))
            print(my_list)
            return
        try:
            if line not in self.returdic().keys():
                raise NameError()
            my_list = []
            for key in objects:
                keygen = (key.split("."))[0]
                if keygen == line:
                    my_list.append(str(objects[key]))
            print(my_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        try:
            if not line:
                raise SyntaxError()
            name = line.split()
            if name[0] not in self.returdic().keys():
                raise NameError()
            if len(name) < 2:
                raise IndexError()
            objects = storage.all()
            key = name[0] + "." + name[1]
            if key not in objects:
                raise KeyError()
            if len(name) < 3:
                raise AttributeError()
            if len(name) < 4:
                raise ValueError()
            try:
                x = int(name[3].replace('"', ''))
            except ValueError:
                try:
                    x = float(name[3].replace('"', ''))
                except ValueError:
                    try:
                        x = str(name[3].replace('"', ''))
                    except ValueError:
                        pass
            setattr(objects[str(name[0]) + "." + str(name[1])], name[2], x)
            storage.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def default(self, line):
        """evaluates line"""
        aux = line.split(".")
        if len(aux) > 1:
            if aux[1] == "all()":
                self.do_all(aux[0])
            elif aux[1] == "count()":
                self.do_count(aux[0])
            elif (aux[1])[:4] == "show":
                """class.show("id") id must to be in double quotes"""
                self.do_show(aux[0] + " " + (aux[1])[6:42])
            elif (aux[1])[:7] == "destroy":
                """class.destroy("id") id must to be in double quotes"""
                self.do_destroy(aux[0] + " " + (aux[1])[9:45])
            elif (aux[1])[:6] == "update" and (aux[1]).find(":") == -1:
                line = aux[0] + " "
                line += (aux[1].replace(",", "")).replace('"', "")[7:-1]
                self.do_update(line)
            elif (aux[1])[:6] == "update" and (aux[1]).find(":") > -1:
                id_aux = (aux[1])[8:44]
                """new_line = (aux[1])[46:-1]
                new_line = new_line.replace("'", "").replace('"', "")
                new_line = new_line.replace("{", "").replace("}", "")
                new_line = new_line.split(",")
                my_list = []
                for element in new_line:
                    my_list.append(element.split(":"))
                for i in range(len(my_list)):
                    line = aux[0] + " "
                    line += id_aux + my_list[i][0] + my_list[i][1]
                    self.do_update(line)"""
                aux_dic = json.loads(((aux[1])[47:-1]).replace("'", '"'))
                for key, value in aux_dic.items():
                    if value:
                        line = aux[0] + " "
                        line += id_aux + " " + key + " " + str(value)
                        self.do_update(line)
                return

    def do_count(self, line):
        """
        retrieve the number of instances of a
        class: <class name>.count()
        """
        try:
            name = line.split()
            if name[0] not in self.returdic().keys():
                raise NameError()
            counter = 0
            for key, value in (storage.all()).items():
                if name[0] in key:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
