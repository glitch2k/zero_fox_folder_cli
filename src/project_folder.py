#!/bin/python3

from lib.resources import python_programming_evn









# ******** GET INPUT FROM USER USING THE CLI
msg = f'Enter The Name Of The Project Folder'
print(msg)
proj_name = input('=>')

print()

# msg = f'Enter The Location to Save the Project Folder - [Default = ~/home/$USER/Documents/]'
# print(msg)
# proj_local = input('[y/n] =>')

python_programming_evn(proj_name)


