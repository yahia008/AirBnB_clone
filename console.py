#!/usr/bin/python3
"""Creating The cmd module for HBNB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for cmd interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self):
        """An end of file command"""
        return True

    def do_quit(self):
        """A quit command command"""
        return True

    def emptyline(self):
        """Do noyhing when line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
