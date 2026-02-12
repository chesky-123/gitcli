from config import *

list_of_pis=get_list_of_file("network_traffic.log")

get_the_hour=list(map(lambda time:int(time[0][11:13]),list_of_pis))

convert_from_byte_to_kilobyte=list(map(lambda row:int(row[-1])/1024,list_of_pis))



