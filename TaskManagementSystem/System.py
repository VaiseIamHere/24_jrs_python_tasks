from pathlib import Path

p1 = "TaskManagementSystem/logs.txt"
p2 = "TaskManagementSystem/Task.txt"

def updateLog(str):
    (open(p1,'a')).write(str+"\n")

def addTask():
    Task = input("Enter Task: ")
    file = open(p2,"r")
    lines = file.readlines()
    file.close()
    c = True
    for i in lines:
        if((Task+"\n").lower() == i.lower()):
            print("Task Already Exists.\n")
            updateLog("Adding Unsuccessfull")
            c = False
            break
    if(c):
        file = open(p2,"a")
        file.write(Task+"\n")
        file.close()
        print(Task+" Added Successfully.\n")
        updateLog("Added --> "+Task)

def removeTask():
    Task = input("Enter Task: ")
    file = open(p2,"r")
    lines = file.readlines()
    file.close()
    (open(p2,'w')).write("")
    c = True
    for i in lines:
        if((Task+"\n").lower() == i.lower()):
            lines.remove(i)
            file = open(p2,"a")
            for i in lines:
                file.write(i)
            file.close()
            updateLog("Removed--> "+Task)
            c = False
            print(Task+" Removed Sucessfully.\n")
            break
    if(c):
        file = open(p2,"a")
        for i in lines:
            file.write(i)
        file.close()
        print("Unable to remove !!\n")
        updateLog("Removing Unsucessfull")

def searchTask():
    Task = input("Enter Task: ")
    file = open(p2,"r")
    lines = file.readlines()
    c = True
    for i in lines:
        if((Task+"\n").lower() == i.lower()):
            updateLog("Searched--> "+Task)
            print(Task,"is your Task no.",lines.index(i),"\n")
            c = False
            break
    if(c):
        updateLog("Search Unsuccessfull")
        print("Task not Found.\n")

def showAllTask():
    file = open(p2,"r")
    lines = file.readlines()
    for i in range(1,len(lines)):
        print(lines[i])
    file.close()
    updateLog("All Tasks Presented.")

def clearLog():
    header = "<----- All the Actions performed are Stored here ----->\n"
    (open("TaskManagementSystem/logs.txt",'w')).write(header)
    print("Log Cleared.\n")

def clearTask():
    header = "<----- Saved Tasks are stored here ----->\n"
    (open(p2,'w')).write(header)
    updateLog("All Tasks Cleared.")
    print("All Tasks Removed.\n")
