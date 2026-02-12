from main import *

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

def filter_by_time(lst:list):
    return [row for row in lst if "00:00:00"<= row[0][11:19] <= "00:06:00"]

def suspicion_detection_for_each_IP(lst:list):
    data={}
    for line in lst:
        if line[1] not in data:
            data[line[1]]=[]
        if line[1] in extracting_external_IP_addresses(lst) and "IP_EXTERNAL" not in data[line[1]]:
            data[line[1]].append("IP_EXTERNAL")
        if line in filter_by_sensitive_port(lst) and "PORT_SENSITIVE" not in data[line[1]]:
            data[line[1]].append("PORT_SENSITIVE")
        if line in filter_by_size(lst) and "PACKET_LARGE" not in data[line[1]]:
            data[line[1]].append("PACKET_LARGE")
        if line in filter_by_time(lst) and "ACTIVITY_NIGHT" not in data[line[1]]:
            data[line[1]].append("ACTIVITY_NIGHT")
    return data



