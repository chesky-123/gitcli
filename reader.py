from config import *

listi=list_of_pys=get_list_of_file("network_traffic.log")

get_the_hour=list(map(lambda time:int(time[0][11:13]), list_of_pys))

convert_from_byte_to_kilobyte=list(map(lambda row:int(row[-1])/1024, list_of_pys))

filter_rows_by_port=list(filter(lambda line:line[3]=="22" or line[3]=="23" or line[3]=="3389",list_of_pys))

nighttime_activity_filtering=list(filter(lambda n:"00:00:00"<= n[0][11:19] <= "00:06:00",list_of_pys))

suspicion_checks = { "EXTERNAL_IP": lambda row: True if not row[1].strip().startswith("192.168") and not row[1].strip().startswith("10.") else False,
                    "SENSITIVE_PORT": lambda row: True if row[3]=="22" or row[3]=="23" or row[3]=="3389" else False,
                     "LARGE_PACKET":lambda row: True if int(row[-1])>5000 else False,
                     "NIGHT_ACTIVITY": lambda row: True if "00:00:00"<= row[0][11:19] <= "00:06:00" else False}


def running_tests_on_a_line(line,dicti=suspicion_checks):
    return list(filter(lambda key:dicti[key](line) ,dicti))


processing_the_entire_log=list(filter(lambda l:len(l)>=1,list(map(lambda line:running_tests_on_a_line(line),listi))))

