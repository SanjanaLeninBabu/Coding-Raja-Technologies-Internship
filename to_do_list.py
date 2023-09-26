import argparse
import json
import os
from datetime import datetime
tasks={}
def add_task(name,description,priority,due_date):
    task={
    "name":name,
    "description":description,
    "priority":priority,
    "due_date":due_date,
    "completed":False
    }
    tasks[name]=task
def remove_task(name):
    if name in tasks:
        del tasks[name]
        return True
    return False
def mark_completed(name):
    if name in tasks:
        tasks[name]["completed"]=True
        return True
    return False
def list_tasks():
    for name, task in tasks.items():
        print(f"name:{task['name']}")
        print(f"description:{task['description']}")
        print(f"priority:{task['priority']}")
        print(f"due date:{task['due_date']}")
        print(f"completed:{'Yes' if task['completed'] else 'No'}")
        print("-"*30)

def save_tasks_to_file():
    with open("tasks.json","w") as file:
        json.dump(tasks,file)
        
def load_task_from_file():
    if os.path.isfile("tasks.json"):
        with open("tasks.json","r")as file:
            loaded_tasks=json.load(file)
            tasks.clear()
            tasks.update(loaded_tasks)
parser=argparse.ArgumentParser(description="Command-line To-Do List Application")
parser.add_argument("command",choices=["add","remove","complete","list"])
parser.add_argument("--name",required=True, help="task name")
parser.add_argument("--description", help="task description")
parser.add_argument("--priority",choices=["high","medium","low"],default="medium",help="task priority")
parser.add_argument("--due_date",help="task due date (YYYY-MM-DD)")
args=parser.parse_args()
load_task_from_file()
if args.command=="add":
    add_task(args.name,args.discription,args.priority,args.due_date)
    print("task added successfully")
elif args.command == "add":
    if remove_task(args.name):
        print("task removed successfully")
    else:
        print("task not found")
elif args.command == "list":
        list_tasks()

save_tasks_to_file()





