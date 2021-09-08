#!/usr/bin/python3

from GoogleTasks import *
import sys

try:
    chosenObject = sys.argv[1]
    if chosenObject == "--help":
        print("Usage: gtcli [OBJECT] [MODIFIER] [ATTRIBUTES]\n"+
                "     Objects:\n"+
                "         tl - Represents a Task List, used to add, rename or delete a Task List.\n"+
                "         t - Represents a Task, used to add, update, complete or delete a Task List.\n"+
                "     Modifiers:\n"+
                "         tl:\n"+
                "             -l - Lists all Task Lists.\n"+
                "             -a [TITLE] - Adds a Task List with the specified title.\n"+
                "             -d [TITLE] - Deletes the Task List with the specified title.\n"+
                "             -r [TITLE] [NEW TITLE] - Changes the title of the Task List with the specified title to the NEW TITLE value passed.\n"+
                "         t:\n"+
                "             -l [TASK LIST] - Lists all Tasks in the specified Task List.\n"+
                "             -a [TASK LIST] [TITLE] optional -n [NOTES] - Adds a note to the specified Task List.\n"+
                "             -d [TASK LIST] - Presents all the Tasks in the specified Task List and allows you to pick a Task to delete.\n"+
                "             -u [TASK LIST] optional -t [TITLE] -n [NOTES] - Presents all the Tasks in the specified Task List and allows you to pick a Task to update with the information passed.\n"+
                "             -t [TASK LIST] - Presents all the Tasks in the specified Task List and allows you to pick a Task to toggle as completed or uncompleted depending on it's current state.\n"+
                "             -c [TASK LIST] - Clears all the completed Tasks from the specified Task List.\n")
    else: 
        try:
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
                                print("Usage: gtcli t -a [TASKLIST] [TITLE] optional -n [NOTES]") 
                        except:
                            pass
                        addTask(taskList, title, notes)
                    except:
                        print("Usage: gtcli t -a [TASKLIST] [TITLE] optional -n [NOTES]")
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
                else:
                    print("Usage: gtcli [OBJECT] [MODIFIER] [ATTRIBUTES]\n"+
                    "Try \"gtcli --help\" for more information.")
        except:
            print("Usage: gtcli [OBJECT] [MODIFIER] [ATTRIBUTES]\n"+
                "Try \"gtcli --help\" for more information.")
except:
    print("Usage: gtcli [OBJECT] [MODIFIER] [ATTRIBUTES]\n"+
        "Try \"gtcli --help\" for more information.")