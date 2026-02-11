from pathlib import Path

def get_list_of_file(path):
    with open(path,'r') as file:
        list_of_lines=[line for line in [w.split(",") for w in file.readlines()]]
    return list_of_lines


def extracting_external_IP_addresses(lst:list):
    list_external_addresses=[l for l in lst if not l[1].strip().startswith("192.168") and not l[1].strip().startswith("10.")]
    return list_external_addresses


def filter_by_sensitive_port(lst:list):
    sensitive = ["22", "23", "3389"]
    list_filtered_by_sensitive_port=[l for l in lst if l[3].strip() in sensitive]
    return list_filtered_by_sensitive_port

def filter_by_size(lst:list):
    list_filter_by_size=list(filter(lambda l:int(l[-1])>5000,lst))
    return list_filter_by_size

def traffic_tagging(lst:list):
    updated_list=["LARGE" if int(row[-1])>5000  else "NORMAL" for row in lst]
    return updated_list
