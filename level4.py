from level3 import *

def open_file(path):
    with open(path,'r') as file:
        for line in file:
            lisr_of_lines=[w for w in line.split(",")]
            yield lisr_of_lines





