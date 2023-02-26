## Purpose of this program
- from the CLI, create project folders automatically with user input

## Code Walk-thru
- User runs the cmd from the cli to bring up the interactive env

- The interactive env will ask the user the following questons:
  - project folder name
  - project folder save location (absolute path)
  - programming language that will be used for that project

- Create the project folder with the name given

- Copy the boiler-plate files & folders based on the user input as to the programming language being used

- Initiate a local GIT repo in the project folder

- Start a vscode instance from the project folder

## v1.1

Change Log
  - Project directory can be set with Linux environment variable
      - PROJ_FOLDER
        - OR
      - If not set, the default location will be used:
        - /home/[user]/Documents/zero_fox_projects/
          - where [user] is the name of the logged in user
  - If the program is ran with a project name that already exists, the program will exit and inform the user the following
    - a project with that name already exist in the main project PROJ_FOLDER
  - 