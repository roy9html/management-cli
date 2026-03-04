# CLI Project Management Tool

## About the Project

This is a simple command line tool built with Python.
It is used to manage users, projects, and tasks for a small development team.

The program allows an admin to:

1. create users
2. add projects for users
3. assign tasks to projects
4. mark tasks as completed
5. view projects that belong to a specific user

All the information is saved locally using a JSON file so the data is not lost when the program stops.

## Project Files

project_manager_cli
│
├── main.py
├── requirements.txt
├── data/
│   └── database.json
├── models/
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   └── storage.py
└── test/
    └── test_basic.py

main.py – runs the CLI program
models – contains the classes for users, projects and tasks
utils – helper functions for saving and loading data
data – stores the JSON database
test – contains simple tests using pytest

## Setup

Make sure Python is installed.

Install the required packages:

pip install -r requirements.txt

## Running the Program

## Run the CLI with:
python main.py
This will show the available commands.

## Example Commands:

## Create a user
python main.py add-user --name Alex --email alex@mail.com

## List users
python main.py list-users

## Add a project
python main.py add-project --user Alex --title "CLI Tool"

## Show projects for a user
python main.py list-projects --user Alex

## Add a task
python main.py add-task --project "CLI Tool" --title "Build CLI" --assigned_to Alex

## Complete a task
python main.py complete-task --title "Build CLI"

## Running Tests
To run the tests:
pytest:

## Author
Nyaga Murimi


