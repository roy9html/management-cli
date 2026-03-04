import argparse
from rich import print
from utils.storage import load_data, save_data
from models.user import User
from models.project import Project
from models.task import Task

data = load_data()

def add_user(args):
    user = User(args.name, args.email)
    data["users"].append(user.to_dict())
    save_data(data)
    print("User added")

def list_users(args):
    if not data["users"]:
        print("No users found")
        return

    for u in data["users"]:
        print(u["name"], "-", u["email"])

def add_project(args):
    project = Project(
        args.title,
        args.description,
        args.due_date,
        args.user
    )

    data["projects"].append(project.to_dict())

    save_data(data)

    print("Project added")



def list_projects(args):
    found = False

    for p in data["projects"]:
        if args.user is None or p["user"] == args.user:
            print(p["title"], "-", p["user"], "-", p["due_date"])
            found = True

    if not found:
        print("No projects found")

def add_task(args):

    task = Task(
        args.title,
        args.project,
        args.assigned_to
    )

    data["tasks"].append(task.to_dict())
    save_data(data)
    print("Task added")

def complete_task(args):

    for t in data["tasks"]:

        if t["title"] == args.title:
            t["status"] = "completed"
            print("Task marked complete")
            save_data(data)
            return

    print("Task not found")


def main():

    parser = argparse.ArgumentParser(description="Simple project manager CLI")
    sub = parser.add_subparsers()
    user_cmd = sub.add_parser("add-user")
    user_cmd.add_argument("--name")
    user_cmd.add_argument("--email")
    user_cmd.set_defaults(func=add_user)


    list_cmd = sub.add_parser("list-users")
    list_cmd.set_defaults(func=list_users)

    proj_cmd = sub.add_parser("add-project")
    proj_cmd.add_argument("--user")
    proj_cmd.add_argument("--title")
    proj_cmd.add_argument("--description", default="")
    proj_cmd.add_argument("--due_date", default="none")
    proj_cmd.set_defaults(func=add_project)

    proj_list = sub.add_parser("list-projects")
    proj_list.add_argument("--user", required=False)
    proj_list.set_defaults(func=list_projects)

    task_cmd = sub.add_parser("add-task")
    task_cmd.add_argument("--project")
    task_cmd.add_argument("--title")
    task_cmd.add_argument("--assigned_to")
    task_cmd.set_defaults(func=add_task)

    complete_cmd = sub.add_parser("complete-task")
    complete_cmd.add_argument("--title")
    complete_cmd.set_defaults(func=complete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()