from config import *

list_of_pys=get_list_of_file("network_traffic.log")

get_the_hour=list(map(lambda time:int(time[0][11:13]), list_of_pys))

convert_from_byte_to_kilobyte=list(map(lambda row:int(row[-1])/1024, list_of_pys))

filter_rows_by_port=list(filter(lambda line:line[3]=="22" or line[3]=="23" or line[3]=="3389",list_of_pys))

nighttime_activity_filtering=list(filter(lambda n:"00:00:00"<= n[0][11:19] <= "00:06:00",list_of_pys))


