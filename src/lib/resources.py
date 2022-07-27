import subprocess









# things used to create a python programming env: [used to define the structure of the args passed into the function]
#   project name [required]
#   location to save project folder [required, default arg=documents, can be modified with options passed in from frontend]
#   copy puthon boiler-plate into new project folder
#   initiate local GIT repo in new project folder
#   start a new vscode instance from the new project folder

# default locations for boiler-plate content & location for all project folders
projs_folder_local = f'/media/glitch/2c4828b9-9157-4e11-9376-ce119bd58aa2/glitch/RECENTLY_ADDED/projects/'
boiler_plate_python = f'/media/glitch/2c4828b9-9157-4e11-9376-ce119bd58aa2/glitch/RECENTLY_ADDED/boiler-plates/python/*'

def python_programming_evn(proj_name):
    # ***** create new project folder
    create_project_folder_cmd = f'mkdir {projs_folder_local}/{proj_name}'
    
    try:
        cmd_return = subprocess.Popen(create_project_folder_cmd, shell=True)
        cmd_return.wait()
    except:
        print("error in creating Python Programming Environment")
# ******************************************************************

    # ***** copy content from boiler-plate to project folder

    copy_boiler_plate_content_cmd = f'cp -R {boiler_plate_python} {projs_folder_local}/{proj_name}'

    try:
        cmd_return = subprocess.Popen(copy_boiler_plate_content_cmd, shell=True)
        cmd_return.wait()
    except:
        print("the boiler-plate content failed to copy")
# ******************************************************************

    # ***** Initiate a local GIT repo in the project folder

    initiate_local_git_repo_cmd = f'git init {projs_folder_local}/{proj_name}'
    
    try:
        cmd_return = subprocess.Popen(initiate_local_git_repo_cmd, shell=True)
        cmd_return.wait()
    except:
        print("initiate local GIT repo failed")
    # ******************************************************************

    # Start a vscode instance from the project folder

    start_vscode_instance_cmd = f'code {projs_folder_local}/{proj_name}'

    try:
        cmd_return = subprocess.Popen(start_vscode_instance_cmd, shell=True)
        cmd_return.wait()
    except:
        print("failed to start vscode instance in the project folder")
# ******************************************************************