from main import get_list_of_file

def counting_calls_by_IP(lst:list):
    data={}
    for line in lst:
        if line[1] not in data:
            data[line[1]]=0
        data[line[1]]+=1
    return data

def port_to_protocol_mapping(lst:list):
    data={line[3]:line[4] for line in lst}
    return data




