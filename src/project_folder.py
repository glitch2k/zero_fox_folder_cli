#!/bin/python3
import argparse
from kezia.resources import python_programming_evn


parse = argparse.ArgumentParser(description='Create a new project folder')

# first positional argument to accept the project name
parse.add_argument('project_name', metavar='POS_ARG-1',nargs=1, type=str, help='name of the project folder')

# take-in 1st positional argument and pass it into the function
args_pyList = parse.parse_args()
proj_name = args_pyList.project_name[0]


python_programming_evn(proj_name)


