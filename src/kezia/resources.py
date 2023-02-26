import subprocess, os, shutil
from distutils.dir_util import copy_tree









# things used to create a python programming env: [used to define the structure of the args passed into the function]
#   project name [required]
#   location to save project folder [required, default arg=documents, can be modified with options passed in from frontend]
#   copy puthon boiler-plate into new project folder
#   initiate local GIT repo in new project folder
#   start a new vscode instance from the new project folder

# default locations for boiler-plate content & location for all project folders
# projs_folder_local = f'/media/glitch/2c4828b9-9157-4e11-9376-ce119bd58aa2/glitch/RECENTLY_ADDED/projects/'
boiler_plate_python = f'/media/glitch/2c4828b9-9157-4e11-9376-ce119bd58aa2/glitch/RECENTLY_ADDED/boiler-plates/python/'

def python_programming_evn(proj_name):
# ***** create new project folder
    # create_project_folder_cmd = f'mkdir {projs_folder_local}/{proj_name}'

# ***** default path for project folder
# get username of the current user
    user = os.getlogin()

# default project directory path if environment variable is not set
# this will save the project folder in the user's Documents folder called "zero_fox_folder_projects"
    script_default_project_location = '/home/' + user + '/Documents/zero_fox_folder_projects'

# project directory path using environment variable & default path if environment variable is not set
    project_dir = os.environ.get('PROJ_FOLDER', script_default_project_location)

# new directory location
    new_dir = os.path.join(project_dir, proj_name)

    
    # try:
    #     cmd_return = subprocess.Popen(create_project_folder_cmd, shell=True)
    #     cmd_return.wait()
    # except:
    #     print("error in creating Python Programming Environment")

#  create a directory with condition
    try:
        os.mkdir(new_dir)
    except FileExistsError as e:
        print("***********************************")
        print("***********************************")
        print('Python error message: ', e)
        print('The directory already exists')
# ******************************************************************

    # ***** copy content from boiler-plate to project folder
    copy_tree(boiler_plate_python, new_dir)

# ******************************************************************

    # ***** Initiate a local GIT repo in the project folder

    initiate_local_git_repo_cmd = f'git init {new_dir}'
    
    try:
        cmd_return = subprocess.Popen(initiate_local_git_repo_cmd, shell=True)
        cmd_return.wait()
    except:
        print("initiate local GIT repo failed")
    # ******************************************************************

    # Start a vscode instance from the project folder

    start_vscode_instance_cmd = f'code {new_dir}'

    try:
        cmd_return = subprocess.Popen(start_vscode_instance_cmd, shell=True)
        cmd_return.wait()
    except:
        print("failed to start vscode instance in the project folder")
# ******************************************************************