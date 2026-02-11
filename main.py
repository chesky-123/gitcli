from pathlib import Path

def get_list_of_file(path):
    with open(path,'r') as file:
        list_of_lines=[line for line in [w.split(",") for w in file.readlines()]]
    return list_of_lines


def extracting_external_IP_addresses(lst:list):
    list_external_addresses=[l for l in lst if not l[1].startswith("192.168") if not l[1].startswith("10.")]
    return list_external_addresses




