#!/usr/bin/python3

from GoogleTasks import *
import sys

# try:
chosenObject = sys.argv[1]
modifier = sys.argv[2]
authenticate()

if chosenObject == "tl":
    if modifier == "-l":
        listTaskLists()
    elif modifier == "-a":
        title = sys.argv[3]
        addTaskList(title)
    elif modifier == "-d":
        tasklist = sys.argv[3]
        deleteTaskList(tasklist)
    elif modifier == "-r":
        taskList = sys.argv[3]
        newTitle = sys.argv[4]
        renameTaskList(taskList, newTitle)
elif chosenObject == "t":
    if modifier == "-l":
        taskList = sys.argv[3]
        listTasks(taskList)
    elif modifier == "-a":
        try: 
            taskList = sys.argv[3]
            title = sys.argv[4]
            notes = ""
            try:
                notesFlag = sys.argv[5]
                try:
                    notes = sys.argv[6]
                except:
                    print("Usage: gtcli t -a [TASKLIST] [TITLE] optional -n [notes]") 
            except:
                pass
            addTask(taskList, title, notes)
        except:
            print("Usage: gtcli t -a [TASKLIST] [TITLE] optional -n [notes]")
    elif modifier == "-d":
        taskList = sys.argv[3]
        deleteTask(taskList)
    elif modifier == "-u":
        # try:
        taskList = sys.argv[3]
        title = ""
        notes = ""
        try:
            title = sys.argv[4]
        except:
            pass
        try: 
            notes = sys.argv[5]
        except:
            pass
        if title == "" and notes == "":
            print("You must update either the title or the notes.")
        else:
            updateTask(taskList, title, notes)
        # except:
        #     print("Usage: gtcli t -u [TASKLIST] [NEW TITLE] [NEW NOTES]")
# except:
#     print("Usage: gtcli [OBJECT] [MODIFIER]\n"+
#           "Try \"gtcli --help\" for more information.")