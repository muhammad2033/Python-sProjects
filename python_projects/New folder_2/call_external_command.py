# from setuptools import Command


# make a program for calling an external Command
from subprocess import call
call(["is","-1"])

# simple solution 2

import os
print(os.system('ls -l'))