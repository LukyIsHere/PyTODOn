#!/usr/bin/python3
from functions import *

# init
if(os.path.isfile(path) != True):
    notes = open(path, "w")
    notes.close()

todolist = load(path)
show(todolist)

# main loop
while(1):
    usrInput = input(promptcol+prompt+END)
    if(" " in usrInput):
        command, parameter = usrInput.split(' ', 1)
    else:
        command = usrInput
        parameter = ""

    if(command == "new" or command == "n"):
        new(todolist, parameter)

    elif(command == "write" or command == "w"):
        save(todolist, path)
        todolist = load(path)

    elif(command == "remove" or command == "rm"):
        remove(todolist, parameter)

    elif(command == "quit" or command == "q" or command == "exit" or command == "x"):
        if(writeonexit == True):
            save(todolist, path)
        print("\033c", end="")
        exit()

    elif(command == "clear" or command == "cl"):
        delete()
        todolist = load(path)

    elif(command == "date" or command == "d"):
        cdate(todolist, parameter)

    else:
        change_flag(todolist, command, parameter)

    show(todolist)
