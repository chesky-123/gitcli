from pathlib import Path

def get_list_of_file(path):
    with open(path,'r') as file:
        list_of_lines=[line for line in [w.split(",") for w in file.readlines()]]
    return list_of_lines









