#!/usr/bin/python3

from GoogleTasks import *
import sys

try:
    chosenObject = sys.argv[1]
    modifier = sys.argv[2]
    authenticate()

    if chosenObject == "tl":
        if modifier == "-l":
            listTaskLists()
        elif modifier == "-a":
            try:
                title = sys.argv[3]
                addTaskList(title)
            except:
                print("Usage: gtcli tl -a [TITLE]")
        elif modifier == "-d":
            try:
                tasklist = sys.argv[3]
                deleteTaskList(tasklist)
            except:
                print("Usage: gtcli tl -d [TITLE]")
        elif modifier == "-r":
            try:
                taskList = sys.argv[3]
                newTitle = sys.argv[4]
                renameTaskList(taskList, newTitle)
            except:
                print("Usage: gtcli tl -r [TASKLIST] [NEW TITLE]")
    elif chosenObject == "t":
        if modifier == "-l":
            try:
                taskList = sys.argv[3]
                listTasks(taskList)
            except:
                print("Usage: gtcli t -l [TASKLIST]")
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
            try:
                taskList = sys.argv[3]
                deleteTask(taskList)
            except:
                print("Usage: gtcli t -d [TASKLIST]")
        elif modifier == "-u":
            try:
                taskList = sys.argv[3]
                title = ""
                notes = ""
                try:
                    firstFlag = sys.argv[4]
                    title = ""
                    notes = ""
                    if firstFlag == "-t":
                        try: 
                            title = sys.argv[5]
                        except:
                            print("No title was provided.")
                    elif firstFlag == "-n":
                        try: 
                            notes = sys.argv[5]
                        except:
                            print("No notes were provided.")
                    else:
                        print("Usage: gtcli t -u [TASKLIST] optional -t [NEW TITLE] -n [NEW NOTES]")
                    try:
                        secondFlag = sys.argv[6]
                        if secondFlag == "-n":
                            try:
                                notes = sys.argv[7]
                                updateTask(taskList, title, notes)
                            except:
                                print("No notes were provided.")
                        else:
                            print("Usage: gtcli t -u [TASKLIST] optional -t [NEW TITLE] -n [NEW NOTES]")
                    except:
                        updateTask(taskList, title, notes)
                except:
                    print("You must update either the title or the notes.")
            except:
                print("Usage: gtcli t -u [TASKLIST] optional -t [NEW TITLE] -n [NEW NOTES]")
        elif modifier == "-t":
            try:
                taskList = sys.argv[3]
                toggleTask(taskList)
            except:
                print("Usage: gtcli t -t [TASKLIST]")
        elif modifier == "-c":
            try:
                taskList = sys.argv[3]
                clearCompletedTasks(taskList)
            except:
                print("Usage: gtcli t -c [TASKLIST]")
except:
    print("Usage: gtcli [OBJECT] [MODIFIER]\n"+
          "Try \"gtcli --help\" for more information.")