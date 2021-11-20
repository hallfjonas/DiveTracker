import random as rnd
from os import listdir
from os.path import isfile, join
from shutil import copyfile
import os

# Source directory
source_dir = "fish_xml"

def get_files_in_dir(dir):
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    paths = [join(dir, f) for f in files]
    return files, paths

def clear_directory(dir):
    files, paths = get_files_in_dir(dir)

    for p in paths:
        os.remove(p)

clear_directory("train")
clear_directory("test")

i = 1
files, paths = get_files_in_dir(source_dir)
for file in files:
    # Copy about 20% to test dir
    if (rnd.random() >= 0.8):
        dst_dir = "test"
    else:
        dst_dir = "train"

    copyfile(join(source_dir, file), join(dst_dir, file))

    i = i + 1




