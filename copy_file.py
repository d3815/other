#!/bin/python

import os
import shutil

dir_path = 'dir_name'
tree = os.walk(dir_path)
list = []

for i in os.walk(dir_path):
    list.append(i)

path_f = []
for d, dirs, files in os.walk(dir_path):
    for one_file in files:
        path = os.path.join(d, one_file)
        shutil.copy2(path, "dir_to_copy")