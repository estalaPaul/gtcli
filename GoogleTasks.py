from __future__ import print_function
import pickle
import random
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import os

SCOPES = ["https://www.googleapis.com/auth/tasks"]
RESOURCES_DIR = os.environ["GTCLI_RESOURCES_DIR"]
service = None

def authenticate():
    creds = None
    global service
    if os.path.exists(RESOURCES_DIR + "token.pickle"):
        with open(RESOURCES_DIR + "token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(RESOURCES_DIR + "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open(RESOURCES_DIR + "token.pickle", "wb") as token:
            pickle.dump(creds, token)
    service = build('tasks', 'v1', credentials=creds)

def listTaskLists():
    taskLists=fetchTasksLists()
    if not taskLists:
        print('No task lists found.')
    else:
        print('Task lists:')
        i=1
        for taskList in taskLists:
            print(str(i)+": "+taskList['title'])
            i=i+1

def addTaskList(title):
    service.tasklists().insert(body={'title':title}).execute()
    print("The task list " + title + " was added.")

def deleteTaskList(title):
    taskListId=getTaskListId(title)
    if taskListId == "":
        print("No task list with that title was found.")
    else:
        service.tasklists().delete(tasklist=taskListId).execute()
        print("The task list was deleted.")

def renameTaskList(taskList, newTitle):
    taskListId = getTaskListId(taskList)
    if taskListId == "":
        print("No task list with that title was found.")
    else:
        service.tasklists().update(tasklist=taskListId,body={'title': newTitle, 'id': taskListId}).execute()
        print("The task list was updated.")

def listTasks(taskList):
    taskListId = getTaskListId(taskList)
    if taskListId == "":
        print("No task list with that title was found.")
    else:
        tasks = fetchTasks(taskListId)
        if not tasks:
            print('No tasks found.')
        else:
            print("Tasks:\n")
            i = 1
            for task in tasks:
                print(str(i) + ": " + task['title'])
                status = ""
                if task['status'] == "needsAction":
                    status = "Get 'er done"
                else:
                    status = "dunzo"
                print("     Status: " + status)
                if 'notes' in task:
                    print("     Description: " + task['notes'])
                if 'due' in task:
                    print("     Due: " + task['due'])
                if i < len(tasks):
                    print("\n")
                i = i + 1

def addTask(taskList, title, notes):
    taskListId = getTaskListId(taskList)
    if taskListId == "":
        print("No task list with that title was found.")
    else:
        if notes == "":
            body = {'title': title}
        else:
            body = {'title': title, 'notes': notes}
        service.tasks().insert(tasklist=taskListId, body=body).execute()
        print("Task was added to " + taskList + ".")

def deleteTask(taskList):
    taskListId = getTaskListId(taskList)
    if taskList == "":
        print("No task list with that title was found.")
    else:
        tasks = fetchTasks(taskListId)
        if not tasks:
            print('No tasks found.')
        else:
            print('What task do you want to delete?')
            tasksIds=printTaskList(tasks)
            chosenTask = input()
            if chosenTask in tasksIds:
                service.tasks().delete(tasklist=taskListId, task=tasksIds[chosenTask]).execute()
                print("Task was deleted.")
            else:
                print("Pick a number from the list.")
                deleteTask(taskList)

def updateTask(taskList, newTitle, newNotes):
    taskListId = getTaskListId(taskList)
    if taskListId == "":
        print("No task list with that title was found.")
    else:
        tasks = fetchTasks(taskListId)
        if not tasks:
            print('No tasks found.')
        else:
            print('What task do you want to update?')
            tasksIds = printTaskList(tasks)
            chosenTask = input()
            if chosenTask in tasksIds:
                body = {}
                if newTitle == "":
                    body = {"notes": newNotes, "id": tasksIds[chosenTask]}
                elif newNotes == "":
                    body = {"title": newTitle, "id": tasksIds[chosenTask]}
                else:
                    body = {"title": newTitle, "notes": newNotes, "id": tasksIds[chosenTask]}
                service.tasks().update(tasklist=taskListId, task=tasksIds[chosenTask], body=body).execute()
                print("Task was updated.")
            else:
                print("Pick a number from the list.")
                updateTask(taskList, newTitle, newNotes)

def toggleTask(taskList):
    taskListId = getTaskListId(taskList)
    if taskListId == "":
        print("No task list with that title was found.")
    else:
        tasks = fetchTasks(taskListId)
        if not tasks:
            print("No tasks were found.")
        else:
            print("What task do you want to toggle?")
            tasksIds = printTaskList(tasks)
            chosenTask = input()
            if chosenTask in tasksIds:
                status = ""
                printStatus = ""
                if fetchTaskStatus(taskListId, tasksIds[chosenTask]) == "completed":
                    status = "needsAction"
                    printStatus = "marked as Get 'er done"
                else:
                    status = "completed"
                    printStatus = "marked as dunzo"
                body = {"status": status, "id": tasksIds[chosenTask]}
                service.tasks().update(tasklist=taskListId, task=tasksIds[chosenTask], body=body).execute()
                print("Task was " + printStatus)
            else:
                print("Pick a number from the list.")
                toggleTask(taskList)

def clearCompletedTasks(taskList):
    taskListId = getTaskListId(taskList)
    if taskListId == "":
        print("No task list with that title was found.")
    else: 
        service.tasks().clear(tasklist=taskListId).execute()
        print("Completed tasks cleared from " + taskList)

def fetchTaskStatus(taskListId, taskId):
    task = service.tasks().get(tasklist=taskListId, task=taskId).execute()
    return task['status']

def printTaskList(tasks):
    tasksIds = {}
    i = 1
    for task in tasks:
        print(str(i) + ": " + task['title'])
        tasksIds[str(i)] = task['id']
        i = i + 1
    return tasksIds

def fetchTasks(taskListId):
    results = service.tasks().list(tasklist=taskListId).execute()
    tasks = results.get('items', [])
    return tasks

def getTaskListId(title):
    taskListId = ""
    taskLists = fetchTasksLists()
    for taskList in taskLists:
        if taskList['title'] == title:
            taskListId = taskList['id']
    return taskListId

def fetchTasksLists():
    results = service.tasklists().list(maxResults=10).execute()
    taskLists = results.get('items', [])
    return taskLists